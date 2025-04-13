import re
import requests
from bs4 import BeautifulSoup
from typing import Optional, List

def fetch_webpage_content(url: str) -> str:
    """
    Fetch and extract content from a web page.
    
    Args:
        url: The webpage URL to fetch content from
        
    Returns:
        The extracted text content
    """
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
       
        for tag in soup(['script', 'style', 'header', 'footer', 'nav', 'aside', 'meta', 'iframe']):
            tag.decompose()
            
        
        paragraphs = soup.find_all("p")
        text = "\n".join([p.get_text().strip() for p in paragraphs if p.get_text().strip()])
        
        
        if not text:
            main_content = soup.find('main') or soup.find('article') or soup.find('body')
            if main_content:
                text = main_content.get_text(separator="\n", strip=True)
            
        return text if text else "No readable content found."
    except Exception as e:
        return f"Error fetching webpage: {str(e)}"

def get_sentences(text: str) -> List[str]:
    """
    Extract sentences from text content.
    
    Args:
        text: The text to extract sentences from
        
    Returns:
        List of sentences
    """
   
    text = re.sub(r'\.(?=[A-Z])', '. ', text)  
    text = re.sub(r'\s+', ' ', text)  
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if s.strip()]

def get_key_sentences(sentences: List[str], num_sentences: int = 5) -> List[str]:
    """
    Extract the most important sentences from content.
    
    Args:
        sentences: List of sentences to analyze
        num_sentences: Number of sentences to extract
        
    Returns:
        List of key sentences
    """
    if len(sentences) <= num_sentences:
        return sentences
    
   
    key_sentences = [sentences[0]]  
    
    
    middle_count = num_sentences - 2  
    if middle_count > 0:
        step = max(1, (len(sentences) - 2) // middle_count)
        for i in range(1, len(sentences) - 1, step):
            if len(key_sentences) < num_sentences - 1:  # Leave room for last sentence
                key_sentences.append(sentences[i])
    
    key_sentences.append(sentences[-1])  
    
    return key_sentences

def summarize_content(content: Optional[str] = None, url: Optional[str] = None, length: str = "medium") -> str:
    """
    Generate a summary of the provided content or webpage.
    
    Args:
        content: Text content to summarize
        url: URL to fetch content from
        length: Summary length ('short', 'medium', or 'long')
        
    Returns:
        Summary of the content
    """
    
    if url:
        content = fetch_webpage_content(url)
    
    if not content:
        return "No content provided for summarization."
    
    
    sentences = get_sentences(content)
    
   
    if len(sentences) <= 3:
        return content
    
    
    if length == "short":
        num_sentences = min(3, len(sentences))
    elif length == "long":
        num_sentences = min(max(5, len(sentences) // 4), 10)
    else:  
        num_sentences = min(max(3, len(sentences) // 5), 5)
    
    
    summary_sentences = get_key_sentences(sentences, num_sentences)
    
    
    summary = " ".join(summary_sentences)
    
    return summary