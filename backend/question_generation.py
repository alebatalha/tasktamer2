import re
import random
from typing import List, Dict, Any, Optional
import logging
from urllib.parse import urlparse
from tenacity import retry, stop_after_attempt, wait_exponential
from utils.fallback_detector import USING_NLTK_FALLBACK
from utils.content_fetcher import process_url


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
                
                nltk.data.find('corpora/stopwords')
                
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
        
        return keywords[:max_keywords]
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
        return ["item_1", "item_2", "item_3"]

def create_fill_in_blank_question(sentence: str, keywords: List[str]) -> Dict[str, Any]:
 
    try:
        if not sentence or not isinstance(sentence, str) or len(sentence.strip()) < 10:
            logger.debug(f"Invalid or too short sentence: {sentence[:50]}...")
            return {}

        words = sentence.split()
        if len(words) < 3:
            return {}
            
        potential_blanks = []
        for i in range(2, len(words) - 2):
            word = words[i]
            if len(word) > 3 and word.lower() not in {'with', 'that', 'this', 'from', 'their', 'about'}:
                cleaned_word = re.sub(r'[^\w\s]', '', word)
                if cleaned_word:
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
            import nltk
            from nltk.tokenize import sent_tokenize
            
            nltk.data.find('tokenizers/punkt')
            
            return sent_tokenize(text)
        
        return re.split(r'(?<=[.!?])\s+', text)
    except Exception as e:
        logger.error(f"Error splitting sentences: {str(e)}", exc_info=True)
        return []

def generate_quiz(content: Optional[str] = None, url: Optional[str] = None, num_questions: int = 3) -> List[Dict[str, Any]]:
    
    try:
        if content and isinstance(content, str) and content.strip():
            content = re.sub(r'\s+', ' ', content.strip())
        elif url:
            content = process_url(url)  # Relies on content_fetcher.py's retries
            if not content or content.startswith(("Error", "Invalid", "No readable")):
                logger.warning(f"Failed to fetch content from URL: {url}")
                return [{"error": f"Unable to fetch content: {content}"}]
        else:
            logger.warning("No valid content or URL provided for quiz generation.")
            return [{"error": "Please provide text or a valid URL."}]
        
        if not content or len(content) < 50:
            logger.warning("Content too short for quiz generation.")
            return [{"error": "Content is too short to generate questions."}]
        
        num_questions = max(1, min(num_questions, 10))
        
        sentences = get_sentences(content)
        if len(sentences) < 2:
            logger.warning("Not enough sentences to generate quiz.")
            return [{"error": "Not enough sentences to create questions."}]
        
        keywords = extract_keywords(content)
        if not keywords:
            logger.warning("No keywords extracted from content.")
            return [{"error": "Unable to extract keywords for questions."}]
        
        valid_sentences = [s for s in sentences if len(s.split()) >= 3 and len(s) >= 10]
        if not valid_sentences:
            logger.warning("No valid sentences for quiz generation.")
            return [{"error": "No suitable sentences found for questions."}]
        
        if len(valid_sentences) < num_questions:
            valid_sentences = valid_sentences * (num_questions // len(valid_sentences) + 1)
        
        selected_sentences = random.sample(valid_sentences, min(num_questions, len(valid_sentences)))
        
        quiz = []
        for sentence in selected_sentences:
            question = create_fill_in_blank_question(sentence, keywords)
            if question:
                quiz.append(question)
        
        while len(quiz) < num_questions and len(valid_sentences) > len(quiz):
            remaining = [s for s in valid_sentences if s not in [q["question"].split(": ")[1] for q in quiz]]
            if not remaining:
                break
                
            new_sentence = random.choice(remaining)
            question = create_fill_in_blank_question(new_sentence, keywords)
            if question:
                quiz.append(question)
        
        if not quiz:
            logger.warning("Failed to generate any quiz questions.")
            return [{"error": "Unable to generate questions from the provided content."}]
        
        logger.info(f"Generated {len(quiz)} quiz questions.")
        return quiz
    except Exception as e:
        logger.error(f"Error generating quiz: {str(e)}", exc_info=True)
        return [{"error": f"Failed to generate quiz: {str(e)}"}]