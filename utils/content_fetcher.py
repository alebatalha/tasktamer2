import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse
from typing import Union
from utils.fallback_detector import USING_YOUTUBE_API


def fetch_webpage_content(url: str) -> str:

    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
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
            
            # Clean up whitespace
            text = re.sub(r'\s+', ' ', text)
            return text
        
        return "No readable content found."
    except Exception as e:
        return f"Error fetching webpage: {str(e)}"


def extract_youtube_id(url: str) -> Union[str, None]:

    youtube_regex = r'(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})'
    match = re.search(youtube_regex, url)
    return match.group(1) if match else None


def get_youtube_content(youtube_url: str) -> str:
  
    video_id = extract_youtube_id(youtube_url)
    if not video_id:
        return "Invalid YouTube URL"
    
    
    if USING_YOUTUBE_API:
        try:
            from youtube_transcript_api import YouTubeTranscriptApi
            
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
            transcript = transcript_list.find_transcript(['en'])
            
            captions = transcript.fetch()
            text = " ".join([item['text'] for item in captions])
            return text
        except Exception as e:
            return f"Error retrieving YouTube captions: {str(e)}"
    else:
        return "YouTube transcript functionality requires youtube_transcript_api. Please install it using pip."


def process_url(url: str) -> str:
   
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.lower()
    
    if 'youtube.com' in domain or 'youtu.be' in domain:
        return get_youtube_content(url)
    else:
        return fetch_webpage_content(url)