import re
import random
from typing import List, Dict, Any, Optional
from backend.summarization import fetch_webpage_content, get_sentences

def extract_keywords(text: str) -> List[str]:
    """
    Extract potential keywords from text.
    
    Args:
        text: The text to extract keywords from
        
    Returns:
        List of potential keywords
    """
    
    words = re.findall(r'\b[A-Za-z][A-Za-z-]+\b', text)
    
    
    stopwords = {'the', 'a', 'an', 'and', 'or', 'but', 'if', 'then', 'else', 'when', 
                'at', 'from', 'by', 'for', 'with', 'about', 'against', 'between',
                'into', 'through', 'during', 'before', 'after', 'above', 'below',
                'to', 'of', 'in', 'on', 'as', 'is', 'are', 'was', 'were', 'be', 'been',
                'has', 'have', 'had', 'do', 'does', 'did', 'can', 'could', 'will',
                'would', 'should', 'might', 'that', 'this', 'these', 'those', 'it',
                'they', 'them', 'their', 'he', 'she', 'his', 'her', 'we', 'us', 'our',
                'you', 'your', 'i', 'me', 'my'}
    
    keywords = [word for word in words if word.lower() not in stopwords and len(word) > 3]
    
    return keywords

def get_distractors(keywords: List[str], correct_answer: str) -> List[str]:
    """
    Generate distractor options for quiz questions.
    
    Args:
        keywords: List of potential keywords to use as distractors
        correct_answer: The correct answer
        
    Returns:
        List of distractor options
    """
   
    filtered_keywords = [w for w in keywords if w != correct_answer and w.lower() != correct_answer.lower()]
    
   
    if len(filtered_keywords) < 3:
        return ["Option A", "Option B", "Option C"]
    
    
    distractors = random.sample(filtered_keywords, min(3, len(filtered_keywords)))
    
    return distractors

def create_fill_in_blank_question(sentence: str, keywords: List[str]) -> Dict[str, Any]:
    """
    Create a fill-in-the-blank question from a sentence.
    
    Args:
        sentence: The sentence to create a question from
        keywords: List of potential keywords to use
        
    Returns:
        A question dict with question, options, and answer
    """
    words = sentence.split()
    if len(words) < 5:
        return {}
        
    
    potential_blanks = []
    for i in range(2, len(words) - 2):
        word = words[i]
        
        if len(word) > 3 and word.lower() not in {'with', 'that', 'this', 'from', 'their', 'about'}:
            
            cleaned_word = re.sub(r'[^\w\s]', '', word)
            if cleaned_word:
                potential_blanks.append((i, cleaned_word))
    
    if not potential_blanks:
        return {}
    
   
    blank_pos, correct_answer = random.choice(potential_blanks)
    
    
    question_words = words.copy()
    question_words[blank_pos] = "_____"
    question = " ".join(question_words)
    
    
    distractors = get_distractors(keywords, correct_answer)
    
    
    options = [correct_answer] + distractors
    random.shuffle(options)
    
    return {
        "question": f"Fill in the blank: {question}",
        "options": options,
        "answer": correct_answer
    }

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
   
    if url:
        content = fetch_webpage_content(url)
        
    if not content:
        return []
    
   
    num_questions = max(1, min(num_questions, 10))
    
    
    sentences = get_sentences(content)
    if len(sentences) < 3:
        return []
    
    
    keywords = extract_keywords(content)
    
   
    valid_sentences = [s for s in sentences if len(s.split()) >= 5]
    if len(valid_sentences) < num_questions:
       
        valid_sentences = valid_sentences * (num_questions // len(valid_sentences) + 1)
    
    selected_sentences = random.sample(valid_sentences, num_questions)
    
   
    quiz = []
    for sentence in selected_sentences:
        question = create_fill_in_blank_question(sentence, keywords)
        if question:
            quiz.append(question)
    
    
    while len(quiz) < num_questions and len(valid_sentences) > len(quiz):
        remaining = [s for s in valid_sentences if s not in selected_sentences]
        if not remaining:
            break
            
        new_sentence = random.choice(remaining)
        selected_sentences.append(new_sentence)
        
        question = create_fill_in_blank_question(new_sentence, keywords)
        if question:
            quiz.append(question)
    
    return quiz