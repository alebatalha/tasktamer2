from typing import List, Dict, Any, Optional
import random

def generate_adhd_tip() -> str:

    tips = [
        "Use a colorful pen to make this step more engaging!",
        "Stand up or move around while working on this to stay energized.",
        "Play focus music in the background to maintain concentration.",
        "Try body doubling - work with someone else nearby for accountability.",
        "Set a visual timer for this step to make time more concrete.",
        "Use the Pomodoro technique - 25 minutes of work, then a 5-minute break.",
        "Minimize distractions by turning off notifications during this step.",
        "Break this step down further if it feels overwhelming.",
        "Create a designated workspace for this task to signal 'focus time' to your brain.",
        "Use a fidget toy to help with focus during this step.",
        "Consider using text-to-speech for reading content to engage multiple senses.",
        "Try the 'body scan' technique if you feel restless - focus on each part of your body briefly.",
        "Use sticky notes for this step to make it more tactile and visual.",
        "Verbalize your thoughts out loud to maintain focus and clarity.",
        "Try the '5-4-3-2-1' grounding technique if you feel scattered (notice 5 things you see, 4 things you touch, etc.)",
    ]
    return random.choice(tips)

def generate_reward_suggestion() -> str:
    rewards = [
        "Watch a short funny video after completing this section!",
        "Take a 5-minute dance break to your favorite song!",
        "Grab a small healthy snack as a reward for your progress.",
        "Check social media for 5 minutes (set a timer!).",
        "Step outside for a quick breath of fresh air.",
        "Do a quick stretch routine to refresh your body.",
        "Make a cup of tea or coffee to enjoy.",
        "Send a message to a friend to celebrate your progress.",
        "Play a quick game on your phone as a mental reset.",
        "Give yourself a high five and positive self-talk for your accomplishment!",
        "Doodle or color for 5 minutes as a creative break.",
        "Listen to a favorite song as a mini-celebration.",
        "Browse something you're interested in (but not related to work) for 5 minutes.",
        "Do a quick mindfulness meditation to reset your focus.",
        "Add a sticker or checkmark to your progress tracker!"
    ]
    return random.choice(rewards)

