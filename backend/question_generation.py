import re
import random
from typing import List, Dict, Any
from backend.summarization import process_url

def generate_quiz(content: str = None, url: str = None, num_questions: int = 3) -> List[Dict[str, Any]]:
    if url:
        content = process_url(url)
        
    if not content or num_questions <= 0:
        return []
    
    # Split content into sentences
    sentences = re.split(r'(?<=[.!?])\s+', content)
    sentences = [s for s in sentences if len(s.split()) >= 6]  # Filter short sentences
    
    if len(sentences) < num_questions:
        return []
    
    # Choose random sentences for questions
    selected_sentences = random.sample(sentences, min(num_questions * 2, len(sentences)))
    
    quiz = []
    for i, sentence in enumerate(selected_sentences[:num_questions]):
        question_data = create_question_from_sentence(sentence, i)
        if question_data:
            quiz.append(question_data)
    
    return quiz

def create_question_from_sentence(sentence: str, index: int) -> Dict[str, Any]:
    words = sentence.split()
    if len(words) < 6:
        return None
    
    # Identify potential keywords to blank out
    nouns_and_verbs = []
    for i, word in enumerate(words):
        if len(word) > 3 and word.isalpha() and i > 0 and i < len(words) - 1:
            nouns_and_verbs.append((i, word))
    
    if not nouns_and_verbs:
        return None
    
    # Select a random word to blank out
    word_index, correct_word = random.choice(nouns_and_verbs)
    
    # Create incorrect options
    incorrect_options = generate_incorrect_options(correct_word)
    
    # Create the question
    question_text = " ".join(words[:word_index] + ["_____"] + words[word_index+1:])
    
    # Create options and shuffle them
    options = [correct_word] + incorrect_options[:3]
    random.shuffle(options)
    
    return {
        "question": f"Fill in the blank: {question_text}",
        "options": options,
        "answer": correct_word
    }

def generate_incorrect_options(correct_word: str) -> List[str]:
    # Generate incorrect options that are different from the correct word
    if len(correct_word) <= 3:
        base_options = ["Small", "Large", "Quick", "Slow", "Good", "Nice", "Bad", "Old", "New"]
    else:
        # For longer words, create variations or use common alternatives
        base_options = [
            "Important", "Different", "Available", "Necessary", "Possible", "Significant",
            "Required", "Optional", "Essential", "Complete", "Effective", "Standard",
            "Alternative", "Additional", "Specific", "Relevant", "Primary", "Secondary"
        ]
    
    # Filter out options that match the correct word
    incorrect_options = [opt for opt in base_options if opt.lower() != correct_word.lower()]
    
    # Ensure we have at least 3 options
    while len(incorrect_options) < 3:
        incorrect_options.append(f"Option {len(incorrect_options) + 1}")
    
    return incorrect_options