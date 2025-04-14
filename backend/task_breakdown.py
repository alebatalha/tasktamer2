import re
from typing import List

def break_down_task(task_description: str) -> List[str]:
    task_lower = task_description.lower()
    
    if "research" in task_lower or "paper" in task_lower:
        return [
            "Define your research topic and goals",
            "Gather relevant sources and materials",
            "Take notes from your sources",
            "Organize your information",
            "Create an outline",
            "Write a first draft",
            "Revise and edit your work"
        ]
    elif "presentation" in task_lower or "slide" in task_lower:
        return [
            "Define your presentation topic and audience",
            "Research key information",
            "Create an outline",
            "Design slides or visual aids",
            "Practice your delivery",
            "Get feedback and revise",
            "Finalize your presentation"
        ]
    elif "project" in task_lower or "manage" in task_lower:
        return [
            "Define project scope and objectives",
            "Create a timeline with milestones",
            "Identify required resources",
            "Assign responsibilities",
            "Track progress and adjust as needed",
            "Review and quality check",
            "Finalize and deliver"
        ]
    elif "budget" in task_lower or "finance" in task_lower:
        return [
            "Gather all financial information",
            "Identify income sources",
            "List all expenses",
            "Categorize expenses",
            "Set financial goals",
            "Create a spending plan",
            "Track and adjust regularly"
        ]
    elif "learning" in task_lower or "study" in task_lower:
        return [
            "Define what you want to learn",
            "Gather learning resources",
            "Break content into smaller chunks",
            "Create a study schedule",
            "Use active learning techniques",
            "Test your knowledge",
            "Review and reinforce regularly"
        ]
    elif "write" in task_lower or "essay" in task_lower:
        return [
            "Choose and narrow your topic",
            "Create a thesis statement",
            "Research supporting evidence",
            "Create an outline",
            "Write your introduction",
            "Develop body paragraphs with evidence",
            "Write a conclusion",
            "Edit and proofread"
        ]
    elif "event" in task_lower or "conference" in task_lower:
        return [
            "Define event goals and target audience",
            "Set date, time, and venue",
            "Create a budget",
            "Arrange speakers or entertainment",
            "Plan logistics (food, equipment, etc.)",
            "Create and distribute invitations",
            "Prepare day-of materials",
            "Follow up after the event"
        ]
    else:
        return [
            "Define your goal and desired outcome",
            "Break down the main components",
            "Create a timeline",
            "Gather necessary resources",
            "Work through each component",
            "Review progress regularly",
            "Complete final review"
        ]