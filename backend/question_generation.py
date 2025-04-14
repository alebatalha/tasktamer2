import re
import random
from typing import List, Dict, Any, Optional
import logging
from urllib.parse import urlparse
from tenacity import retry, stop_after_attempt, wait_exponential
from utils.fallback_detector import USING_NLTK_FALLBACK
from utils.content_fetcher import process_url
import nltk


try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
    
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_keywords(text: str, max_keywords: int = 50) -> List[str]:
    
    try:
        if not text or not isinstance(text, str):
            logger.warning("Invalid text input for keyword extraction.")
            return []

     
        text = text[:10000].lower()

        if USING_NLTK_FALLBACK:
            try:
                import nltk
                from nltk.corpus import stopwords
                from nltk.tokenize import word_tokenize
                
                stop_words = set(stopwords.words('english'))
                words = word_tokenize(text)
                
                keywords = [word for word in words if word.isalnum() and 
                           word not in stop_words and len(word) > 3]
                
                return keywords[:max_keywords]
            except (ImportError, LookupError) as e:
                logger.warning(f"NLTK fallback failed: {str(e)}. Using regex-based keyword extraction.")
        
       
        words = re.findall(r'\b[a-z][a-z-]+\b', text)
        
        stopwords = {
            'the', 'a', 'an', 'and', 'or', 'but', 'if', 'then', 'else', 'when',
            'at', 'from', 'by', 'for', 'with', 'about', 'against', 'between',
            'into', 'through', 'during', 'before', 'after', 'above', 'below',
            'to', 'of', 'in', 'on', 'as', 'is', 'are', 'was', 'were', 'be', 'been',
            'has', 'have', 'had', 'do', 'does', 'did', 'can', 'could', 'will',
            'would', 'should', 'might', 'that', 'this', 'these', 'those', 'it',
            'they', 'them', 'their', 'he', 'she', 'his', 'her', 'we', 'us', 'our',
            'you', 'your', 'i', 'me', 'my'
        }
        
        
        keywords = [word for word in words if word not in stopwords and len(word) > 3]
        
        
        keyword_counts = {}
        for word in keywords:
            keyword_counts[word] = keyword_counts.get(word, 0) + 1
            
        sorted_keywords = sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)
        return [word for word, _ in sorted_keywords[:max_keywords]]
    except Exception as e:
        logger.error(f"Error extracting keywords: {str(e)}", exc_info=True)
        return []

def get_distractors(keywords: List[str], correct_answer: str) -> List[str]:
    
    try:
       
        filtered_keywords = [w for w in keywords if w.lower() != correct_answer.lower()]
        
        
        if len(filtered_keywords) >= 3:
            return random.sample(filtered_keywords, 3)
        
      
        distractors = filtered_keywords.copy()
        
        answer_len = len(correct_answer)
        variations = [
            f"{correct_answer[:2]}ing" if answer_len > 3 else "thing",
            f"{correct_answer[:2]}ed" if answer_len > 3 else "item",
            f"{correct_answer[:2]}er" if answer_len > 3 else "unit"
        ]
        distractors.extend(variations[:3 - len(distractors)])
        
        return distractors[:3]
    except Exception as e:
        logger.error(f"Error generating distractors: {str(e)}", exc_info=True)
        return ["option_1", "option_2", "option_3"]

def create_fill_in_blank_question(sentence: str, keywords: List[str]) -> Dict[str, Any]:
  
    try:
        if not sentence or not isinstance(sentence, str) or len(sentence.strip()) < 10:
            logger.debug(f"Invalid or too short sentence: {sentence[:50]}...")
            return {}

        words = sentence.split()
        if len(words) < 5:  
            return {}
            
 
        potential_blanks = []
        for i in range(2, len(words) - 2):
            word = words[i]
         
            cleaned_word = re.sub(r'[^\w\s]', '', word).lower()
            
           
            if (len(cleaned_word) > 3 and 
                cleaned_word not in {'with', 'that', 'this', 'from', 'their', 'about'} and
                cleaned_word in [k.lower() for k in keywords]):
                potential_blanks.append((i, cleaned_word))
        
        if not potential_blanks:
            logger.debug(f"No suitable words for blank in sentence: {sentence[:50]}...")
            return {}
        
     
        blank_pos, correct_answer = random.choice(potential_blanks)
        
      
        question_words = words.copy()
        question_words[blank_pos] = "_____"
        question = " ".join(question_words)
        
       
        distractors = get_distractors(keywords, correct_answer)
        
      
        options = [correct_answer] + distractors
        random.shuffle(options)
        
        return {
            "question": f"Fill in the blank: {question}",
            "options": options,
            "answer": correct_answer
        }
    except Exception as e:
        logger.error(f"Error creating question: {str(e)}", exc_info=True)
        return {}

def get_sentences(text: str) -> List[str]:
    
    try:
        if not text or not isinstance(text, str):
            logger.warning("Invalid text input for sentence splitting.")
            return []

    
        text = re.sub(r'\s+', ' ', text.strip())
        if len(text) < 10:
            return []

       
        if USING_NLTK_FALLBACK:
            try:
                import nltk
                from nltk.tokenize import sent_tokenize
                
                return sent_tokenize(text)
            except Exception as e:
                logger.warning(f"NLTK sentence tokenization failed: {str(e)}")
 
        return re.split(r'(?<=[.!?])\s+', text)
    except Exception as e:
        logger.error(f"Error splitting sentences: {str(e)}", exc_info=True)
        return []

