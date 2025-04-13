def ask_question(question: str) -> str:
    """
    Otto, the TaskTamer assistant, answers questions about productivity and the app.
    
    Args:
        question: The user's question
        
    Returns:
        Otto's response to the question
    """
    if not question:
        return "Hi, I'm Otto! How can I help you with your productivity today? Feel free to ask me about any of TaskTamer's features."

    
    question_lower = question.lower().strip()
    
    
    feature_responses = {
        "task": "TaskTamer's Task Breakdown feature helps you conquer large projects by dividing them into manageable steps. I recognize different types of projects (like research papers, presentations, or marketing campaigns) and generate customized steps. Try typing in something like 'Write a research paper' or 'Plan a marketing campaign'!",
        
        "summarize": "The Summarization feature extracts the key points from any text or webpage. It's perfect when you need to quickly understand the main ideas without reading everything. Just paste your text or enter a URL, and I'll create a concise summary for you.",
        
        "summary": "Use the Summary tool when you're short on time but need to grasp the essential points of an article, document, or webpage. It works by identifying the most important sentences and combining them into a coherent summary.",
        
        "quiz": "The Quiz Generator transforms any content into interactive questions to test your knowledge. It's great for studying or reinforcing what you've learned. Enter your text or a webpage URL, adjust how many questions you want, and start testing yourself!",
        
        "test": "Testing your knowledge is easy with TaskTamer's Quiz Generator. Just provide some study material, and I'll create questions to help you assess your understanding and retention of the information.",
        
        "break down": "Breaking down complex tasks is one of my specialties! The Task Breakdown feature helps you take overwhelming projects and split them into clear, actionable steps. Just describe your task, and I'll create a step-by-step plan for you.",
        
        "assistant": "I'm Otto, your TaskTamer assistant! I'm here to help you use the app, answer questions about productivity, and provide guidance on managing your tasks and learning more efficiently.",
        
        "chat": "You're chatting with me right now! I'm Otto, your productivity assistant. I can answer questions about TaskTamer features, provide productivity tips, or help you figure out how to approach your tasks and projects."
    }
    
    
    how_to_responses = {
        "use task": "To use the Task Breakdown feature: 1) Go to the 'Task Breakdown' page from the sidebar, 2) Enter your task in the text area (be as specific as possible), 3) Click 'Break Down Task', and 4) Review your step-by-step plan, which you can download for reference.",
        
        "use summary": "To summarize content: 1) Navigate to the 'Summarization' page, 2) Either paste your text in the 'Text Input' tab or enter a webpage URL in the 'URL' tab, 3) Click 'Summarize Text' or 'Summarize URL', and 4) View your summary, which you can download if needed.",
        
        "use quiz": "To create a quiz: 1) Go to the 'Quiz Generator' page, 2) Enter your content or a URL containing study material, 3) Adjust the number of questions using the slider, 4) Click 'Generate Quiz', 5) Answer the questions and submit to see your score.",
        
        "download": "You can download your results from any of the main features. After generating a task breakdown, summary, or quiz, look for the download button below the results. Task breakdowns and summaries download as text files, while quizzes download as JSON files that you can reimport later.",
        
        "save": "TaskTamer allows you to download your results for future reference. Look for the download buttons below your generated content. You can save task breakdowns, summaries, and quizzes to your computer.",
        
        "start": "To get started with TaskTamer: 1) Choose a feature from the sidebar (Task Breakdown, Summarization, or Quiz Generator), 2) Enter your content according to the instructions, 3) Click the action button (like 'Break Down Task'), and 4) Review and save your results if desired."
    }
    
    #
    productivity_responses = {
        "productive": "Being more productive isn't about working harder—it's about working smarter! Try techniques like: 1) Breaking large tasks into smaller steps (TaskTamer can help with this!), 2) Using the Pomodoro technique (25 minutes of focus followed by a 5-minute break), 3) Managing your energy, not just your time, by scheduling difficult tasks when you're naturally most alert.",
        
        "focus": "Improving focus takes practice. Try these techniques: 1) Remove distractions by silencing notifications, 2) Use the Pomodoro technique to work in focused bursts, 3) Create a dedicated workspace, 4) Use tools like TaskTamer to break overwhelming tasks into manageable pieces, and 5) Take short breaks to recharge your mental energy.",
        
        "procrastinate": "Procrastination often comes from feeling overwhelmed or unclear about next steps. TaskTamer's breakdown feature can help by creating clear, actionable steps. Other tips: 1) Start with just 5 minutes of work to build momentum, 2) Use the 'two-minute rule'—if something takes less than two minutes, do it now, 3) Create artificial deadlines with rewards when you meet them.",
        
        "distract": "Reducing distractions is crucial for productivity. Try: 1) Putting your phone in another room or using an app blocker, 2) Working in shorter, focused sessions (25-45 minutes), 3) Creating a physical environment that promotes focus, 4) Using noise-cancelling headphones or background sound like white noise, and 5) Keeping a 'distraction list' to jot down off-topic thoughts for later.",
        
        "adhd": "TaskTamer was designed with ADHD-friendly features in mind! The task breakdown helps combat overwhelm by creating clear steps. The summarizer helps you extract key information quickly. The quiz feature promotes active engagement with material. I recommend using external timers with TaskTamer to create time boundaries for each task step.",
        
        "prioritize": "Effective prioritization is key to productivity. Try methods like: 1) The Eisenhower Matrix (urgent/important grid), 2) The 1-3-5 Rule (plan to accomplish one big thing, three medium things, and five small things), 3) MoSCoW method (Must do, Should do, Could do, Won't do). TaskTamer can help break down your prioritized tasks into actionable steps.",
        
        "schedule": "Effective scheduling involves knowing your energy patterns. Plan your most demanding tasks during your peak energy hours. Use time blocking to dedicate specific hours to similar tasks. Don't forget to schedule breaks and buffer time between tasks. TaskTamer can help you break down each scheduled task into manageable steps.",
        
        "time management": "Effective time management combines good planning with flexibility. Try techniques like: 1) Time blocking your calendar, 2) The 2-minute rule (do it now if it takes less than 2 minutes), 3) Batching similar tasks together, 4) Using the Pomodoro technique, and 5) Planning your day the night before."
    }
    
    
    about_otto_responses = {
        "who are you": "I'm Otto, your friendly TaskTamer assistant! I'm here to help you break down tasks, summarize content, create quizzes, and become more productive. While I'm not a human, I'm designed to provide helpful, friendly assistance with your productivity challenges.",
        
        "your name": "My name is Otto! I'm your TaskTamer assistant, named after the word 'automate' because I help automate and simplify your productivity processes. How can I help you today?",
        
        "hello": "Hello there! I'm Otto, your TaskTamer assistant. How can I help you with your productivity today?",
        
        "hi otto": "Hi there! I'm happy to help with your productivity needs. Would you like to know about breaking down tasks, summarizing content, or creating quizzes?",
        
        "help me": "I'd be happy to help! TaskTamer offers several features: 1) Task Breakdown - turns complex projects into manageable steps, 2) Summarization - extracts key points from content, and 3) Quiz Generator - creates questions to test your knowledge. What would you like help with specifically?"
    }
    
    
    for key, response in about_otto_responses.items():
        if key in question_lower:
            return response
    
    
    for key, response in how_to_responses.items():
        if key in question_lower:
            return response
            
    
    for key, response in feature_responses.items():
        if key in question_lower:
            return response
    
    
    for key, response in productivity_responses.items():
        if key in question_lower:
            return response
    
    
    if "thank" in question_lower:
        return "You're welcome! I'm always here to help. Is there anything else you'd like to know about TaskTamer or productivity?"
    
    if any(word in question_lower for word in ["bye", "goodbye", "see you"]):
        return "Goodbye! Feel free to come back whenever you need help with your tasks or productivity. Have a productive day!"
    
    
    return "I'm Otto, your productivity assistant! I can help with task breakdown, content summarization, and quiz generation. I also have tips for improving focus, managing time, and staying productive. Could you rephrase your question or ask about a specific TaskTamer feature?"