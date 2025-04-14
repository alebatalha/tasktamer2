import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse
from typing import Union
import logging
from tenacity import retry, stop_after_attempt, wait_exponential
from utils.fallback_detector import USING_YOUTUBE_API

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def fetch_webpage_content(url: str) -> str:
    
    try:
        if not url or not isinstance(url, str):
            logger.warning("Invalid URL provided for fetching.")
            return "Error: Invalid URL."

        parsed = urlparse(url)
        if not parsed.scheme in ['http', 'https'] or not parsed.netloc:
            logger.warning(f"Invalid URL scheme or domain: {url}")
            return "Error: Invalid URL format."

        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
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
            return text if text else "Error: No readable content found."
        
        logger.warning(f"No main content found for URL: {url}")
        return "Error: No readable content found."
    except requests.RequestException as e:
        logger.error(f"Error fetching webpage {url}: {str(e)}", exc_info=True)
        return f"Error fetching webpage: {str(e)}"

def extract_youtube_id(url: str) -> Union[str, None]:
    
    try:
        youtube_regex = r'(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})'
        match = re.search(youtube_regex, url)
        return match.group(1) if match else None
    except Exception as e:
        logger.error(f"Error extracting YouTube ID from {url}: {str(e)}")
        return None

def get_youtube_content(youtube_url: str) -> str:
    
    try:
        video_id = extract_youtube_id(youtube_url)
        if not video_id:
            logger.warning(f"Invalid YouTube URL: {youtube_url}")
            return "Error: Invalid YouTube URL."
        
        if USING_YOUTUBE_API:
            try:
                from youtube_transcript_api import YouTubeTranscriptApi
                
                transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
                transcript = transcript_list.find_transcript(['en'])
                
                captions = transcript.fetch()
                text = " ".join([item['text'] for item in captions])
                text = re.sub(r'\s+', ' ', text.strip())
                return text if text else "Error: No transcript available."
            except ImportError:
                logger.warning("youtube_transcript_api not installed.")
                return "Error: YouTube transcript functionality requires youtube_transcript_api."
            except Exception as e:
                logger.error(f"Error retrieving YouTube captions for {youtube_url}: {str(e)}")
                return f"Error retrieving YouTube captions: {str(e)}"
        else:
            logger.warning("YouTube API disabled.")
            return "Error: YouTube transcript functionality requires youtube_transcript_api."
    except Exception as e:
        logger.error(f"Error in get_youtube_content for {youtube_url}: {str(e)}")
        return f"Error: {str(e)}"

def process_url(url: str) -> str:
   
    try:
        if not url or not isinstance(url, str):
            logger.warning("Invalid URL provided for processing.")
            return "Error: Invalid URL."

        parsed_url = urlparse(url)
        domain = parsed_url.netloc.lower()
        
        if 'youtube.com' in domain or 'youtu.be' in domain:
            return get_youtube_content(url)
        return fetch_webpage_content(url)
    except Exception as e:
        logger.error(f"Error processing URL {url}: {str(e)}")
        return f"Error: {str(e)}"