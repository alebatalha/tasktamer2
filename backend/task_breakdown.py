import re
from typing import List, Dict, Any, Optional
import random
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Check if advanced models are available
try:
    from transformers import pipeline
    ADVANCED_MODELS_AVAILABLE = True
    logger.info("Advanced models are available")
except ImportError:
    ADVANCED_MODELS_AVAILABLE = False
    logger.info("Advanced models not available, using base functionality")

def break_down_task(task_description: str) -> List[str]:
    """
    AI-powered function to break down a task into steps.
    This maintains the original API for backward compatibility.
    
    Args:
        task_description: The task to break down
        
    Returns:
        List of step descriptions
    """
    task_lower = task_description.lower()
    
    # First check if we can use AI to generate steps
    if ADVANCED_MODELS_AVAILABLE:
        try:
            # Try to use a text generation model for more personalized steps
            generator = pipeline("text-generation", model="gpt2")
            
            prompt = f"Break down the task of '{task_description}' into steps:\n1."
            output = generator(prompt, max_length=200, num_return_sequences=1)[0]['generated_text']
            
            # Extract just the generated steps
            if "steps:" in output.lower() and "1." in output:
                steps_text = output.split("1.")[1].strip()
                steps = []
                
                # Try to find numbered steps
                step_matches = re.findall(r'\d+\.\s*(.*?)(?=\d+\.|$)', steps_text + "999.")
                if step_matches:
                    steps = [match.strip() for match in step_matches if match.strip()]
                    
                # Add the first step that was part of the prompt
                if steps and "1." in output:
                    first_step = output.split("1.")[1].split("2.")[0].strip()
                    if first_step:
                        steps.insert(0, first_step)
                
                # If we found valid steps, return them
                if len(steps) >= 3:
                    # Clean up and limit to 7 steps
                    steps = [s for s in steps if 3 < len(s) < 100 and not s.isdigit()]
                    return steps[:7]
            
            logger.info("AI generation didn't produce usable steps, falling back to templates")
        except Exception as e:
            logger.error(f"Error using AI for task breakdown: {str(e)}")
    
    # Fall back to template-based approach (original implementation)
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

