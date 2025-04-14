from typing import List, Dict, Any, Union
import nltk
from nltk.tokenize import sent_tokenize
from utils.fallback_detector import USING_FALLBACK, USING_NLTK_FALLBACK


try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)
    
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)

class TaskTamer:
    
    
    def __init__(self):
        
        self.documents = []
        
        
        if not USING_FALLBACK:
            try:
                from haystack.document_stores import InMemoryDocumentStore
                from haystack.nodes import PreProcessor
                
                self.document_store = InMemoryDocumentStore()
                self.preprocessor = PreProcessor(
                    clean_empty_lines=True,
                    clean_whitespace=True,
                    split_by='word',
                    split_length=200,
                    split_overlap=50,
                    split_respect_sentence_boundary=True
                )
                self.using_haystack = True
            except ImportError:
                self.using_haystack = False
        else:
            self.using_haystack = False
    
    def process_text(self, text: str) -> List[Dict[str, Any]]:
        
        if not text:
            return []
            
        if self.using_haystack:
           
            processed_docs = self.preprocessor.process([{"content": text}])
            self.document_store.write_documents(processed_docs)
            return processed_docs
        else:
            
            paragraphs = text.split('\n\n')
            processed_docs = []
            
            for i, para in enumerate(paragraphs):
                if para.strip():
                    processed_docs.append({
                        "content": para.strip(),
                        "id": f"doc_{i}"
                    })
                    
            self.documents.extend(processed_docs)
            return processed_docs
    
    def get_documents(self) -> List[Dict[str, Any]]:
     
        if self.using_haystack:
            return self.document_store.get_all_documents()
        else:
            return self.documents
    
    def clear_documents(self) -> None:
       
        if self.using_haystack:
            self.document_store.delete_documents()
        else:
            self.documents = []
    
    def get_sentences(self, text: str) -> List[str]:
        """Break text into sentences using NLP techniques."""
        return sent_tokenize(text)


tamer = TaskTamer()