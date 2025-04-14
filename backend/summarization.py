from typing import List, Dict, Any, Optional, Tuple, Union
import requests
import re
import numpy as np
import logging
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from tenacity import retry, stop_after_attempt, wait_exponential
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer
from string import punctuation
from collections import Counter
from utils.content_fetcher import fetch_webpage_content

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
    
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

class TextRankSummarizer:
    def __init__(self, language='english'):
        self.language = language
        self.stop_words = set(stopwords.words(language))
        self.stemmer = PorterStemmer()
        
    def preprocess_text(self, text: str) -> List[str]:
        try:
            sentences = sent_tokenize(text)
            return sentences
        except Exception as e:
            logger.error(f"Error preprocessing text: {str(e)}", exc_info=True)
            return []
    
    def create_similarity_matrix(self, sentences: List[str]) -> np.ndarray:
        n = len(sentences)
        similarity_matrix = np.zeros((n, n))
        
        for i in range(n):
            for j in range(n):
                if i != j:
                    similarity_matrix[i][j] = self._sentence_similarity(sentences[i], sentences[j])
        
        return similarity_matrix
    
    def _sentence_similarity(self, sent1: str, sent2: str) -> float:
        words1 = self._clean_and_tokenize(sent1)
        words2 = self._clean_and_tokenize(sent2)
        
        all_words = list(set(words1 + words2))
        vector1 = [0] * len(all_words)
        vector2 = [0] * len(all_words)
        
        for word in words1:
            vector1[all_words.index(word)] += 1
        
        for word in words2:
            vector2[all_words.index(word)] += 1
        
        return self._cosine_similarity(vector1, vector2)
    
    def _clean_and_tokenize(self, sentence: str) -> List[str]:
        words = re.sub(r'[^\w\s]', '', sentence.lower()).split()
        words = [self.stemmer.stem(word) for word in words if word not in self.stop_words]
        return words
    
    def _cosine_similarity(self, vector1: List[int], vector2: List[int]) -> float:
        dot_product = sum(a * b for a, b in zip(vector1, vector2))
        magnitude1 = sum(a * a for a in vector1) ** 0.5
        magnitude2 = sum(b * b for b in vector2) ** 0.5
        
        if magnitude1 * magnitude2 == 0:
            return 0
        
        return dot_product / (magnitude1 * magnitude2)
    
    def power_method(self, similarity_matrix: np.ndarray, epsilon: float = 1e-4, max_iter: int = 100) -> np.ndarray:
        n = len(similarity_matrix)
        p = np.ones(n) / n
        
        for _ in range(max_iter):
            prev_p = p.copy()
            p = np.dot(similarity_matrix.T, p)
            p /= p.sum() if p.sum() > 0 else 1
            
            if np.abs(p - prev_p).sum() < epsilon:
                break
        
        return p
    
    def summarize(self, text: str, ratio: float = 0.3, min_sentences: int = 3, max_sentences: int = 7) -> str:
        try:
            original_sentences = self.preprocess_text(text)
            
            if len(original_sentences) <= min_sentences:
                return text
            
            similarity_matrix = self.create_similarity_matrix(original_sentences)
            scores = self.power_method(similarity_matrix)
            
            ranked_sentences = [(score, i, sentence) for i, (sentence, score) in 
                            enumerate(zip(original_sentences, scores))]
            ranked_sentences.sort(reverse=True)
            
            num_sentences = min(max(min_sentences, int(len(original_sentences) * ratio)), max_sentences, len(original_sentences))
            
            selected_indices = [idx for _, idx, _ in ranked_sentences[:num_sentences]]
            selected_indices.sort()
            
            summary = [original_sentences[i] for i in selected_indices]
            return ' '.join(summary)
        except Exception as e:
            logger.error(f"Error summarizing text: {str(e)}", exc_info=True)
            return ""

