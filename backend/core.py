from typing import List, Dict, Any, Union
import nltk
import logging
from nltk.tokenize import sent_tokenize
from utils.fallback_detector import USING_FALLBACK, USING_NLTK_FALLBACK


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


nltk.data.find('tokenizers/punkt')
nltk.data.find('corpora/stopwords')

class TaskTamer:
    def __init__(self):
        self.documents = []
        self.using_haystack = False
        
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
                logger.info("Initialized TaskTamer with Haystack support.")
            except ImportError as e:
                logger.warning(f"Haystack import failed: {str(e)}. Using basic text processing fallback.")
                self.using_haystack = False
        else:
            logger.info("Haystack disabled by USING_FALLBACK. Using basic text processing.")
            self.using_haystack = False
    
    def process_text(self, text: str) -> List[Dict[str, Any]]:
        try:
            if not text or not isinstance(text, str):
                logger.warning("Invalid or empty text input provided.")
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
        except Exception as e:
            logger.error(f"Error processing text: {str(e)}", exc_info=True)
            return []
    
    def get_documents(self) -> List[Dict[str, Any]]:
        if self.using_haystack:
            return self.document_store.get_all_documents()
        return self.documents
    
    def clear_documents(self) -> None:
        if self.using_haystack:
            self.document_store.delete_documents()
        else:
            self.documents = []
    
    def get_sentences(self, text: str) -> List[str]:
        
        try:
            return sent_tokenize(text)
        except Exception as e:
            logger.error(f"Error tokenizing sentences: {str(e)}", exc_info=True)
            return []

tamer = TaskTamer()