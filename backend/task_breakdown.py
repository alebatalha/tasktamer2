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
    
    if "research" in task_lower:
        return [
            "Define your research topic and goals",
            "Gather relevant sources and materials",
            "Take notes from your sources",
            "Organize your information",
            "Create an outline",
            "Write a first draft",
            "Revise and edit your work"
        ]
    elif "presentation" in task_lower:
        return [
            "Define your presentation topic and audience",
            "Research key information",
            "Create an outline",
            "Design slides or visual aids",
            "Practice your delivery",
            "Get feedback and revise",
            "Finalize your presentation"
        ]
    elif "project" in task_lower:
        return [
            "Define project scope and objectives",
            "Create a timeline with milestones",
            "Identify required resources",
            "Assign responsibilities",
            "Track progress and adjust as needed",
            "Review and quality check",
            "Finalize and deliver"
        ]
    else:
        # Generic task breakdown
        return [
            "Define your goal and desired outcome",
            "Break down the main components",
            "Create a timeline",
            "Gather necessary resources",
            "Work through each component",
            "Review progress regularly",
            "Complete final review"
        ]
