from typing import List
import re
import nltk
from nltk.tokenize import sent_tokenize


try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

def get_sentences(text: str) -> List[str]:

    if not text:
        return []
    

    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    

    sentences = sent_tokenize(text)
  
    sentences = [s for s in sentences if len(s.split()) > 3]
    
    return sentences

def extract_keywords(text: str, top_n: int = 20) -> List[str]:

    try:
        from nltk.corpus import stopwords
        from nltk.probability import FreqDist
        from nltk.tokenize import word_tokenize
        
       
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords', quiet=True)
        
    
        stop_words = set(stopwords.words('english'))
        words = word_tokenize(text.lower())
        
     
        words = [word for word in words if word.isalnum() and 
                 word not in stop_words and len(word) > 3]
        
  
        fdist = FreqDist(words)
        
      
        return [word for word, _ in fdist.most_common(top_n)]
    
    except (ImportError, LookupError):
       
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