import re
import random
from typing import List, Dict, Any, Optional
import logging
from urllib.parse import urlparse
from utils.fallback_detector import USING_NLTK_FALLBACK
from utils.content_fetcher import process_url, fetch_webpage_content


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_keywords(text: str) -> List[str]:
    try:
        if USING_NLTK_FALLBACK:
            try:
                import nltk
                from nltk.corpus import stopwords
                from nltk.tokenize import word_tokenize
                
                
                nltk.data.find('corpora/stopwords')
                
                stop_words = set(stopwords.words('english'))
                words = word_tokenize(text.lower())
                
                keywords = [word for word in words if word.isalnum() and 
                           word not in stop_words and len(word) > 3]
                
                return keywords
            except (ImportError, LookupError) as e:
                logger.warning(f"NLTK fallback failed: {str(e)}. Using regex-based keyword extraction.")
        
        words = re.findall(r'\b[A-Za-z][A-Za-z-]+\b', text)
        
        stopwords = {'the', 'a', 'an', 'and', 'or', 'but', 'if', 'then', 'else', 'when', 
                    'at', 'from', 'by', 'for', 'with', 'about', 'against', 'between',
                    'into', 'through', 'during', 'before', 'after', 'above', 'below',
                    'to', 'of', 'in', 'on', 'as', 'is', 'are', 'was', 'were', 'be', 'been',
                    'has', 'have', 'had', 'do', 'does', 'did', 'can', 'could', 'will',
                    'would', 'should', 'might', 'that', 'this', 'these', 'those', 'it',
                    'they', 'them', 'their', 'he', 'she', 'his', 'her', 'we', 'us', 'our',
                    'you', 'your', 'i', 'me', 'my'}
        
        keywords = [word for word in words if word.lower() not in stopwords and len(word) > 3]
        
        return keywords
    except Exception as e:
        logger.error(f"Error extracting keywords: {str(e)}", exc_info=True)
        return []

def get_distractors(keywords: List[str], correct_answer: str) -> List[str]:
    try:
        filtered_keywords = [w for w in keywords if w.lower() != correct_answer.lower()]
        
        if len(filtered_keywords) < 3:
           
            distractors = []
            base_words = ["concept", "item", "term"]
            for i in range(3 - len(filtered_keywords)):
                distractors.append(f"Related {base_words[i % len(base_words)]} {i + 1}")
            distractors.extend(filtered_keywords)
            return distractors[:3]
        
        distractors = random.sample(filtered_keywords, min(3, len(filtered_keywords)))
        
        return distractors
    except Exception as e:
        logger.error(f"Error generating distractors: {str(e)}", exc_info=True)
        return ["Related concept 1", "Related item 2", "Related term 3"]

def create_fill_in_blank_question(sentence: str, keywords: List[str]) -> Dict[str, Any]:
    try:
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
        if url:
           
            parsed = urlparse(url)
            if not parsed.scheme in ['http', 'https'] or not parsed.netloc:
                logger.warning(f"Invalid URL provided: {url}")
                return []
            content = process_url(url)
        
        if not content or not isinstance(content, str) or not content.strip():
            logger.warning("No valid content provided for quiz generation.")
            return []
        
        num_questions = max(1, min(num_questions, 10))
        
        sentences = get_sentences(content)
        if len(sentences) < 3:
            logger.warning("Not enough sentences to generate quiz.")
            return []
        
        keywords = extract_keywords(content)
        
        valid_sentences = [s for s in sentences if len(s.split()) >= 3]  # Lowered threshold
        if len(valid_sentences) < num_questions:
            valid_sentences = valid_sentences * (num_questions // len(valid_sentences) + 1)
        
        selected_sentences = random.sample(valid_sentences, num_questions)
        
        quiz = []
        for sentence in selected_sentences:
            question = create_fill_in_blank_question(sentence, keywords)
            if question:
                quiz.append(question)
        
        while len(quiz) < num_questions and len(valid_sentences) > len(quiz):
            remaining = [s for s in valid_sentences if s not in selected_sentences]
            if not remaining:
                break
                
            new_sentence = random.choice(remaining)
            selected_sentences.append(new_sentence)
            
            question = create_fill_in_blank_question(new_sentence, keywords)
            if question:
                quiz.append(question)
        
        if not quiz:
            logger.warning("Failed to generate any quiz questions.")
        
        return quiz
    except Exception as e:
        logger.error(f"Error generating quiz: {str(e)}", exc_info=True)
        return []