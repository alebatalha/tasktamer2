def ask_question(question: str) -> str:
    question_lower = question.lower()
    
    # Task Breakdown questions
    if any(kw in question_lower for kw in ["task", "break", "breakdown", "divide", "steps"]):
        return (
            "The Task Breakdown feature helps you divide complex tasks into manageable steps. "
            "Just enter your task in the text area and click 'Break Down Task'. "
            "TaskTamer will analyze your task and provide a step-by-step breakdown. "
            "You can download the breakdown for later reference."
        )
    
    # Summarization questions
    elif any(kw in question_lower for kw in ["summary", "summarize", "summarization", "extract"]):
        return (
            "The Summarization feature helps you extract key information from text or web content. "
            "You can either paste text directly or provide a URL. "
            "TaskTamer will analyze the content and generate a concise summary. "
            "This is great for quickly understanding articles, research papers, or any long-form content."
        )
    
    # Quiz questions
    elif any(kw in question_lower for kw in ["quiz", "question", "test", "multiple choice"]):
        return (
            "The Quiz Generator creates multiple-choice questions based on your provided content. "
            "Simply paste your text or enter a URL, and TaskTamer will generate quiz questions. "
            "You can take the quiz directly in the app to test your knowledge, "
            "and download the questions for later study."
        )
    
    # About TaskTamer
    elif any(kw in question_lower for kw in ["about", "purpose", "what is", "developed", "creator"]):
        return (
            "TaskTamer is a productivity tool developed by Alessandra Batalha as part of her final year project "
            "at Dublin Business School. It's designed to help students and professionals manage "
            "their learning and work tasks more efficiently, particularly those with ADHD. "
            "The application combines task breakdown, content summarization, and quiz generation "
            "features to improve productivity and learning."
        )
    
    # How to use
    elif any(kw in question_lower for kw in ["how to", "use", "work", "help", "instruction"]):
        return (
            "To use TaskTamer, select a feature from the sidebar navigation. Each feature has its own page "
            "with clear instructions. For example, to break down a task, go to Task Breakdown, enter your task, "
            "and click the button. For summarization, you can paste text or enter a URL. "
            "The Quiz Generator works similarly, allowing you to create questions from your content. "
            "Feel free to ask about specific features if you need more details!"
        )
    
    # Technical questions
    elif any(kw in question_lower for kw in ["technology", "built", "made", "stack", "code"]):
        return (
            "TaskTamer is built using Python with Streamlit for the web interface. "
            "It uses BeautifulSoup for web scraping, requests for HTTP interactions, "
            "and various text processing techniques. The application has a modular architecture "
            "with separate components for task breakdown, summarization, quiz generation, "
            "and the chat assistant. This design makes it easy to maintain and extend."
        )
    
    # Fallback
    else:
        return (
            "I'm your TaskTamer assistant! I can help you learn how to use our features including "
            "task breakdown, summarization, and quiz generation. Please ask specific questions about "
            "these features or how to use the application, and I'll be happy to assist you."
        )