def generate_quiz(content: Optional[str] = None, url: Optional[str] = None, num_questions: int = 3) -> List[Dict[str, Any]]:

    try:
        
        if content and isinstance(content, str) and content.strip():
            content = re.sub(r'\s+', ' ', content.strip())
        elif url:
            content = process_url(url)
            if not content or isinstance(content, str) and content.startswith(("Error", "Invalid", "No readable")):
                logger.warning(f"Failed to fetch content from URL: {url}")
                return [{"error": f"Unable to fetch content: {content}"}]
        else:
            logger.warning("No valid content or URL provided for quiz generation.")
            return [{"error": "Please provide text or a valid URL."}]
        
       
        if not content or len(content) < 100:
            logger.warning("Content too short for quiz generation.")
            return [{"error": "Content is too short to generate questions."}]
        
       
        num_questions = max(1, min(num_questions, 10))
        
        
        sentences = get_sentences(content)
        if len(sentences) < 3:
            logger.warning("Not enough sentences to generate quiz.")
            return [{"error": "Not enough sentences to create questions."}]
        
        keywords = extract_keywords(content)
        if not keywords:
            logger.warning("No keywords extracted from content.")
            return [{"error": "Unable to extract keywords for questions."}]
        
        
        valid_sentences = [s for s in sentences if len(s.split()) >= 5 and len(s) >= 20]
        if not valid_sentences:
            logger.warning("No valid sentences for quiz generation.")
            return [{"error": "No suitable sentences found for questions."}]
        
        
        if len(valid_sentences) < num_questions:
            valid_sentences = valid_sentences * (num_questions // len(valid_sentences) + 1)
        
       
        selected_sentences = random.sample(valid_sentences, min(num_questions * 2, len(valid_sentences)))
        
      
        quiz = []
        for sentence in selected_sentences:
            question = create_fill_in_blank_question(sentence, keywords)
            if question and len(quiz) < num_questions:
                quiz.append(question)
        
        
        remaining_sentences = [s for s in valid_sentences if s not in selected_sentences]
        attempts = 0
        
        while len(quiz) < num_questions and remaining_sentences and attempts < 3:
            more_sentences = random.sample(remaining_sentences, min(num_questions - len(quiz), len(remaining_sentences)))
            for sentence in more_sentences:
                question = create_fill_in_blank_question(sentence, keywords)
                if question and len(quiz) < num_questions:
                    quiz.append(question)
            
            remaining_sentences = [s for s in remaining_sentences if s not in more_sentences]
            attempts += 1
        
        
        if len(quiz) < num_questions:
            logger.info("Falling back to simple quiz generation.")
            simple_quiz = generate_simple_quiz(content, num_questions - len(quiz))
            if simple_quiz and not "error" in simple_quiz[0]:
                quiz.extend(simple_quiz)
        
        if not quiz:
            logger.warning("Failed to generate any quiz questions.")
            return [{"error": "Unable to generate questions from the provided content."}]
        
        logger.info(f"Generated {len(quiz)} quiz questions.")
        return quiz
    except Exception as e:
        logger.error(f"Error generating quiz: {str(e)}", exc_info=True)
        return [{"error": f"Failed to generate quiz: {str(e)}"}]

def generate_simple_quiz(content: str, num_questions: int = 3) -> List[Dict[str, Any]]:
   
    try:
        sentences = get_sentences(content)
        sentences = [s for s in sentences if len(s) > 30]
        
        if len(sentences) < 3:
            return [{"error": "Not enough content for quiz generation"}]
        
        quiz = []
        for i in range(min(num_questions, len(sentences))):
            sentence = sentences[i]
            words = sentence.split()
            
            if len(words) < 5:
                continue
                
      
            blank_index = random.randint(2, len(words) - 3)
            answer = re.sub(r'[^\w]', '', words[blank_index]).lower()
            
      
            if len(answer) < 3:
                continue
                
            question_words = words.copy()
            question_words[blank_index] = "_____"
            
            options = [answer]

            for j in range(3):
                if len(words) > blank_index + j + 1:
                    other_word = re.sub(r'[^\w]', '', words[blank_index + j + 1]).lower()
                    if len(other_word) > 2 and other_word != answer and other_word not in options:
                        options.append(other_word)
                        continue
                
           
                other_word = f"option{j+1}"
                options.append(other_word)
                
            if len(set(options)) < 4:  
                for j in range(10):
                    if len(options) >= 4:
                        break
                    options.append(f"option{j}")
                options = list(set(options))[:4]
                
            random.shuffle(options)
            
            quiz.append({
                "question": f"Fill in the blank: {' '.join(question_words)}",
                "options": options,
                "answer": answer
            })
        
        return quiz
    except Exception as e:
        logger.error(f"Error generating simple quiz: {str(e)}", exc_info=True)
        return [{"error": f"Failed to generate simple quiz: {str(e)}"}]