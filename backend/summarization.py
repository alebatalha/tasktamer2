import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse

def fetch_webpage_content(url: str) -> str:
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        for tag in soup(['script', 'style', 'header', 'footer', 'nav']):
            tag.decompose()
            
        paragraphs = soup.find_all("p")
        text = "\n".join([p.get_text().strip() for p in paragraphs if p.get_text().strip()])
        
        if not text:
            main_content = soup.find('main') or soup.find('article') or soup.find('body')
            if main_content:
                text = main_content.get_text(separator="\n", strip=True)
            
        return text if text else "No readable content found."
    except requests.RequestException as e:
        return f"Error fetching webpage: {e}"

def extract_youtube_id(url: str) -> str:
    youtube_regex = r'(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})'
    match = re.search(youtube_regex, url)
    return match.group(1) if match else None

def process_url(url: str) -> str:
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.lower()
    
    if 'youtube.com' in domain or 'youtu.be' in domain:
        return "YouTube video detected. For full functionality with captions, please install additional dependencies."
    else:
        return fetch_webpage_content(url)

def summarize_content(content: str = None, url: str = None) -> str:
    if url:
        content = process_url(url)
    
    if not content or content.startswith("Error"):
        return "No content provided for summarization."
    
    sentences = re.split(r'(?<=[.!?])\s+', content)
    
    if len(sentences) <= 5:
        return content
    
    important_sentences = []
    
    # Add first sentence (usually contains main topic)
    if sentences:
        important_sentences.append(sentences[0])
    
    # Add a sentence from first third
    first_third_idx = len(sentences) // 3
    if first_third_idx > 0 and first_third_idx < len(sentences):
        important_sentences.append(sentences[first_third_idx])
    
    # Add a sentence from the middle
    middle_idx = len(sentences) // 2
    if middle_idx > 0 and middle_idx < len(sentences) and middle_idx != first_third_idx:
        important_sentences.append(sentences[middle_idx])
    
    # Add a sentence from the last third
    last_third_idx = (len(sentences) * 2) // 3
    if last_third_idx > 0 and last_third_idx < len(sentences) and last_third_idx != middle_idx:
        important_sentences.append(sentences[last_third_idx])
    
    # Add last sentence (usually contains conclusion)
    if len(sentences) > 1:
        important_sentences.append(sentences[-1])
    
    # Deduplicate sentences
    important_sentences = list(dict.fromkeys(important_sentences))
    
    return " ".join(important_sentences)