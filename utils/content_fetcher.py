import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse
import logging
from tenacity import retry, stop_after_attempt, wait_exponential

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def fetch_webpage_content(url: str) -> str:
    try:
        if not url or not isinstance(url, str):
            return "Error: Invalid URL."

        parsed = urlparse(url)
        if not parsed.scheme in ['http', 'https'] or not parsed.netloc:
            return "Error: Invalid URL format."

        response = requests.get(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}, 
            timeout=15
        )
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        for tag in soup(['script', 'style', 'header', 'footer', 'nav', 'aside', 'meta', 'iframe']):
            tag.decompose()
            
        main_content = soup.find('main') or soup.find('article') or soup.find('body')
        
        if main_content:
            paragraphs = main_content.find_all('p')
            if paragraphs:
                text = ' '.join([p.get_text().strip() for p in paragraphs if p.get_text().strip()])
            else:
                text = main_content.get_text(separator=' ', strip=True)
            
            text = re.sub(r'\s+', ' ', text.strip())
            
            if text:
                return text
            return "Error: No readable content found."
        
        return "Error: No readable content found."
    except requests.RequestException as e:
        return f"Error fetching webpage: {str(e)}"

def process_url(url: str) -> str:
    try:
        if not url or not isinstance(url, str):
            return "Error: Invalid URL."
        return fetch_webpage_content(url)
    except Exception as e:
        return f"Error: {str(e)}"