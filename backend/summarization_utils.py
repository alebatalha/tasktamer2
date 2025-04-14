from typing import List
import re
import logging
import nltk
from nltk.tokenize import sent_tokenize


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


nltk.data.find('tokenizers/punkt')

def get_sentences(text: str) -> List[str]:
    try:
        if not text or not isinstance(text, str):
            logger.warning("Invalid or empty text input provided.")
            return []
        
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()
        
        sentences = sent_tokenize(text)
        sentences = [s for s in sentences if len(s.split()) > 3]
        
        return sentences
    except Exception as e:
        logger.error(f"Error getting sentences: {str(e)}", exc_info=True)
        return []

def extract_keywords(text: str, top_n: int = 20) -> List[str]:
    try:
        from nltk.corpus import stopwords
        from nltk.probability import FreqDist
        from nltk.tokenize import word_tokenize
        
        nltk.data.find('corpora/stopwords')
        
        stop_words = set(stopwords.words('english'))
        words = word_tokenize(text.lower())
        
        words = [word for word in words if word.isalnum() and 
                 word not in stop_words and len(word) > 3]
        
        fdist = FreqDist(words)
        
        return [word for word, _ in fdist.most_common(top_n)]
    
    except (ImportError, LookupError) as e:
        logger.warning(f"NLTK keyword extraction failed: {str(e)}. Using regex fallback.")
        
        words = re.findall(r'\b[a-zA-Z][a-zA-Z-]{3,}\b', text.lower())
        
        basic_stopwords = {'the', 'and', 'for', 'this', 'that', 'with', 'from', 
                          'have', 'they', 'will', 'would', 'could', 'should', 
                          'there', 'their', 'what', 'when', 'where', 'which', 
                          'these', 'those', 'been', 'were', 'more', 'much', 
                          'some', 'such', 'your', 'very'}
        
        words = [word for word in words if word not in basic_stopwords]
        
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
        
        sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
        
        return [word for word, _ in sorted_words[:top_n]]
    except Exception as e:
        logger.error(f"Error extracting keywords: {str(e)}", exc_info=True)
        return []