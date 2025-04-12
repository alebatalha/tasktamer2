import re
from typing import List, Dict, Any, Optional
from backend.summarization import fetch_webpage_content

def generate_quiz(content: Optional[str] = None, url: Optional[str] = None, num_questions: int = 3) -> List[Dict[str, Any]]:
    """
    Generate a quiz from the provided content or webpage.
    
    Args:
        content: Text content to create quiz from
        url: URL to fetch content from
        num_questions: Number of questions to generate
        
    Returns:
        List of quiz questions with options and answers
    """
    # If URL is provided, fetch the content
    if url:
        content = fetch_webpage_content(url)
        
    if not content:
        return []
    
    # Validate number of questions
    num_questions = max(1, min(num_questions, 10))
    
    # Split content into sentences
    sentences = re.split(r'(?<=[.!?])\s+', content)
    
    # Select sentences to create questions from
    selected_sentences = []
    step = max(1, len(sentences) // (num_questions + 1))
    
    for i in range(0, min(len(sentences), num_questions * step), step):
        if i < len(sentences):
            selected_sentences.append(sentences[i])
    
    # Create quiz questions
    quiz = []
    
    for i, sentence in enumerate(selected_sentences[:num_questions]):
        # Create a fill-in-the-blank question
        words = sentence.split()
        if len(words) < 4:
            continue
            
        # Pick a word to remove (not first or last word)
        word_index = min(len(words) // 2, len(words) - 2)
        correct_word = words[word_index]
        
        # Create incorrect options
        incorrect_options = ["Option A", "Option B", "Option C"]
        
        # Create the question
        question = " ".join(words[:word_index] + ["_____"] + words[word_index+1:])
        
        quiz.append({
            "question": f"Fill in the blank: {question}",
            "options": [correct_word] + incorrect_options,
            "answer": correct_word
        })
    
    return quiz
