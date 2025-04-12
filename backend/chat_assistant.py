def ask_question(question: str) -> str:
    """
    Simple question answering function for TaskTamer.
    
    Args:
        question: The user's question
        
    Returns:
        Response to the question
    """
    if not question:
        return "Please ask a specific question."

    # Pre-defined responses for common questions
    responses = {
        "what": "TaskTamer helps you break down complex tasks, summarize content, and generate quizzes to test your knowledge.",
        "how": "You can use TaskTamer by selecting a feature from the sidebar and following the instructions. Try entering a task to break down, text to summarize, or content to create a quiz from.",
        "who": "TaskTamer was created by Alessandra Batalha as part of her final year project at Dublin Business School.",
        "when": "You can use TaskTamer anytime you need help organizing tasks, understanding content, or testing your knowledge.",
        "where": "TaskTamer runs in your browser and doesn't require any installation. It's accessible from any device with internet access.",
        "why": "TaskTamer was created to help students and professionals manage their learning and work more efficiently, especially those who might struggle with organizing complex information.",
        "feature": "TaskTamer offers three main features: Task Breakdown, Content Summarization, and Quiz Generation.",
        "example": "Try entering 'Write a research paper on AI ethics' in the Task Breakdown section to see how TaskTamer breaks it into manageable steps.",
        "step": "TaskTamer breaks down complex tasks into manageable steps based on the type of task you enter.",
        "task": "Enter your task in the Task Breakdown section and TaskTamer will divide it into actionable steps.",
        "summary": "The Content Summarizer extracts key points from your text or from a webpage to give you a quick overview.",
        "quiz": "The Quiz Generator creates interactive quizzes from your content to help test your understanding."
    }
    
    # Simple keyword matching
    question_lower = question.lower()
    for keyword, response in responses.items():
        if keyword in question_lower:
            return response
            
    # Default response
    return "I'm here to help with task breakdown, summarization, and quiz generation. Feel free to ask about any of these features or how to use TaskTamer effectively."
