from typing import List

def break_task(task_description: str) -> List[str]:
    """
    Break a complex task into manageable steps.
    
    Args:
        task_description: The task to break down
        
    Returns:
        A list of steps
    """
    if not task_description:
        return []
        
    task_lower = task_description.lower()
    
    
    if "essay" in task_lower or ("write" in task_lower and "paper" in task_lower):
        return [
            "Research and define your topic clearly",
            "Create a thesis statement or main argument",
            "Find credible sources and take detailed notes",
            "Create an outline with your main points",
            "Write your introduction with a hook and thesis",
            "Develop each paragraph with evidence and analysis",
            "Write a strong conclusion that restates your thesis",
            "Review and edit for clarity and coherence",
            "Check grammar, spelling, and formatting"
        ]
    elif "research" in task_lower and "paper" in task_lower:
        return [
            "Define your research question and objectives",
            "Conduct a preliminary literature review",
            "Develop a research methodology",
            "Collect data and information from credible sources",
            "Analyze your findings and identify patterns",
            "Create a detailed outline with your main arguments",
            "Write the introduction and literature review",
            "Present your methodology and findings",
            "Discuss implications and limitations of your research",
            "Write a conclusion and recommend future research",
            "Format your paper according to required style (APA, MLA, etc.)"
        ]
    
    elif "presentation" in task_lower or "slides" in task_lower:
        return [
            "Define your topic and key message",
            "Research content and gather supporting data",
            "Identify your target audience and their needs",
            "Create a compelling structure with intro, body, conclusion",
            "Design visual slides that enhance your message",
            "Prepare speaker notes and practice delivery",
            "Review timing and pace of presentation",
            "Prepare for potential questions",
            "Rehearse full presentation at least twice"
        ]
    
    elif "project" in task_lower or "manage" in task_lower:
        return [
            "Define project scope, objectives, and deliverables",
            "Create a timeline with key milestones and deadlines",
            "Identify required resources and budget constraints",
            "Assign responsibilities to team members",
            "Develop a communication plan for stakeholders",
            "Set up tracking and reporting mechanisms",
            "Monitor progress and address issues promptly",
            "Conduct regular check-ins and status updates",
            "Perform quality checks throughout the project",
            "Finalize deliverables and get approval",
            "Conduct a project review and document lessons learned"
        ]
   
    elif "marketing" in task_lower or "campaign" in task_lower:
        return [
            "Define marketing objectives and target audience",
            "Research market trends and competitor strategies",
            "Develop key messaging and unique selling points",
            "Create a content strategy and calendar",
            "Design marketing materials and visuals",
            "Select appropriate marketing channels",
            "Set up tracking and analytics systems",
            "Launch campaign according to schedule",
            "Monitor performance and engagement metrics",
            "Adjust strategy based on performance data",
            "Evaluate overall campaign success and ROI"
        ]
    
    elif "website" in task_lower or "web" in task_lower and "design" in task_lower:
        return [
            "Define website purpose and target audience",
            "Conduct user research and create personas",
            "Map out site structure and user journeys",
            "Create wireframes for key pages",
            "Design visual style and mockups",
            "Develop responsive HTML/CSS templates",
            "Implement functionality and interactive elements",
            "Create and integrate content (text, images, videos)",
            "Test website across devices and browsers",
            "Optimize for performance and SEO",
            "Launch website and monitor analytics"
        ]
    
    elif "event" in task_lower or "conference" in task_lower or "workshop" in task_lower:
        return [
            "Define event purpose, goals, and target audience",
            "Set date, time, and select venue/platform",
            "Create a detailed budget and secure funding",
            "Develop event agenda and schedule",
            "Book speakers, presenters, or entertainers",
            "Arrange catering, equipment, and other logistics",
            "Create marketing materials and promote the event",
            "Set up registration system and track attendees",
            "Prepare day-of materials and signage",
            "Brief team members on their roles and responsibilities",
            "Execute the event according to plan",
            "Collect feedback and evaluate success"
        ]
    
    elif "book" in task_lower or "novel" in task_lower:
        return [
            "Define your book concept, genre, and target audience",
            "Research your topic or develop your story idea",
            "Create an outline with chapters or major sections",
            "Develop character profiles and plot arcs (for fiction)",
            "Set a writing schedule with regular milestones",
            "Write the first draft, focusing on content not perfection",
            "Take breaks between writing sessions for perspective",
            "Revise your draft for structure, flow, and clarity",
            "Edit for grammar, style, and consistency",
            "Get feedback from beta readers or editors",
            "Make final revisions based on feedback",
            "Prepare for publication (traditional or self-publishing)"
        ]
    
    elif "job" in task_lower and ("search" in task_lower or "find" in task_lower or "hunt" in task_lower):
        return [
            "Define your career goals and ideal job criteria",
            "Update your resume and LinkedIn profile",
            "Research target companies and industries",
            "Set up job alerts on relevant platforms",
            "Prepare a basic cover letter template",
            "Network with industry professionals",
            "Apply to positions that match your qualifications",
            "Customize each application to the specific job",
            "Prepare for interviews with common questions",
            "Research each company before interviewing",
            "Follow up after applications and interviews",
            "Evaluate offers and negotiate as needed"
        ]
    
    elif "move" in task_lower or "moving" in task_lower or "relocate" in task_lower:
        return [
            "Create a moving timeline and master checklist",
            "Research and choose your new location",
            "Set a moving budget and track expenses",
            "Hire movers or rent a moving truck",
            "Collect packing supplies (boxes, tape, markers)",
            "Sort belongings and decide what to keep, donate, or sell",
            "Change your address with USPS and important services",
            "Transfer or set up utilities at new location",
            "Pack items room by room, labeling each box",
            "Plan for special items that need careful handling",
            "Clean your old place and prepare for inspection",
            "Unpack essentials first, then organize room by room"
        ]
   
    else:
        return [
            "Define your goal and desired outcome",
            "Break the task into main components or phases",
            "Prioritize components and create a logical sequence",
            "Set clear deadlines for each phase",
            "Identify resources, tools, and information needed",
            "Anticipate potential obstacles and prepare solutions",
            "Create a detailed action plan with specific steps",
            "Set up a tracking system to monitor progress",
            "Establish check-in points for review and adjustment",
            "Execute the plan and adapt as needed",
            "Evaluate results and document lessons learned"
        ]