class TaskBreakdown:
    """
    Enhanced TaskBreakdown class with AI-driven insights.
    Works with the existing UI without modifications.
    """
    
    def __init__(self, detail_level: str = "standard"):
        """
        Initialize the TaskBreakdown system.
        
        Args:
            detail_level: Level of detail for task breakdown (basic, standard, comprehensive)
        """
        self.detail_level = detail_level
        self.generator = None
        
        # Initialize advanced model if available
        if ADVANCED_MODELS_AVAILABLE:
            try:
                # Try to load a text generation model
                self.generator = pipeline("text-generation", model="gpt2")
                logger.info("Initialized text generation model for task breakdown")
            except Exception as e:
                logger.error(f"Error loading text generation model: {str(e)}")
    
    def get_step_count(self) -> int:
        """Return number of steps based on detail level."""
        if self.detail_level == "basic":
            return 5
        elif self.detail_level == "comprehensive":
            return 9
        else:  # standard
            return 7
    
    def break_task(self, task_description: str, detail_level: Optional[str] = None) -> Dict[str, Any]:
        """
        Break down a task with enhanced AI insights when available.
        
        Args:
            task_description: The task to break down
            detail_level: Optional override for detail level
            
        Returns:
            Dictionary with task breakdown details compatible with the existing UI
        """
        if detail_level:
            self.detail_level = detail_level
            
        if not task_description:
            return {
                "task": "",
                "overview": "Please provide a task description to break down.",
                "steps": [],
                "reward_suggestion": ""
            }
        
        # Determine step count
        step_count = self.get_step_count()
        
        # 1. Get basic step breakdown
        basic_steps = break_down_task(task_description)
        
        # 2. Try to enhance steps with AI if available
        enhanced_steps = self._enhance_steps_with_ai(task_description, basic_steps, step_count)
        
        # 3. Create overview
        overview = self._create_task_overview(task_description)
        
        # 4. Format steps for UI compatibility
        formatted_steps = []
        for i, step_text in enumerate(enhanced_steps[:step_count]):
            # Create each step with the required fields for the UI
            step = {
                "number": i + 1,
                "description": step_text,
                "time": random.randint(10, 30),  # Estimate time (5-30 minutes in the UI's scale)
                "priority": self._assign_priority(i, step_count),
                "adhd_tip": self._generate_adhd_tip()
            }
            formatted_steps.append(step)
        
        # 5. Add reward suggestion
        reward = self._generate_reward_suggestion(task_description)
        
        return {
            "task": task_description,
            "overview": overview,
            "steps": formatted_steps,
            "reward_suggestion": reward
        }
    
    def _enhance_steps_with_ai(self, task_description: str, basic_steps: List[str], step_count: int) -> List[str]:
        """Try to enhance steps with AI when available."""
        if not self.generator:
            return basic_steps
        
        try:
            enhanced_steps = []
            
            # Try to generate sub-steps or details for each basic step
            for step in basic_steps:
                # First, try to make the step more specific to the task
                prompt = f"Task: {task_description}\nMake this step more specific: {step}\nBetter step:"
                
                result = self.generator(prompt, max_length=50, num_return_sequences=1)[0]['generated_text']
                
                # Extract the enhanced step
                if "Better step:" in result:
                    enhanced_step = result.split("Better step:")[1].strip()
                    # Only use if it's reasonable
                    if enhanced_step and 5 < len(enhanced_step) < 100:
                        enhanced_steps.append(enhanced_step)
                    else:
                        enhanced_steps.append(step)
                else:
                    enhanced_steps.append(step)
            
            # If we need more steps, try to generate them
            if len(enhanced_steps) < step_count:
                existing_steps_text = "\n".join([f"{i+1}. {s}" for i, s in enumerate(enhanced_steps)])
                
                prompt = f"Task: {task_description}\nExisting steps:\n{existing_steps_text}\n\nAdditional steps:\n{len(enhanced_steps)+1}."
                
                result = self.generator(prompt, max_length=150, num_return_sequences=1)[0]['generated_text']
                
                # Try to extract additional steps
                if f"{len(enhanced_steps)+1}." in result:
                    additional_text = result.split(f"{len(enhanced_steps)+1}.")[1]
                    additional_steps = re.findall(r'\d+\.\s*(.*?)(?=\d+\.|$)', additional_text + "999.")
                    
                    for step in additional_steps:
                        step = step.strip()
                        if step and 5 < len(step) < 100:
                            enhanced_steps.append(step)
                            if len(enhanced_steps) >= step_count:
                                break
            
            # If we still don't have enough steps, add generic ones
            while len(enhanced_steps) < step_count:
                enhanced_steps.append(f"Continue progress on {task_description}")
            
            return enhanced_steps
        
        except Exception as e:
            logger.error(f"Error enhancing steps with AI: {str(e)}")
            return basic_steps
    
    def _create_task_overview(self, task_description: str) -> str:
        """Create an overview for the task."""
        if self.generator:
            try:
                prompt = f"Write a brief, encouraging overview for breaking down this task: {task_description}. Keep it under 3 sentences."
                
                result = self.generator(prompt, max_length=150, num_return_sequences=1)[0]['generated_text']
                
                # Try to extract just the overview
                if "sentences." in result:
                    overview = result.split("sentences.")[1].strip()
                    if overview and len(overview) > 30:
                        return overview
            except Exception as e:
                logger.error(f"Error generating overview: {str(e)}")
        
        # Fallback to template overview
        return f"Breaking down '{task_description}' into manageable steps will help you make steady progress without feeling overwhelmed. Each step builds on the previous one to help you complete the task efficiently."
    
    def _assign_priority(self, step_index: int, total_steps: int) -> str:
        """Assign priority level to a step based on its position."""
        if step_index == 0 or step_index == total_steps - 1:
            return "High"  # First and last steps are high priority
        elif step_index < total_steps // 3:
            return "High"  # Early steps are high priority
        elif step_index < 2 * total_steps // 3:
            return "Medium"  # Middle steps are medium priority
        else:
            return "Low"  # Later steps are low priority
    
    def _generate_adhd_tip(self) -> str:
        """Generate an ADHD-friendly tip for a task step."""
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
        
        # Try to generate a custom tip if generator is available
        if self.generator:
            try:
                prompt = "Generate a brief ADHD-friendly productivity tip to help with focus. Tip:"
                
                result = self.generator(prompt, max_length=50, num_return_sequences=1)[0]['generated_text']
                
                if "Tip:" in result:
                    tip = result.split("Tip:")[1].strip()
                    if tip and 10 < len(tip) < 100:
                        return tip
            except Exception:
                pass  # Silently fall back to template tips
        
        return random.choice(tips)
    
    def _generate_reward_suggestion(self, task_description: str) -> str:
        """Generate a reward suggestion for completing the task."""
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
        
        # Try to generate a custom reward if generator is available
        if self.generator:
            try:
                prompt = f"Suggest a small, specific reward for completing this task: {task_description}"
                
                result = self.generator(prompt, max_length=50, num_return_sequences=1)[0]['generated_text']
                
                if ":" in result:
                    reward = result.split(":")[1].strip()
                    if reward and 10 < len(reward) < 150:
                        return reward
            except Exception:
                pass  # Silently fall back to template rewards
        
        return random.choice(rewards)


def break_task(task_description: str) -> List[str]:
    """
    Compatibility function for the existing UI.
    
    Args:
        task_description: The task to break down
        
    Returns:
        List of step descriptions
    """
    task_breaker = TaskBreakdown()
    result = task_breaker.break_task(task_description)
    return [step["description"] for step in result["steps"]]