class KeyphraseExtractor:
    def __init__(self, language='english'):
        self.language = language
        self.stop_words = set(stopwords.words(language))
    
    def extract_keyphrases(self, text: str, top_n: int = 5) -> List[str]:
        try:
            words = re.findall(r'\b[a-zA-Z][a-zA-Z-]+[a-zA-Z]\b', text.lower())
            filtered_words = [word for word in words if word not in self.stop_words and len(word) > 3]
            
            word_freq = Counter(filtered_words)
            
            phrases = []
            text_lower = text.lower()
            for sentence in sent_tokenize(text):
                sentence_lower = sentence.lower()
                for word in word_freq:
                    if word in sentence_lower:
                        start_idx = sentence_lower.find(word)
                        if start_idx != -1:
                            window_start = max(0, start_idx - 20)
                            window_end = min(len(sentence_lower), start_idx + len(word) + 20)
                            context = sentence_lower[window_start:window_end]
                            phrases.append((word, word_freq[word], context))
            
            phrases.sort(key=lambda x: x[1], reverse=True)
            return [phrase[0] for phrase in phrases[:top_n]]
        except Exception as e:
            logger.error(f"Error extracting keyphrases: {str(e)}", exc_info=True)
            return []

class AcademicFocusSummarizer:
    def __init__(self):
        self.text_rank = TextRankSummarizer()
        self.keyphrase_extractor = KeyphraseExtractor()
    
    def identify_document_structure(self, text: str) -> Dict[str, Any]:
        try:
            paragraphs = re.split(r'\n\s*\n', text)
            paragraphs = [p.strip() for p in paragraphs if p.strip()]
            
            structure = {
                "introduction": [],
                "body": [],
                "conclusion": []
            }
            
            if len(paragraphs) <= 2:
                return {"introduction": paragraphs, "body": [], "conclusion": []}
            
            intro_limit = min(2, max(1, int(len(paragraphs) * 0.2)))
            conclusion_limit = min(2, max(1, int(len(paragraphs) * 0.2)))
            
            structure["introduction"] = paragraphs[:intro_limit]
            structure["conclusion"] = paragraphs[-conclusion_limit:]
            structure["body"] = paragraphs[intro_limit:-conclusion_limit] if intro_limit < len(paragraphs) - conclusion_limit else []
            
            return structure
        except Exception as e:
            logger.error(f"Error identifying document structure: {str(e)}", exc_info=True)
            return {"introduction": [], "body": [], "conclusion": []}
    
    def generate_focused_summary(self, text: str, focus_area: str = None) -> Dict[str, Any]:
        try:
            structure = self.identify_document_structure(text)
            keyphrases = self.keyphrase_extractor.extract_keyphrases(text)
            
            if not focus_area or focus_area.lower() not in ["introduction", "body", "conclusion"]:
                full_text = ' '.join([' '.join(structure[section]) for section in structure])
                main_summary = self.text_rank.summarize(full_text)
                
                result = {
                    "main_summary": main_summary,
                    "key_points": keyphrases,
                    "structure": {},
                }
                
                for section, paragraphs in structure.items():
                    if paragraphs:
                        section_text = ' '.join(paragraphs)
                        section_summary = self.text_rank.summarize(section_text, ratio=0.5, min_sentences=1)
                        result["structure"][section] = section_summary
                
                return result
            else:
                section = focus_area.lower()
                if structure[section]:
                    section_text = ' '.join(structure[section])
                    section_summary = self.text_rank.summarize(section_text, ratio=0.7, min_sentences=2)
                    return {
                        "main_summary": section_summary,
                        "key_points": self.keyphrase_extractor.extract_keyphrases(section_text),
                        "structure": {section: section_summary}
                    }
                else:
                    return {"main_summary": "", "key_points": [], "structure": {}}
        except Exception as e:
            logger.error(f"Error generating focused summary: {str(e)}", exc_info=True)
            return {"main_summary": "", "key_points": [], "structure": {}}

def extract_main_content(text: str) -> str:
    try:
        paragraphs = re.split(r'\n\s*\n', text)
        paragraphs = [p.strip() for p in paragraphs if p.strip()]
        
        if not paragraphs:
            return text
        
        paragraph_lengths = [len(p) for p in paragraphs]
        avg_length = sum(paragraph_lengths) / len(paragraph_lengths)
        
        main_content_paragraphs = [p for p in paragraphs if len(p) >= avg_length * 0.7]
        
        if not main_content_paragraphs:
            return text
        
        return '\n\n'.join(main_content_paragraphs)
    except Exception as e:
        logger.error(f"Error extracting main content: {str(e)}", exc_info=True)
        return text