class TaskBreakdown:
    
    
    def __init__(self, detail_level: str = "standard"):
    
        self.detail_level = detail_level
        
    def get_step_count(self) -> int:

        if self.detail_level == "basic":
            return 5
        elif self.detail_level == "comprehensive":
            return 10
        else:  # standard
            return 7

    def break_task(self, task_description: str, detail_level: Optional[str] = None) -> Dict[str, Any]:
     
        if detail_level:
            self.detail_level = detail_level
            
        if not task_description:
            return {
                "task": "",
                "overview": "Please provide a task description to break down.",
                "steps": [],
                "reward_suggestion": ""
            }
        
        task_lower = task_description.lower()
        
        task_type = self._identify_task_type(task_lower)
        
      
        overview = self._create_overview(task_description, task_type)
        
       
        steps = self._generate_steps(task_type, self.get_step_count())
        
       
        reward = generate_reward_suggestion()
        
        return {
            "task": task_description,
            "overview": overview,
            "steps": steps,
            "reward_suggestion": reward
        }
    
    def _identify_task_type(self, task_lower: str) -> str:
       
        if "essay" in task_lower or "paper" in task_lower or "research" in task_lower or "write" in task_lower and "report" in task_lower:
            return "academic_writing"
        elif "presentation" in task_lower or "slides" in task_lower:
            return "presentation"
        elif "project" in task_lower or "manage" in task_lower:
            return "project_management"
        elif "marketing" in task_lower or "campaign" in task_lower:
            return "marketing"
        elif "website" in task_lower or "web" in task_lower and "design" in task_lower:
            return "web_design"
        elif "event" in task_lower or "conference" in task_lower or "workshop" in task_lower:
            return "event_planning"
        elif "book" in task_lower or "novel" in task_lower:
            return "creative_writing"
        elif "job" in task_lower and ("search" in task_lower or "find" in task_lower or "hunt" in task_lower):
            return "job_search"
        elif "move" in task_lower or "moving" in task_lower or "relocate" in task_lower:
            return "relocation"
        elif "study" in task_lower or "exam" in task_lower or "test" in task_lower:
            return "studying"
        elif "budget" in task_lower or "finance" in task_lower or "money" in task_lower:
            return "financial_planning"
        else:
            return "general"
    
    def _create_overview(self, task: str, task_type: str) -> str:
      
        overviews = {
            "academic_writing": f"This task involves planning, researching, and writing {task}. It might seem overwhelming, but breaking it into smaller steps makes it totally doable! We'll focus on one small chunk at a time.",
            
            "presentation": f"Creating {task} involves organizing your ideas, designing slides, and preparing your delivery. By breaking this down into bite-sized steps, you'll build an impressive presentation without feeling overwhelmed!",
            
            "project_management": f"Managing {task} requires coordination and organization. We'll break this into smaller, manageable actions so you can make steady progress without feeling overwhelmed by the big picture.",
            
            "marketing": f"Developing {task} involves creativity, planning, and execution. By breaking this down into smaller steps, you'll create an effective campaign without getting lost in the details!",
            
            "web_design": f"Creating {task} involves planning, designing, and implementing. We'll tackle this one step at a time, making the process enjoyable rather than overwhelming!",
            
            "event_planning": f"Organizing {task} involves many moving parts. We'll break this down into smaller, actionable tasks so you can create a successful event without feeling overwhelmed!",
            
            "creative_writing": f"Writing {task} is a creative journey that we'll break into manageable steps. This approach will help maintain your creative flow while making steady progress!",
            
            "job_search": f"Finding a new job can feel overwhelming, but we'll break down {task} into smaller, daily actions that will build momentum and confidence in your search!",
            
            "relocation": f"Moving can be one of life's most stressful events! We'll break down {task} into smaller, manageable steps to reduce anxiety and ensure nothing gets missed.",
            
            "studying": f"Preparing for {task} requires effective study strategies. We'll break this down into focused study sessions with specific goals to maximize learning without burnout!",
            
            "financial_planning": f"Creating {task} involves understanding your finances and making thoughtful decisions. We'll break this down into smaller steps that make the process less overwhelming!",
            
            "general": f"We'll break down '{task}' into smaller, actionable steps. By focusing on one step at a time, you'll make steady progress without feeling overwhelmed by the entire task!"
        }
        
        return overviews.get(task_type, overviews["general"])
    
    def _generate_steps(self, task_type: str, step_count: int) -> List[Dict[str, Any]]:
        """Generate steps based on task type."""
       
        from .task_templates import get_task_steps
        
      
        raw_steps = get_task_steps(task_type)
        
       
        if len(raw_steps) > step_count:
           
            adjusted_steps = []
            step_indices = [int(i * len(raw_steps) / step_count) for i in range(step_count)]
            for i in range(len(step_indices)):
                if i + 1 < len(step_indices):
                  
                    if step_indices[i + 1] - step_indices[i] > 1:
                        combined_step = raw_steps[step_indices[i]].copy()
                        for j in range(step_indices[i] + 1, step_indices[i + 1]):
                            combined_step["description"] += f" Also, {raw_steps[j]['description'].lower()}"
                        adjusted_steps.append(combined_step)
                    else:
                        adjusted_steps.append(raw_steps[step_indices[i]])
                else:
                    adjusted_steps.append(raw_steps[step_indices[i]])
            raw_steps = adjusted_steps
        elif len(raw_steps) < step_count:
       
            extended_steps = []
            for step in raw_steps:
                extended_steps.append(step)
                if len(extended_steps) < step_count and "sub_steps" in step:
                    for sub_step in step["sub_steps"][:step_count - len(extended_steps)]:
                        new_step = {
                            "description": sub_step,
                            "time": step["time"] // 2,  
                            "priority": "Medium" if step["priority"] == "High" else "Low"
                        }
                        extended_steps.append(new_step)
            raw_steps = extended_steps[:step_count]
        
      
        formatted_steps = []
        for index, step in enumerate(raw_steps[:step_count], 1):
            formatted_step = {
                "number": index,
                "description": step["description"],
                "time": step.get("time", 15), 
                "priority": step.get("priority", "Medium"),
                "adhd_tip": step.get("adhd_tip", generate_adhd_tip())
            }
            formatted_steps.append(formatted_step)
            
        return formatted_steps

def break_task(task_description: str) -> List[str]:
    """
    Legacy function to break down a task into steps.
    
    Args:
        task_description: The task to break down
        
    Returns:
        List of step descriptions
    """
    task_breaker = TaskBreakdown()
    result = task_breaker.break_task(task_description)

    return [step["description"] for step in result["steps"]]