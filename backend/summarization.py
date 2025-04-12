import re
import requests
from bs4 import BeautifulSoup
from typing import Optional

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
        
        # Remove unwanted elements
        for tag in soup(['script', 'style', 'header', 'footer', 'nav']):
            tag.decompose()
            
        # Extract paragraphs
        paragraphs = soup.find_all("p")
        text = "\n".join([p.get_text().strip() for p in paragraphs if p.get_text().strip()])
        
        # If no paragraphs found, try to get content from main content areas
        if not text:
            main_content = soup.find('main') or soup.find('article') or soup.find('body')
            if main_content:
                text = main_content.get_text(separator="\n", strip=True)
            
        return text if text else "No readable content found."
    except Exception as e:
        return f"Error fetching webpage: {str(e)}"

def summarize_content(content: Optional[str] = None, url: Optional[str] = None) -> str:
    """
    Generate a summary of the provided content or webpage.
    
    Args:
        content: Text content to summarize
        url: URL to fetch content from
        
    Returns:
        Summary of the content
    """
    # If URL is provided, fetch the content
    if url:
        content = fetch_webpage_content(url)
    
    if not content:
        return "No content provided for summarization."
    
    # Extract sentences
    sentences = re.split(r'(?<=[.!?])\s+', content)
    
    # If content is already short, return it as is
    if len(sentences) <= 3:
        return content
    
    # Simple extractive summarization: first, middle, and last sentence
    summary = [
        sentences[0],
        sentences[len(sentences) // 2],
        sentences[-1]
    ]
    
    return " ".join(summary)