def get_summary_format(summary_data: Dict[str, Any], format_type: str = "concise") -> str:
    try:
        if format_type == "detailed":
            formatted_summary = summary_data["main_summary"] + "\n\n"
            
            if summary_data["key_points"]:
                formatted_summary += "Key Points:\n" + "\n".join([f"• {point}" for point in summary_data["key_points"]]) + "\n\n"
                
            for section, summary in summary_data["structure"].items():
                if summary:
                    formatted_summary += f"{section.capitalize()}:\n{summary}\n\n"
            
            return formatted_summary.strip()
        
        elif format_type == "bullet":
            formatted_summary = "Summary:\n" + "\n".join([f"• {sentence.strip()}" for sentence in summary_data["main_summary"].split('. ') if sentence.strip()]) + "\n\n"
            
            if summary_data["key_points"]:
                formatted_summary += "Key Points:\n" + "\n".join([f"• {point}" for point in summary_data["key_points"]])
            
            return formatted_summary.strip()
        
        else:
            return summary_data["main_summary"]
    except Exception as e:
        logger.error(f"Error formatting summary: {str(e)}", exc_info=True)
        return summary_data["main_summary"]

def summarize_content(content: Optional[str] = None, url: Optional[str] = None, format_type: str = "concise", focus_area: str = None) -> str:
    try:
        if url:
            content = fetch_webpage_content(url)
        
        if not content or not isinstance(content, str):
            logger.warning("No valid content provided for summarization.")
            return "No content provided for summarization."
        
        main_content = extract_main_content(content)
        
        summarizer = AcademicFocusSummarizer()
        summary_data = summarizer.generate_focused_summary(main_content, focus_area)
        
        if not summary_data["main_summary"]:
            logger.info("Falling back to TextRank summarization.")
            fallback_summarizer = TextRankSummarizer()
            summary_data["main_summary"] = fallback_summarizer.summarize(main_content)
        
        return get_summary_format(summary_data, format_type)
    except Exception as e:
        logger.error(f"Error in summarize_content: {str(e)}", exc_info=True)
        return f"Error summarizing content: {str(e)}"

def extract_study_material(content: str) -> Dict[str, Any]:
    try:
        summarizer = AcademicFocusSummarizer()
        structure = summarizer.identify_document_structure(content)
        keyphrases = summarizer.keyphrase_extractor.extract_keyphrases(content, top_n=10)
        
        sentences = sent_tokenize(content)
        sentence_scores = []
        
        for sentence in sentences:
            score = 0
            for phrase in keyphrases:
                if phrase.lower() in sentence.lower():
                    score += 1
            sentence_scores.append((sentence, score))
        
        important_sentences = [s for s, score in sorted(sentence_scores, key=lambda x: x[1], reverse=True)[:10]]
        
        return {
            "key_concepts": keyphrases,
            "important_points": important_sentences,
            "structure": structure
        }
    except Exception as e:
        logger.error(f"Error extracting study material: {str(e)}", exc_info=True)
        return {"key_concepts": [], "important_points": [], "structure": {}}

def generate_study_notes(content: str) -> str:
    try:
        material = extract_study_material(content)
        
        study_notes = "# Study Notes\n\n"
        
        study_notes += "## Key Concepts\n"
        for concept in material["key_concepts"]:
            study_notes += f"- {concept}\n"
        
        study_notes += "\n## Important Points\n"
        for point in material["important_points"]:
            study_notes += f"- {point}\n"
        
        study_notes += "\n## Document Structure\n"
        
        for section, paragraphs in material["structure"].items():
            if paragraphs:
                study_notes += f"### {section.capitalize()}\n"
                section_text = ' '.join(paragraphs)
                summarizer = TextRankSummarizer()
                section_summary = summarizer.summarize(section_text, ratio=0.3, min_sentences=1)
                study_notes += f"{section_summary}\n\n"
        
        return study_notes
    except Exception as e:
        logger.error(f"Error generating study notes: {str(e)}", exc_info=True)
        return "Error generating study notes."