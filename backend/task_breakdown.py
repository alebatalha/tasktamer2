import re
from typing import List, Dict, Any, Optional, Union
import random
import logging
import os
import json
import numpy as np

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Flag to indicate if advanced models are available
try:
    from sentence_transformers import SentenceTransformer
    from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
    from transformers import AutoModelForSeq2SeqLM
    ADVANCED_MODELS_AVAILABLE = True
    logger.info("Advanced models (transformers & sentence-transformers) are available")
except ImportError:
    ADVANCED_MODELS_AVAILABLE = False
    logger.info("Advanced models not available, using base functionality")

class RAGTaskBreakdown:
    """
    Enhanced Task Breakdown using Retrieval Augmented Generation (RAG)
    with Hugging Face models for more personalized and contextually relevant task steps.
    """
    
    def __init__(self, detail_level: str = "standard", 
                 embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2",
                 llm_model: str = "google/flan-t5-base"):
        """
        Initialize the RAG Task Breakdown system.
        
        Args:
            detail_level: Level of detail for task breakdown (basic, standard, comprehensive)
            embedding_model: Hugging Face model for embeddings
            llm_model: Hugging Face model for text generation
        """
        self.detail_level = detail_level
        self.embedding_model_name = embedding_model
        self.llm_model_name = llm_model
        
        # Initialize models if available
        self.embedding_model = None
        self.model = None
        self.tokenizer = None
        self.text_generator = None
        self.is_seq2seq = False
        
        # Initialize template database
        self.template_db = {}
        
        # Only load models if the required libraries are available
        if ADVANCED_MODELS_AVAILABLE:
            self._initialize_models()
        
        # Load template database
        self._initialize_template_database()
    
    def _initialize_models(self):
        """Initialize the embedding and language models."""
        try:
            logger.info(f"Loading embedding model: {self.embedding_model_name}")
            self.embedding_model = SentenceTransformer(self.embedding_model_name)
        except Exception as e:
            logger.error(f"Error loading embedding model: {str(e)}")
            self.embedding_model = None
        
        try:
            logger.info(f"Loading language model: {self.llm_model_name}")
            self.tokenizer = AutoTokenizer.from_pretrained(self.llm_model_name)
            
            # Check if the model is a T5-style seq2seq model or a causal language model
            if "t5" in self.llm_model_name or "bart" in self.llm_model_name:
                self.model = AutoModelForSeq2SeqLM.from_pretrained(self.llm_model_name)
                self.is_seq2seq = True
            else:
                self.model = AutoModelForCausalLM.from_pretrained(self.llm_model_name)
                self.is_seq2seq = False
                
            self.text_generator = pipeline(
                "text2text-generation" if self.is_seq2seq else "text-generation",
                model=self.model,
                tokenizer=self.tokenizer,
                max_length=150,
                temperature=0.7
            )
        except Exception as e:
            logger.error(f"Error loading language model: {str(e)}")
            self.model = None
            self.tokenizer = None
            self.text_generator = None
            
    def _initialize_template_database(self) -> Dict[str, Any]:
        """Initialize the template database for retrieval."""
        # Define task templates
        task_templates = {
            "research": [
                "Define your research topic and goals",
                "Gather relevant sources and materials",
                "Take notes from your sources",
                "Organize your information",
                "Create an outline",
                "Write a first draft",
                "Revise and edit your work"
            ],
            "presentation": [
                "Define your presentation topic and audience",
                "Research key information",
                "Create an outline",
                "Design slides or visual aids",
                "Practice your delivery",
                "Get feedback and revise",
                "Finalize your presentation"
            ],
            "project_management": [
                "Define project scope and objectives",
                "Create a timeline with milestones",
                "Identify required resources",
                "Assign responsibilities",
                "Track progress and adjust as needed",
                "Review and quality check",
                "Finalize and deliver"
            ],
            "budgeting": [
                "Gather all financial information",
                "Identify income sources",
                "List all expenses",
                "Categorize expenses",
                "Set financial goals",
                "Create a spending plan",
                "Track and adjust regularly"
            ],
            "studying": [
                "Define what you want to learn",
                "Gather learning resources",
                "Break content into smaller chunks",
                "Create a study schedule",
                "Use active learning techniques",
                "Test your knowledge",
                "Review and reinforce regularly"
            ],
            "writing": [
                "Choose and narrow your topic",
                "Create a thesis statement",
                "Research supporting evidence",
                "Create an outline",
                "Write your introduction",
                "Develop body paragraphs with evidence",
                "Write a conclusion",
                "Edit and proofread"
            ],
            "event_planning": [
                "Define event goals and target audience",
                "Set date, time, and venue",
                "Create a budget",
                "Arrange speakers or entertainment",
                "Plan logistics (food, equipment, etc.)",
                "Create and distribute invitations",
                "Prepare day-of materials",
                "Follow up after the event"
            ],
            "general": [
                "Define your goal and desired outcome",
                "Break down the main components",
                "Create a timeline",
                "Gather necessary resources",
                "Work through each component",
                "Review progress regularly",
                "Complete final review"
            ]
        }
        
        # Convert simple task templates to enhanced format
        for task_type, steps in task_templates.items():
            formatted_steps = []
            for i, step in enumerate(steps, 1):
                formatted_step = {
                    "number": i,
                    "description": step,
                    "time": random.choice([10, 15, 20, 25, 30]),
                    "priority": random.choice(["High", "Medium", "Low"]),
                    "adhd_tip": self._generate_adhd_tip()
                }
                formatted_steps.append(formatted_step)
            
            self.template_db[task_type] = {
                "steps": formatted_steps,
                "embeddings": None
            }
        
        # Generate embeddings if model is available
        if self.embedding_model:
            for task_type, data in self.template_db.items():
                try:
                    step_descriptions = [step["description"] for step in data["steps"]]
                    embeddings = self.embedding_model.encode(step_descriptions)
                    self.template_db[task_type]["embeddings"] = embeddings
                    logger.info(f"Generated embeddings for task type: {task_type}")
                except Exception as e:
                    logger.error(f"Error generating embeddings for {task_type}: {str(e)}")
        
        return self.template_db
    
    def get_step_count(self) -> int:
        """Return number of steps based on detail level."""
        if self.detail_level == "basic":
            return 5
        elif self.detail_level == "comprehensive":
            return 10
        else:  # standard
            return 7
    
    def break_task(self, task_description: str, detail_level: Optional[str] = None) -> Dict[str, Any]:
        """
        Break down a task using RAG approach.
        
        Args:
            task_description: The task to break down
            detail_level: Optional override for detail level
            
        Returns:
            Dictionary with task breakdown
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
        
        logger.info(f"Breaking down task: {task_description[:50]}...")
        
        # 1. Identify task type
        task_type = self._identify_task_type(task_description.lower())
        logger.info(f"Identified task type: {task_type}")
        
        # 2. Create task overview
        overview = self._create_overview(task_description, task_type)
        
        # 3. Generate steps using RAG approach
        steps = self._generate_steps_with_rag(task_description, task_type, self.get_step_count())
        
        # 4. Generate reward suggestion
        reward = self._generate_reward_suggestion(task_description)
        
        return {
            "task": task_description,
            "overview": overview,
            "steps": steps,
            "reward_suggestion": reward
        }
    
    def _identify_task_type(self, task_lower: str) -> str:
        """Identify the task type based on keywords and embedding similarity."""
        # Keyword mapping for task types
        keyword_mapping = {
            "research": ["research", "paper", "study", "investigate", "analyze", "thesis"],
            "presentation": ["presentation", "slide", "talk", "speech", "present"],
            "project_management": ["project", "manage", "coordinate", "plan", "organize", "team"],
            "budgeting": ["budget", "finance", "money", "expense", "financial", "saving"],
            "studying": ["learning", "study", "practice", "learn", "class", "course", "exam"],
            "writing": ["write", "essay", "article", "blog", "story", "content", "document"],
            "event_planning": ["event", "conference", "meetup", "party", "gathering", "workshop"]
        }
        
        # Check for keyword matches
        for task_type, keywords in keyword_mapping.items():
            if any(keyword in task_lower for keyword in keywords):
                return task_type
        
        # If no keyword match and embedding model is available, use semantic similarity
        if self.embedding_model:
            try:
                # Create task embedding
                task_embedding = self.embedding_model.encode([task_lower])[0]
                
                # Create comparison descriptions
                task_descriptions = {
                    "research": "conducting research or writing a research paper",
                    "presentation": "creating and delivering a presentation",
                    "project_management": "managing a project with multiple components",
                    "budgeting": "creating a budget or managing finances",
                    "studying": "studying or learning a new subject",
                    "writing": "writing an essay, article, or creative piece",
                    "event_planning": "planning and organizing an event",
                    "general": "completing a general task or project"
                }
                
                # Find most similar task type
                max_similarity = -1
                best_match = "general"
                
                for task_type, description in task_descriptions.items():
                    description_embedding = self.embedding_model.encode([description])[0]
                    similarity = np.dot(task_embedding, description_embedding) / (
                        np.linalg.norm(task_embedding) * np.linalg.norm(description_embedding)
                    )
                    if similarity > max_similarity:
                        max_similarity = similarity
                        best_match = task_type
                
                return best_match
            except Exception as e:
                logger.error(f"Error in embedding task type identification: {str(e)}")
        
        # Default to general if no match found
        return "general"
    
    def _create_overview(self, task: str, task_type: str) -> str:
        """Create a personalized overview for the task."""
        # Try to generate with LLM if available
        if self.text_generator:
            try:
                prompt = f"Create a brief, encouraging overview for breaking down this task: {task}. "
                prompt += "The overview should explain why breaking down the task is helpful and give hope that it's achievable."
                
                generated = self.text_generator(prompt, max_length=150)[0]["generated_text"]
                
                # Extract the relevant part of the response
                if self.is_seq2seq:
                    overview = generated
                else:
                    # For causal models, extract just the generated part
                    if prompt in generated:
                        overview = generated.split(prompt)[1].strip()
                    else:
                        overview = generated
                
                if overview and len(overview) > 30:
                    return overview
            except Exception as e:
                logger.error(f"Error generating overview: {str(e)}")
        
        # Fallback to template overviews
        overviews = {
            "research": f"Breaking down your research on '{task}' into manageable steps will help you make steady progress. By tackling one piece at a time, you'll avoid feeling overwhelmed by the scope of the project.",
            
            "presentation": f"Creating '{task}' presentation may seem daunting, but with a step-by-step approach, you'll develop a polished final product. Focus on one component at a time to build your confidence.",
            
            "project_management": f"Managing '{task}' involves several moving parts. We'll break this down into clear, actionable steps that will help you stay organized and ensure nothing falls through the cracks.",
            
            "budgeting": f"Taking control of your finances with '{task}' becomes much easier when broken into smaller steps. This methodical approach will help you develop a comprehensive financial plan without feeling overwhelmed.",
            
            "studying": f"Learning about '{task}' is more effective when you break it into focused study sessions. This approach helps improve retention and makes the learning process more manageable.",
            
            "writing": f"Writing '{task}' becomes less intimidating when you approach it in stages. By breaking down the writing process, you'll maintain focus and develop your ideas more clearly.",
            
            "event_planning": f"Planning '{task}' involves many details, but tackling them one by one makes the process manageable. This breakdown will help ensure a successful event without the stress of last-minute scrambling.",
            
            "general": f"Breaking down '{task}' into smaller, actionable steps will help you make consistent progress. By focusing on one step at a time, you'll avoid feeling overwhelmed and maintain momentum."
        }
        
        return overviews.get(task_type, overviews["general"])
    
    def _retrieve_relevant_templates(self, task_description: str, task_type: str, count: int = 5) -> List[Dict]:
        """Retrieve the most relevant step templates based on semantic similarity."""
        # If embedding model is available, use similarity search
        if self.embedding_model and task_type in self.template_db and self.template_db[task_type]["embeddings"] is not None:
            try:
                # Encode the task description
                task_embedding = self.embedding_model.encode([task_description])[0]
                
                # Calculate similarity with all steps in the template database for this task type
                template_embeddings = self.template_db[task_type]["embeddings"]
                similarities = []
                
                for i, template_embedding in enumerate(template_embeddings):
                    similarity = np.dot(task_embedding, template_embedding) / (
                        np.linalg.norm(task_embedding) * np.linalg.norm(template_embedding)
                    )
                    similarities.append((i, similarity))
                
                # Sort by similarity and get top matches
                similarities.sort(key=lambda x: x[1], reverse=True)
                top_indices = [idx for idx, _ in similarities[:count]]
                
                # Return the corresponding steps
                return [self.template_db[task_type]["steps"][i] for i in top_indices]
            except Exception as e:
                logger.error(f"Error retrieving templates with embeddings: {str(e)}")
        
        # Fallback: Return steps from the template database
        if task_type in self.template_db and self.template_db[task_type]["steps"]:
            steps = self.template_db[task_type]["steps"]
            return steps[:count]
        
        # Ultimate fallback: Return steps from the general template
        return self.template_db["general"]["steps"][:count]
    
    def _generate_steps_with_rag(self, task_description: str, task_type: str, step_count: int) -> List[Dict[str, Any]]:
        """Generate task breakdown steps using the RAG approach."""
        # 1. Retrieve relevant templates
        relevant_templates = self._retrieve_relevant_templates(task_description, task_type, step_count)
        
        # 2. Generate personalized steps
        steps = []
        for i in range(min(step_count, len(relevant_templates))):
            template = relevant_templates[i]
            
            # Start with the template
            step = {
                "number": i + 1,
                "description": template["description"],
                "time": template.get("time", 15),
                "priority": template.get("priority", "Medium"),
                "adhd_tip": template.get("adhd_tip", self._generate_adhd_tip())
            }
            
            # Try to enhance with language model if available
            if self.text_generator:
                try:
                    # Create a prompt for enhancing the step description
                    prompt = f"Task: {task_description}\n\nOriginal step: {template['description']}\n\n"
                    prompt += "Create a more personalized and specific version of this step for the task."
                    
                    generated = self.text_generator(prompt, max_length=150)[0]["generated_text"]
                    
                    # Extract just the generated part
                    if self.is_seq2seq:
                        enhanced_description = generated
                    else:
                        if "Create a more personalized" in generated:
                            parts = generated.split("Create a more personalized")
                            enhanced_description = parts[1].strip() if len(parts) > 1 else generated
                        else:
                            enhanced_description = generated
                    
                    # Use the generated text if it's reasonable
                    if enhanced_description and len(enhanced_description) > 10 and len(enhanced_description) < 200:
                        step["description"] = enhanced_description
                        
                    # Generate personalized ADHD tip
                    adhd_prompt = f"Create a helpful ADHD-friendly tip for this task step: {step['description']}"
                    adhd_generated = self.text_generator(adhd_prompt, max_length=100)[0]["generated_text"]
                    
                    if adhd_generated and "tip" in adhd_generated.lower():
                        # Try to extract just the tip part
                        if ":" in adhd_generated:
                            adhd_generated = adhd_generated.split(":", 1)[1].strip()
                        step["adhd_tip"] = adhd_generated
                except Exception as e:
                    logger.error(f"Error enhancing step with language model: {str(e)}")
            
            steps.append(step)
        
        # If we need more steps than we have templates, generate additional ones
        if len(steps) < step_count and self.text_generator:
            try:
                for i in range(len(steps), step_count):
                    prompt = f"Task: {task_description}\n\n"
                    prompt += f"Generate step {i+1} of {step_count} for breaking down this task. "
                    prompt += "The step should be specific, actionable, and about 15-20 words."
                    
                    generated = self.text_generator(prompt, max_length=100)[0]["generated_text"]
                    
                    # Extract the generated step
                    if self.is_seq2seq:
                        step_text = generated
                    else:
                        if "step should be" in generated.lower():
                            parts = generated.lower().split("step should be")
                            step_text = parts[1].strip() if len(parts) > 1 else generated
                        else:
                            step_text = generated
                    
                    if not step_text or len(step_text) < 10:
                        step_text = f"Review your progress and plan next steps for {task_description}"
                    
                    step = {
                        "number": i + 1,
                        "description": step_text,
                        "time": random.choice([10, 15, 20, 25, 30]),
                        "priority": random.choice(["High", "Medium", "Medium", "Low"]),
                        "adhd_tip": self._generate_adhd_tip()
                    }
                    steps.append(step)
            except Exception as e:
                logger.error(f"Error generating additional steps: {str(e)}")
        
        # Ensure we have exactly the right number of steps
        while len(steps) < step_count:
            # Add generic steps if needed
            generic_step = {
                "number": len(steps) + 1,
                "description": f"Review progress and plan next actions for {task_description}",
                "time": 15,
                "priority": "Medium",
                "adhd_tip": self._generate_adhd_tip()
            }
            steps.append(generic_step)
        
        # Limit to the requested step count
        return steps[:step_count]
    
    def _generate_adhd_tip(self) -> str:
        """Generate an ADHD-friendly tip for task steps."""
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
    
    def _generate_reward_suggestion(self, task_description: str) -> str:
        """Generate a personalized reward suggestion."""
        if self.text_generator:
            try:
                prompt = f"Suggest a small, specific reward for completing this task: {task_description}"
                generated = self.text_generator(prompt, max_length=100)[0]["generated_text"]
                
                # Extract just the reward part
                if ":" in generated:
                    generated = generated.split(":", 1)[1].strip()
                
                if generated and len(generated) > 10 and len(generated) < 150:
                    return generated
            except Exception as e:
                logger.error(f"Error generating reward suggestion: {str(e)}")
        
        # Fallback to predefined rewards
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
    """
    Task Breakdown class that leverages RAG capabilities when available.
    This maintains backward compatibility with the existing application.
    """
    
    def __init__(self, detail_level: str = "standard"):
        self.detail_level = detail_level
        self.rag_breakdown = RAGTaskBreakdown(detail_level)
        
    def get_step_count(self) -> int:
        return self.rag_breakdown.get_step_count()

    def break_task(self, task_description: str, detail_level: Optional[str] = None) -> Dict[str, Any]:
        return self.rag_breakdown.break_task(task_description, detail_level)
    

def break_down_task(task_description: str) -> List[str]:
    """
    Legacy function to break down a task into steps.
    
    Args:
        task_description: The task to break down
        
    Returns:
        List of step descriptions
    """
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


def break_task(task_description: str) -> List[str]:
    """
    Enhanced function for task breakdown, with RAG when available.
    Falls back to basic functionality when advanced models aren't available.
    
    Args:
        task_description: The task to break down
        
    Returns:
        List of step descriptions
    """
    if ADVANCED_MODELS_AVAILABLE:
        try:
            task_breaker = TaskBreakdown()
            result = task_breaker.break_task(task_description)
            return [step["description"] for step in result["steps"]]
        except Exception as e:
            logger.error(f"Error using enhanced task breakdown: {str(e)}")
            logger.info("Falling back to basic task breakdown")
            return break_down_task(task_description)
    else:
        return break_down_task(task_description)