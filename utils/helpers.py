import base64
import re
import json
import os
import streamlit as st
from typing import List, Dict, Any, Union


def is_valid_url(url: str) -> bool:
    
    url_pattern = re.compile(
        r'^(https?:\/\/)?' 
        r'(www\.)?' 
        r'([a-zA-Z0-9-]+\.)+'
        r'[a-zA-Z]{2,}'
        r'(\/[a-zA-Z0-9-._~:/?#[\]@!$&\'()*+,;=]*)?' 
        r'$'
    )
    return bool(url_pattern.match(url))

def extract_youtube_id(url: str) -> Union[str, None]:
   
    youtube_regex = r'(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})'
    match = re.search(youtube_regex, url)
    return match.group(1) if match else None

def save_to_json(data: Any, filename: str) -> bool:
    
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception:
        return False

def load_from_json(filename: str) -> Union[Dict, List, None]:
    
    if not os.path.exists(filename):
        return None
        
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except Exception:
        return None

def clean_text(text: str) -> str:
    
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text

def truncate_text(text: str, max_length: int = 100) -> str:
    
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."

def format_file_size(size_bytes: int) -> str:
   
    if size_bytes < 1024:
        return f"{size_bytes} bytes"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.1f} MB"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.1f} GB"

def ensure_directories(*dirs):
    
    for directory in dirs:
        os.makedirs(directory, exist_ok=True)
    return True

def handle_file_upload(uploaded_file):
    
    if uploaded_file is None:
        return None
        
    try:
        content = uploaded_file.getvalue().decode("utf-8")
        return content
    except UnicodeDecodeError:
        # For binary files
        return uploaded_file.getvalue()

def clear_session_state(*keys):
    
    for key in keys:
        if key in st.session_state:
            del st.session_state[key]

def get_file_extension(filename: str) -> str:
   
    return os.path.splitext(filename)[1].lower()

def is_text_file(filename: str) -> bool:
    
    text_extensions = ['.txt', '.md', '.csv', '.json', '.py', '.html', '.css', '.js']
    ext = get_file_extension(filename)
    return ext in text_extensions

def is_pdf_file(filename: str) -> bool:
   
    return get_file_extension(filename) == '.pdf'

def is_document_file(filename: str) -> bool:
    
    doc_extensions = ['.doc', '.docx', '.odt', '.rtf']
    ext = get_file_extension(filename)
    return ext in doc_extensions

def create_download_link(content: str, filename: str, text: str = "Download"):
    
    b64 = base64.b64encode(content.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="{filename}">{text}</a>'
    return href