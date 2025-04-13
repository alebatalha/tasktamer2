def get_task_steps(task_type: str):
    task_templates = {
        "academic_writing": [
            {
                "description": "Brainstorm 2-3 specific aspects of your topic that interest you most. Just jot down ideas - don't judge them yet!",
                "time": 10,
                "priority": "High",
                "adhd_tip": "Use a colorful mind map to make brainstorming more visual and engaging.",
                "sub_steps": [
                    "Set a 5-minute timer and write down everything that comes to mind about the topic",
                    "Take a 2-minute break to stand up and stretch",
                    "Spend 3 minutes circling the ideas that most interest you"
                ]
            },
            {
                "description": "Choose ONE specific focus for your paper and write it down as a single sentence.",
                "time": 5,
                "priority": "High",
                "adhd_tip": "Stand up while making this decision to engage your body and mind.",
                "sub_steps": [
                    "Review your brainstorming ideas",
                    "Eliminate topics that seem too broad",
                    "Write your chosen focus as a clear statement"
                ]
            },
            {
                "description": "Find 3-5 credible sources on your topic. Just save the links for now - don't read the full texts yet!",
                "time": 15,
                "priority": "Medium",
                "adhd_tip": "Use the Pomodoro technique - set a 15-minute timer to create urgency and focus.",
                "sub_steps": [
                    "Open Google Scholar or your library database",
                    "Search using keywords from your focus statement",
                    "Scan titles and abstracts for relevance",
                    "Save promising sources to a document or citation manager"
                ]
            },
            {
                "description": "Create a simple outline with 3 main points that support your focus. Just bullet points - don't write full sentences yet.",
                "time": 10,
                "priority": "High",
                "adhd_tip": "Use different colored pens for each main point to make the outline visually stimulating.",
                "sub_steps": [
                    "Review the titles and abstracts of your sources",
                    "Identify 3 key arguments or themes that emerge",
                    "Arrange these in a logical order"
                ]
            },
            {
                "description": "Take focused notes from ONE source, looking specifically for evidence supporting your first main point.",
                "time": 20,
                "priority": "Medium",
                "adhd_tip": "Use the highlighting technique: yellow for main ideas, blue for evidence, pink for questions.",
                "sub_steps": [
                    "Choose your most promising source",
                    "Skim the source to locate relevant sections",
                    "Take bullet point notes on supporting evidence",
                    "Record the citation information"
                ]
            },
            {
                "description": "Write a rough draft of your introduction paragraph (just 3-5 sentences).",
                "time": 15,
                "priority": "Medium",
                "adhd_tip": "Speak your thoughts out loud before writing them down to clarify your ideas.",
                "sub_steps": [
                    "Start with an interesting hook or question",
                    "Provide brief context for your topic",
                    "End with your thesis statement (main argument)"
                ]
            },
            {
                "description": "Draft your first body paragraph using the notes from your first source.",
                "time": 20,
                "priority": "Medium",
                "adhd_tip": "Use speech-to-text if typing feels challenging - sometimes talking is easier than writing.",
                "sub_steps": [
                    "Start with a topic sentence that states your first main point",
                    "Add evidence from your source",
                    "Explain how this evidence supports your thesis",
                    "Add a transition sentence to the next paragraph"
                ]
            },
            {
                "description": "Take a bigger break (15-30 minutes) to recharge your brain before continuing with the next sections.",
                "time": 15,
                "priority": "High",
                "adhd_tip": "Physical movement during breaks helps reset your focus - try a short walk or stretch routine.",
                "sub_steps": [
                    "Set a timer for your break",
                    "Move away from your workspace",
                    "Do something physically active if possible",
                    "Hydrate and have a small snack if needed"
                ]
            },
            {
                "description": "Gather evidence for your second main point from another source using the same focused note-taking approach.",
                "time": 20,
                "priority": "Medium",
                "adhd_tip": "Change your environment slightly to maintain engagement - move to a different seat or area.",
                "sub_steps": [
                    "Select your second source",
                    "Take focused notes on evidence for your second point",
                    "Organize the information in a clear structure"
                ]
            },
            {
                "description": "Draft your second body paragraph using your notes.",
                "time": 20,
                "priority": "Medium",
                "adhd_tip": "Use a fidget tool to help maintain focus while writing.",
                "sub_steps": [
                    "Write a clear topic sentence for your second point",
                    "Include the evidence you gathered",
                    "Explain the significance of this evidence",
                    "Add a transition to the next section"
                ]
            },
            {
                "description": "Repeat the process for your third main point: gather evidence and draft the paragraph.",
                "time": 40,
                "priority": "Medium",
                "adhd_tip": "Break this bigger task into two 20-minute sessions with a 5-minute break between.",
                "sub_steps": [
                    "Find evidence for your third point",
                    "Take a short break",
                    "Write your third body paragraph"
                ]
            },
            {
                "description": "Write a brief conclusion that restates your main points and thesis (3-4 sentences).",
                "time": 15,
                "priority": "Medium",
                "adhd_tip": "Try the 'backward' technique: read your introduction, then each topic sentence, to remind yourself what to conclude.",
                "sub_steps": [
                    "Restate your thesis in different words",
                    "Briefly summarize your main points",
                    "End with a thought-provoking statement or call to action"
                ]
            },
            {
                "description": "Take a long break (at least a few hours or overnight) before reviewing your draft.",
                "time": 0,
                "priority": "High",
                "adhd_tip": "Distance from your writing helps you return with fresh eyes for better editing.",
                "sub_steps": [
                    "Save your document with proper backup",
                    "Set a specific time to return to it",
                    "Do something completely different in between"
                ]
            },
            {
                "description": "Review your draft for content and organization. Make notes on what to improve, but don't edit yet.",
                "time": 20,
                "priority": "Medium",
                "adhd_tip": "Read your paper out loud - this activates different parts of your brain and helps catch issues.",
                "sub_steps": [
                    "Check if your thesis is clear",
                    "Verify that each paragraph supports your thesis",
                    "Ensure your points flow logically",
                    "Make notes on areas to improve"
                ]
            },
            {
                "description": "Edit your paper for clarity and coherence, focusing on one paragraph at a time.",
                "time": 30,
                "priority": "Medium",
                "adhd_tip": "Edit on paper if possible - the physical interaction can help maintain focus.",
                "sub_steps": [
                    "Strengthen your introduction and conclusion",
                    "Improve topic sentences and transitions",
                    "Clarify any confusing explanations",
                    "Make sure evidence clearly supports your claims"
                ]
            },
            {
                "description": "Proofread for grammar, spelling, punctuation, and citation format.",
                "time": 20,
                "priority": "Low",
                "adhd_tip": "Use a text-to-speech reader to hear errors you might miss when reading.",
                "sub_steps": [
                    "Check spelling and grammar using tools",
                    "Verify citation format using a guide",
                    "Read backward (last sentence to first) to catch errors",
                    "Check for consistent formatting"
                ]
            }
        ],
        
        "presentation": [
            {
                "description": "Define your presentation topic and 1-2 specific goals you want to achieve.",
                "time": 10,
                "priority": "High",
                "adhd_tip": "Write your goals on a sticky note and keep it visible during the entire presentation creation process.",
                "sub_steps": [
                    "Clarify what you want the audience to learn",
                    "Consider what action you want the audience to take",
                    "Write these down as specific, measurable objectives"
                ]
            },
            {
                "description": "Identify your audience and list 3 things they care about related to your topic.",
                "time": 10,
                "priority": "High",
                "adhd_tip": "Create a quick mind map of your audience's interests and needs.",
                "sub_steps": [
                    "Define who will be in your audience",
                    "Consider their existing knowledge level",
                    "Think about what problems or questions they have"
                ]
            },
            {
                "description": "Brainstorm your 3 most important points that support your presentation goals.",
                "time": 15,
                "priority": "High",
                "adhd_tip": "Use colorful sticky notes - one color for each main point and its supporting details.",
                "sub_steps": [
                    "Focus on quality over quantity",
                    "Think about logical flow between points",
                    "Make sure points align with audience needs"
                ]
            },
            {
                "description": "Gather evidence, examples, or stories for each of your main points.",
                "time": 20,
                "priority": "Medium",
                "adhd_tip": "Set a timer for 6-7 minutes per point to maintain focus and create urgency.",
                "sub_steps": [
                    "Find statistics or data to support your points",
                    "Think of personal stories or examples",
                    "Look for visual evidence you could include"
                ]
            },
            {
                "description": "Create a simple outline with an intro, your 3 main points, and a conclusion.",
                "time": 15,
                "priority": "High",
                "adhd_tip": "Physically arrange your notes or sticky notes in sequence to visualize the flow.",
                "sub_steps": [
                    "Plan an engaging opening hook",
                    "Outline your three main points",
                    "Plan how you'll conclude and what action you'll request"
                ]
            },
            {
                "description": "Design your first 3 slides: title slide and intro slides that hook your audience.",
                "time": 15,
                "priority": "Medium",
                "adhd_tip": "Find inspirational slide designs before starting to get creative ideas flowing.",
                "sub_steps": [
                    "Create a clear, simple title slide",
                    "Design an attention-grabbing second slide",
                    "Create a slide that previews your main points"
                ]
            },
            {
                "description": "Create slides for your first main point (2-3 slides maximum for this section).",
                "time": 15,
                "priority": "Medium",
                "adhd_tip": "Use the 5/5/5 rule: no more than 5 words per line, 5 lines per slide, 5 text-heavy slides in a row.",
                "sub_steps": [
                    "Make one slide with the main point clearly stated",
                    "Create supporting slides with evidence or examples",
                    "Include relevant visuals to enhance understanding"
                ]
            },
            {
                "description": "Take a 5-minute movement break.",
                "time": 5,
                "priority": "Medium",
                "adhd_tip": "Stand up, stretch, or take a quick walk to refresh your brain and body.",
                "sub_steps": [
                    "Set a timer for exactly 5 minutes",
                    "Move away from your workspace",
                    "Do some physical movement to re-energize"
                ]
            },
            {
                "description": "Create slides for your second main point (2-3 slides).",
                "time": 15,
                "priority": "Medium",
                "adhd_tip": "Challenge yourself to make these slides different from the first set to maintain interest.",
                "sub_steps": [
                    "Create a slide stating your second main point",
                    "Add supporting evidence or examples",
                    "Include relevant visuals or diagrams"
                ]
            },
            {
                "description": "Create slides for your third main point (2-3 slides).",
                "time": 15,
                "priority": "Medium",
                "adhd_tip": "Use a visual timer on your desk to maintain awareness of time spent on this section.",
                "sub_steps": [
                    "Make a slide with your third main point clearly stated",
                    "Create supporting slides with evidence",
                    "Ensure visuals are consistent with your overall design"
                ]
            },
            {
                "description": "Design your conclusion slides (1-2) with a clear call to action.",
                "time": 10,
                "priority": "High",
                "adhd_tip": "Make your call to action bold, specific, and visually prominent.",
                "sub_steps": [
                    "Create a summary slide of your main points",
                    "Design a slide with your call to action",
                    "Include your contact information if appropriate"
                ]
            },
            {
                "description": "Review all slides for visual consistency and simplicity.",
                "time": 15,
                "priority": "Medium",
                "adhd_tip": "View slides in presentation mode to see them from the audience perspective.",
                "sub_steps": [
                    "Check for consistent fonts and colors",
                    "Ensure text is large enough to read",
                    "Reduce clutter and unnecessary elements",
                    "Verify that visuals support rather than distract"
                ]
            },
            {
                "description": "Practice your presentation out loud, focusing on smooth transitions between points.",
                "time": 20,
                "priority": "High",
                "adhd_tip": "Record yourself on your phone to review later, but don't stop to critique during practice.",
                "sub_steps": [
                    "Time your presentation to ensure it fits the allocated time",
                    "Practice transitioning between slides",
                    "Identify any points where you get stuck"
                ]
            },
            {
                "description": "Write brief speaker notes for each slide (just bullet points).",
                "time": 15,
                "priority": "Medium",
                "adhd_tip": "Keep speaker notes extremely brief - just cues, not full sentences to read.",
                "sub_steps": [
                    "Note key facts you want to mention",
                    "Write transition phrases between slides",
                    "Highlight areas where you'll interact with the audience"
                ]
            },
            {
                "description": "Practice your full presentation again, with a focus on engagement and energy.",
                "time": 20,
                "priority": "High",
                "adhd_tip": "Practice in the same position you'll present in (standing if you'll be standing, etc.).",
                "sub_steps": [
                    "Focus on your opening and closing for maximum impact",
                    "Practice any technical demonstrations",
                    "Work on varying your tone and pacing"
                ]
            }
        ],
        
        "project_management": [
            {
                "description": "Define your project's primary goal in one clear sentence.",
                "time": 10,
                "priority": "High",
                "adhd_tip": "Write this goal statement on a brightly colored card and keep it visible throughout the project.",
                "sub_steps": [
                    "Identify what success looks like for this project",
                    "Make the goal specific and measurable",
                    "Ensure the goal is realistically achievable"
                ]
            },
            {
                "description": "List the 3-5 major deliverables required to achieve your goal.",
                "time": 15,
                "priority": "High",
                "adhd_tip": "Use a mind map to visually connect deliverables to your main goal.",
                "sub_steps": [
                    "Brainstorm all possible outputs from the project",
                    "Group similar items together",
                    "Prioritize the most critical deliverables"
                ]
            },
            {
                "description": "Create a list of stakeholders who need to be involved or informed.",
                "time": 10,
                "priority": "Medium",
                "adhd_tip": "Categorize stakeholders visually (decision-makers, team members, external partners).",
                "sub_steps": [
                    "Identify who needs to approve project elements",
                    "List who will be doing the work",
                    "Note who needs to be kept informed"
                ]
            },
            {
                "description": "Break down your first major deliverable into 3-5 specific tasks.",
                "time": 15,
                "priority": "High",
                "adhd_tip": "Use the 'begin with the end in mind' technique - visualize the completed deliverable, then work backwards.",
                "sub_steps": [
                    "Start with the final result of this deliverable",
                    "Identify the major steps needed to create it",
                    "Make each task specific and actionable"
                ]
            },
            {
                "description": "Repeat the task breakdown process for each remaining deliverable.",
                "time": 30,
                "priority": "High",
                "adhd_tip": "Take a 2-minute movement break between each deliverable to maintain focus and energy.",
                "sub_steps": [
                    "Focus on one deliverable at a time",
                    "Create specific, action-oriented tasks",
                    "Take short breaks between deliverables"
                ]
            },
            {
                "description": "Estimate time required for each task and identify any dependencies.",
                "time": 20,
                "priority": "Medium",
                "adhd_tip": "Use a timer when estimating - spend no more than 1-2 minutes per task to avoid perfectionism.",
                "sub_steps": [
                    "Make a best guess at how long each task will take",
                    "Add a 25% buffer for unexpected challenges",
                    "Note which tasks must happen before others can start"
                ]
            },
            {
                "description": "Create a simple project timeline with key milestones and deadlines.",
                "time": 20,
                "priority": "High",
                "adhd_tip": "Use a visual timeline tool or a colorful hand-drawn timeline to make it engaging.",
                "sub_steps": [
                    "Start with the final deadline and work backwards",
                    "Place milestones at completion points for deliverables",
                    "Mark dependencies between tasks"
                ]
            },
            {
                "description": "Identify the resources you'll need for the project (people, tools, budget, etc.).",
                "time": 15,
                "priority": "Medium",
                "adhd_tip": "Create a visual checklist with categories for different resource types.",
                "sub_steps": [
                    "List the people needed and their required skills",
                    "Identify tools or software required",
                    "Estimate budget needed for each deliverable"
                ]
            },
            {
                "description": "Assign responsibilities for specific tasks to team members (or to time blocks if working solo).",
                "time": 15,
                "priority": "Medium",
                "adhd_tip": "Use a responsibility assignment matrix (RACI chart) to clarify roles.",
                "sub_steps": [
                    "Match tasks to people with appropriate skills",
                    "Consider workload balance across the team",
                    "If solo, assign tasks to specific days/times"
                ]
            },
            {
                "description": "Identify potential risks or obstacles and create simple contingency plans.",
                "time": 15,
                "priority": "Medium",
                "adhd_tip": "Use the 'What could go wrong?' game - make it playful rather than anxiety-inducing.",
                "sub_steps": [
                    "Brainstorm possible challenges or roadblocks",
                    "Rate each risk by likelihood and impact",
                    "Create brief contingency plans for high-priority risks"
                ]
            },
            {
                "description": "Set up a simple progress tracking system (could be a shared doc, project board, etc.).",
                "time": 20,
                "priority": "High",
                "adhd_tip": "Choose a visually engaging tracking method with clear progress indicators.",
                "sub_steps": [
                    "Select a tool that works for your team",
                    "Set up categories for 'To Do', 'In Progress', and 'Done'",
                    "Add major tasks and assign owners"
                ]
            },
            {
                "description": "Schedule a project kickoff meeting or personal project launch session.",
                "time": 15,
                "priority": "Medium",
                "adhd_tip": "Create a visual agenda with specific timeboxes for each topic to keep the meeting focused.",
                "sub_steps": [
                    "Prepare a brief presentation of the project plan",
                    "Create an engaging activity to build excitement",
                    "Prepare specific questions to address concerns"
                ]
            },
            {
                "description": "Set up regular check-in points throughout the project timeline.",
                "time": 10,
                "priority": "Medium",
                "adhd_tip": "Add check-ins to your calendar with specific focus points for each one.",
                "sub_steps": [
                    "Schedule brief weekly progress reviews",
                    "Set milestone review points after major deliverables",
                    "Create reminders with specific questions to assess progress"
                ]
            }
        ],
        
        "marketing": [
            {
                "description": "Define your campaign goal with a specific, measurable outcome.",
                "time": 10,
                "priority": "High",
                "adhd_tip": "Create a visual reminder of your goal with metrics clearly displayed.",
                "sub_steps": [
                    "Identify what specific action you want people to take",
                    "Determine how you'll measure success",
                    "Set a numeric target for your campaign"
                ]
            },
            {
                "description": "Create a specific profile of your target audience (demographics, interests, pain points).",
                "time": 15,
                "priority": "High",
                "adhd_tip": "Find or create a visual representation of your ideal customer to make them feel real.",
                "sub_steps": [
                    "Define demographic characteristics",
                    "List their key interests and values",
                    "Identify their main problems or desires"
                ]
            },
            {
                "description": "Craft your core message in one clear, compelling sentence.",
                "time": 15,
                "priority": "High",
                "adhd_tip": "Try the voice memo technique - record yourself explaining the value naturally, then refine it.",
                "sub_steps": [
                    "Focus on the main benefit for your audience",
                    "Make it memorable and distinctive",
                    "Ensure it aligns with your brand voice"
                ]
            },
            {
                "description": "Select 2-3 primary marketing channels based on where your audience spends time.",
                "time": 10,
                "priority": "Medium",
                "adhd_tip": "Use a decision matrix to compare channels objectively rather than going with gut instinct.",
                "sub_steps": [
                    "List channels your audience uses most",
                    "Consider your budget and resources",
                    "Evaluate past performance on different channels"
                ]
            },
            {
                "description": "Create a basic content calendar with specific types of content for each channel.",
                "time": 20,
                "priority": "Medium",
                "adhd_tip": "Use a visual calendar with color coding for different content types.",
                "sub_steps": [
                    "Decide on frequency for each channel",
                    "Map out content themes or topics",
                    "Identify any timely or seasonal content needs"
                ]
            },
            {
                "description": "Develop your first piece of content (social post, email, blog, etc.).",
                "time": 30,
                "priority": "Medium",
                "adhd_tip": "Use a content creation template to provide structure and reduce decision fatigue.",
                "sub_steps": [
                    "Create an attention-grabbing headline",
                    "Draft the main content",
                    "Add a clear call to action"
                ]
            },
            {
                "description": "Take a break and come back to review your content with fresh eyes.",
                "time": 15,
                "priority": "Low",
                "adhd_tip": "Do something completely different during this break to fully switch contexts.",
                "sub_steps": [
                    "Step away from your workspace",
                    "Do a physical activity to reset your focus",
                    "Return with a critical eye for improvements"
                ]
            },
            {
                "description": "Identify or create visual elements for your campaign (images, graphics, videos).",
                "time": 25,
                "priority": "Medium",
                "adhd_tip": "Create a mood board first to guide your visual choices and maintain consistency.",
                "sub_steps": [
                    "Determine what visuals you need for each channel",
                    "Decide whether to create or source visuals",
                    "Ensure visuals align with your brand and message"
                ]
            },
            {
                "description": "Set up tracking for your campaign metrics (clicks, conversions, etc.).",
                "time": 20,
                "priority": "Medium",
                "adhd_tip": "Create a simple dashboard that will make checking metrics a rewarding experience.",
                "sub_steps": [
                    "Determine which metrics align with your goals",
                    "Set up tracking tools or analytics",
                    "Create a simple template for regular reporting"
                ]
            },
            {
                "description": "Prepare your launch schedule with specific dates and responsible individuals.",
                "time": 15,
                "priority": "High",
                "adhd_tip": "Use time blocking in your calendar for each launch task to make them feel concrete.",
                "sub_steps": [
                    "Create a detailed timeline for launch activities",
                    "Assign specific responsibilities",
                    "Build in buffer time for unexpected issues"
                ]
            },
            {
                "description": "Create a simple plan for testing and optimizing during the campaign.",
                "time": 15,
                "priority": "Medium",
                "adhd_tip": "Schedule specific 'optimization sessions' to make this an explicit part of your process.",
                "sub_steps": [
                    "Identify elements to test (headlines, images, CTAs)",
                    "Determine when you'll review performance",
                    "Set thresholds for when to make changes"
                ]
            },
            {
                "description": "Prepare a communication brief for everyone involved in the campaign.",
                "time": 20,
                "priority": "Medium",
                "adhd_tip": "Create a visual one-pager that captures all essential information at a glance.",
                "sub_steps": [
                    "Summarize the goal, audience, and key message",
                    "Include the content calendar and responsibilities",
                    "Add tracking information and success metrics"
                ]
            }
        ],
        
        "web_design":  [
            {
                "description": "Define the primary purpose of the website and its main target audience.",
                "time": 15,
                "priority": "High",
                "adhd_tip": "Create a visual mission statement for the website to keep you focused on its purpose.",
                "sub_steps": [
                    "Identify the main action you want visitors to take",
                    "Define who the website is primarily for",
                    "List the key problems the website will solve for users"
                ]
            },
            {
                "description": "List the essential pages needed (Home, About, Services, Contact, etc.).",
                "time": 10,
                "priority": "High",
                "adhd_tip": "Use sticky notes to represent each page - this makes it easy to arrange them in different orders.",
                "sub_steps": [
                    "Start with the absolutely necessary pages",
                    "Consider adding specialized pages for key services/products",
                    "Decide if you need a blog or resources section"
                ]
            },
            {
                "description": "Sketch a simple site structure showing how pages connect to each other.",
                "time": 15,
                "priority": "Medium",
                "adhd_tip": "Draw this by hand - the physical activity helps engage your brain differently than typing.",
                "sub_steps": [
                    "Draw your home page at the top",
                    "Connect it to main navigation pages",
                    "Add sub-pages where needed",
                    "Draw lines showing how users might move between pages"
                ]
            },
            {
                "description": "Collect examples of websites you like for inspiration (take screenshots or save links).",
                "time": 20,
                "priority": "Medium",
                "adhd_tip": "Set a timer for this task - it's easy to fall down a rabbit hole of endless browsing.",
                "sub_steps": [
                    "Find 3-5 websites in your industry",
                    "Look for 2-3 websites with features you like",
                    "Note specific elements that appeal to you"
                ]
            },
            {
                "description": "Choose a color scheme and typography that matches your brand.",
                "time": 15,
                "priority": "Medium",
                "adhd_tip": "Use a color palette generator to make this process more visual and engaging.",
                "sub_steps": [
                    "Select 2-3 primary colors that reflect your brand",
                    "Add 1-2 accent colors for contrast",
                    "Choose no more than 2 font families"
                ]
            },
            {
                "description": "Sketch or wireframe your home page layout.",
                "time": 25,
                "priority": "High",
                "adhd_tip": "Use a template or grid paper to provide structure and reduce the blank page effect.",
                "sub_steps": [
                    "Outline the header area with navigation",
                    "Sketch the hero section with main message",
                    "Add content blocks for key information",
                    "Include a footer with essential links"
                ]
            },
            {
                "description": "Create a content list for your home page (headlines, text, images needed).",
                "time": 15,
                "priority": "High",
                "adhd_tip": "Use a checklist format to make content gathering feel like a game with clear wins.",
                "sub_steps": [
                    "Write the main headline and subheadline",
                    "List key messages for each section",
                    "Identify what images will be needed",
                    "Draft your call-to-action text"
                ]
            },
            {
                "description": "Take a short break to refresh your focus.",
                "time": 10,
                "priority": "Medium",
                "adhd_tip": "Do a completely different activity, preferably something physical, to give your creative mind a rest.",
                "sub_steps": [
                    "Step away from your computer",
                    "Do a quick physical activity",
                    "Return with fresh perspective"
                ]
            },
            {
                "description": "Wireframe one key inner page (About, Services, or Product page).",
                "time": 20,
                "priority": "Medium",
                "adhd_tip": "Look at your examples for inspiration but set them aside when actually drawing to avoid copying.",
                "sub_steps": [
                    "Sketch the page layout",
                    "Include areas for all key content",
                    "Consider user flow and calls to action"
                ]
            },
            {
                "description": "List the content needed for this inner page.",
                "time": 15,
                "priority": "Medium",
                "adhd_tip": "If writing feels challenging, try recording yourself talking about the content, then transcribe it.",
                "sub_steps": [
                    "Draft headlines and subheadings",
                    "List key points to cover",
                    "Note any testimonials or examples to include",
                    "Identify image needs"
                ]
            },
            {
                "description": "Choose a website platform or technology to build with (WordPress, Squarespace, etc.).",
                "time": 15,
                "priority": "High",
                "adhd_tip": "Create a pros/cons list for each option to make this decision more concrete.",
                "sub_steps": [
                    "Consider your technical skill level",
                    "Think about maintenance requirements",
                    "Evaluate cost and flexibility needs",
                    "Research good templates for your needs"
                ]
            },
            {
                "description": "Create a development plan with timeline for building the site.",
                "time": 20,
                "priority": "Medium",
                "adhd_tip": "Break the development into very small chunks that can each be completed in under an hour.",
                "sub_steps": [
                    "List all pages to be created",
                    "Estimate time needed for each component",
                    "Create a sequence for development",
                    "Set milestone dates for checking progress"
                ]
            },
            {
                "description": "Set up your development environment or platform account.",
                "time": 30,
                "priority": "High",
                "adhd_tip": "Eliminate distractions before starting this technical task - close other tabs and notifications.",
                "sub_steps": [
                    "Create necessary accounts",
                    "Install required software",
                    "Set up domain and hosting if needed",
                    "Install a basic theme or template"
                ]
            }
        ],
        
        "event_planning": [
            {
                "description": "Define the event purpose and 1-3 specific goals you want to achieve.",
                "time": 15,
                "priority": "High",
                "adhd_tip": "Create a visual 'event mission statement' to keep visible throughout planning.",
                "sub_steps": [
                    "Identify why you're hosting this event",
                    "Determine what success looks like",
                    "Set specific, measurable objectives"
                ]
            },
            {
                "description": "Create a profile of your target attendees (who they are, why they'd attend).",
                "time": 15,
                "priority": "High",
                "adhd_tip": "Find or create images representing your ideal attendees to make them feel real.",
                "sub_steps": [
                    "Define demographics of target attendees",
                    "Identify their interests and needs",
                    "Consider what would motivate them to attend"
                ]
            },
            {
                "description": "Determine date, time, and duration based on your audience and goals.",
                "time": 10,
                "priority": "High",
                "adhd_tip": "Check multiple calendars for conflicts before deciding - personal, community, industry, holidays.",
                "sub_steps": [
                    "Consider your audience's availability",
                    "Check for competing events or holidays",
                    "Think about ideal duration for your content"
                ]
            },
            {
                "description": "Set a budget with categories (venue, food, speakers, materials, etc.).",
                "time": 20,
                "priority": "High",
                "adhd_tip": "Use a budgeting template to ensure you don't miss common expense categories.",
                "sub_steps": [
                    "List all potential expense categories",
                    "Research average costs for each category",
                    "Allocate funds based on priorities",
                    "Include a contingency buffer (10-15%)"
                ]
            },
            {
                "description": "Research and list 3-5 potential venues that fit your requirements.",
                "time": 30,
                "priority": "High",
                "adhd_tip": "Create a venue comparison chart with your must-have features to make evaluation easier.",
                "sub_steps": [
                    "Determine capacity and layout needs",
                    "Consider location and accessibility",
                    "Check availability for your dates",
                    "Gather pricing and policies"
                ]
            },
            {
                "description": "Create an event agenda or schedule with time blocks.",
                "time": 20,
                "priority": "High",
                "adhd_tip": "Use sticky notes or a digital tool that lets you easily move agenda items around.",
                "sub_steps": [
                    "Start with arrival and end times",
                    "Block out main activities or presentations",
                    "Include breaks and transition times",
                    "Consider attention spans when planning session lengths"
                ]
            },
            {
                "description": "Identify speakers, presenters, or entertainment needed.",
                "time": 15,
                "priority": "Medium",
                "adhd_tip": "Create a speaker wishlist, starting with people you already know who would be great.",
                "sub_steps": [
                    "List required topics to be covered",
                    "Identify potential speakers for each topic",
                    "Consider backup options",
                    "Note any speaker requirements or fees"
                ]
            },
            {
                "description": "Plan catering, refreshments, or food arrangements.",
                "time": 20,
                "priority": "Medium",
                "adhd_tip": "Create a visual menu board to make this task more engaging.",
                "sub_steps": [
                    "Decide what meals or snacks to offer",
                    "Consider dietary restrictions and preferences",
                    "Research catering options and costs",
                    "Plan timing for food service"
                ]
            },
            {
                "description": "Create a marketing and invitation plan to reach your target attendees.",
                "time": 25,
                "priority": "High",
                "adhd_tip": "Create a countdown calendar for marketing tasks to add urgency and structure.",
                "sub_steps": [
                    "Decide on invitation methods (email, social, printed)",
                    "Create a compelling event description",
                    "Plan announcement and reminder schedule",
                    "Design any needed graphics or materials"
                ]
            },
            {
                "description": "Set up a registration system to track attendees.",
                "time": 20,
                "priority": "High",
                "adhd_tip": "Choose a registration tool that sends you notifications for new signups to provide dopamine hits.",
                "sub_steps": [
                    "Select a registration platform or method",
                    "Create the registration form",
                    "Set up confirmation emails",
                    "Test the registration process"
                ]
            },
            {
                "description": "Make a detailed logistics checklist for event day.",
                "time": 20,
                "priority": "Medium",
                "adhd_tip": "Create a visual timeline for event day with clear task assignments.",
                "sub_steps": [
                    "Plan setup and teardown times",
                    "List all equipment and supplies needed",
                    "Create staff or volunteer schedule",
                    "Include emergency contact information"
                ]
            },
            {
                "description": "Develop a communication plan for before, during, and after the event.",
                "time": 15,
                "priority": "Medium",
                "adhd_tip": "Draft email and announcement templates in advance so they're ready to use.",
                "sub_steps": [
                    "Create pre-event communication schedule",
                    "Plan day-of announcements or communications",
                    "Prepare post-event thank you and follow-up messages",
                    "Assign communication responsibilities"
                ]
            }
        ],
        
        "studying": [
            {
                "description": "Break down your subject into 3-5 main topics or sections to study.",
                "time": 10,
                "priority": "High",
                "adhd_tip": "Create a colorful mind map of the subject with main topics as branches.",
                "sub_steps": [
                    "Review the syllabus or table of contents",
                    "Identify major themes or concepts",
                    "Organize topics in a logical sequence"
                ]
            },
            {
                "description": "Gather all necessary study materials for your first topic.",
                "time": 10,
                "priority": "High",
                "adhd_tip": "Create a 'study station' with everything you need within reach to minimize disruptions.",
                "sub_steps": [
                    "Collect relevant textbooks or readings",
                    "Gather your notes and handouts",
                    "Prepare blank paper or digital files for new notes",
                    "Get any tools you need (calculator, highlighters, etc.)"
                ]
            },
            {
                "description": "Set a specific learning goal for your first study session.",
                "time": 5,
                "priority": "Medium",
                "adhd_tip": "Write your goal on a sticky note and place it where you can see it during your study session.",
                "sub_steps": [
                    "Be specific about what you want to learn",
                    "Make the goal challenging but achievable",
                    "Phrase it in terms of what you'll be able to do"
                ]
            },
            {
                "description": "Create a retrieval practice plan with questions on your first topic.",
                "time": 15,
                "priority": "High",
                "adhd_tip": "Turn this into a game by creating flashcards or a quiz for yourself.",
                "sub_steps": [
                    "Review your material briefly",
                    "Write 5-10 questions about key concepts",
                    "Include different types of questions (multiple choice, short answer, etc.)",
                    "Set aside the questions for later practice"
                ]
            },
            {
                "description": "Study your first topic using active techniques (not just re-reading).",
                "time": 25,
                "priority": "High",
                "adhd_tip": "Use the 'teach it' method - explain concepts out loud as if teaching someone else.",
                "sub_steps": [
                    "Actively engage with the material (highlight, take notes, draw diagrams)",
                    "Create connections to things you already know",
                    "Break down complex ideas into simpler components",
                    "Focus on understanding rather than memorizing"
                ]
            },
            {
                "description": "Take a 5-minute movement break.",
                "time": 5,
                "priority": "Medium",
                "adhd_tip": "Set a specific timer and do a physical activity that gets your blood flowing.",
                "sub_steps": [
                    "Stand up and move away from your study area",
                    "Do a quick physical activity (jumping jacks, quick walk, stretch)",
                    "Get a drink of water",
                    "Return refreshed when the timer goes off"
                ]
            },
            {
                "description": "Test yourself on the material you just studied using your questions.",
                "time": 15,
                "priority": "High",
                "adhd_tip": "Use different colored pens for questions and answers to make the process more stimulating.",
                "sub_steps": [
                    "Put away your notes and books",
                    "Answer your prepared questions from memory",
                    "Check your answers and note any gaps",
                    "Review material for concepts you missed"
                ]
            },
            {
                "description": "Create a visual summary of the first topic (mind map, diagram, chart).",
                "time": 15,
                "priority": "Medium",
                "adhd_tip": "Use colored pens or digital tools with varied colors and shapes to make this engaging.",
                "sub_steps": [
                    "Identify the main concept at the center",
                    "Add branches for key sub-topics",
                    "Include brief notes or symbols for important details",
                    "Connect related concepts with lines or arrows"
                ]
            },
            {
                "description": "Take a longer break before moving to the next topic.",
                "time": 15,
                "priority": "Medium",
                "adhd_tip": "Do something completely different during this break to help your brain consolidate information.",
                "sub_steps": [
                    "Move away from your study space",
                    "Do something enjoyable but time-limited",
                    "Have a small snack or drink if needed",
                    "Set an alarm to avoid breaking too long"
                ]
            },
            {
                "description": "Repeat the process with your second topic: set a goal, study actively, test yourself.",
                "time": 45,
                "priority": "High",
                "adhd_tip": "Change something about your study method to keep engagement high (location, technique, etc.).",
                "sub_steps": [
                    "Gather materials for the second topic",
                    "Set a specific learning goal",
                    "Use active study techniques",
                    "Test your understanding"
                ]
            },
            {
                "description": "Create connections between your first and second topics.",
                "time": 10,
                "priority": "Medium",
                "adhd_tip": "Draw a bridge diagram showing how the topics connect or relate to each other.",
                "sub_steps": [
                    "Identify common themes or principles",
                    "Note how concepts from one topic influence the other",
                    "Create examples that combine elements from both topics",
                    "Update your visual summaries to show connections"
                ]
            },
            {
                "description": "Plan your next study session with specific goals and timing.",
                "time": 10,
                "priority": "Medium",
                "adhd_tip": "Schedule your next study session when your energy is typically highest.",
                "sub_steps": [
                    "Decide what topics you'll cover next",
                    "Set specific learning objectives",
                    "Schedule the session in your calendar",
                    "Prepare materials in advance"
                ]
            }
        ],
        
        "financial_planning": [
            {
                "description": "Define your financial goals for this budget or plan.",
                "time": 15,
                "priority": "High",
                "adhd_tip": "Create a visual representation of your goals - photos or images that represent what you're saving for.",
                "sub_steps": [
                    "Identify short-term goals (next 3-12 months)",
                    "Consider medium-term goals (1-5 years)",
                    "Think about long-term goals (5+ years)",
                    "Make goals specific and measurable"
                ]
            },
            {
                "description": "Gather information about your income (paystubs, bank statements, etc.).",
                "time": 15,
                "priority": "High",
                "adhd_tip": "Create a 'money date' atmosphere - make a favorite drink and put on music to make this task more pleasant.",
                "sub_steps": [
                    "Collect records of all income sources",
                    "Calculate your average monthly income",
                    "Note if income varies month to month",
                    "Consider any upcoming changes to income"
                ]
            },
            {
                "description": "Track your spending for the past month by category.",
                "time": 30,
                "priority": "High",
                "adhd_tip": "Use a budgeting app that automatically categorizes expenses to make this less tedious.",
                "sub_steps": [
                    "Review bank and credit card statements",
                    "Group expenses into categories",
                    "Include cash spending if possible",
                    "Note any unusual or one-time expenses"
                ]
            },
            {
                "description": "Identify your necessary fixed expenses (rent, utilities, insurance, etc.).",
                "time": 15,
                "priority": "High",
                "adhd_tip": "Color-code expenses by necessity to create visual clarity about priorities.",
                "sub_steps": [
                    "List all recurring bills and payments",
                    "Note due dates for each expense",
                    "Identify which expenses are truly necessary",
                    "Calculate the total of fixed expenses"
                ]
            },
            {
                "description": "Calculate your discretionary spending (entertainment, dining out, etc.).",
                "time": 15,
                "priority": "Medium",
                "adhd_tip": "Use pie charts or graphs to visualize where your discretionary money goes.",
                "sub_steps": [
                    "Review variable expenses from past month",
                    "Group into categories like dining, entertainment, shopping",
                    "Identify patterns in your discretionary spending",
                    "Calculate total discretionary spending"
                ]
            },
            {
                "description": "Take a short break to avoid financial decision fatigue.",
                "time": 10,
                "priority": "Medium",
                "adhd_tip": "Do something physical during this break - financial planning involves a lot of sitting and thinking.",
                "sub_steps": [
                    "Step away from your financial documents",
                    "Do a quick physical activity",
                    "Have water or a healthy snack",
                    "Return with fresh focus"
                ]
            },
            {
                "description": "Compare income to expenses and calculate your current surplus or deficit.",
                "time": 10,
                "priority": "High",
                "adhd_tip": "Create a simple visual formula: Income - Expenses = Result (with a happy face for surplus, concerned face for deficit).",
                "sub_steps": [
                    "Total all income sources",
                    "Total all expenses (fixed and discretionary)",
                    "Subtract expenses from income",
                    "Note whether result is positive or negative"
                ]
            },
            {
                "description": "Identify 2-3 specific areas where you could reduce expenses.",
                "time": 15,
                "priority": "Medium",
                "adhd_tip": "Turn this into a game: 'Money Saving Detective' - look for clues where money is disappearing unnecessarily.",
                "sub_steps": [
                    "Look for subscriptions you don't use",
                    "Identify categories where you overspend",
                    "Consider alternatives for high-cost items",
                    "Estimate potential savings for each area"
                ]
            },
            {
                "description": "Create a realistic budget allocating income to expense categories.",
                "time": 25,
                "priority": "High",
                "adhd_tip": "Use the 50/30/20 rule as a starting point: 50% needs, 30% wants, 20% savings/debt reduction.",
                "sub_steps": [
                    "Start with essential expenses",
                    "Allocate funds for savings goals",
                    "Budget for discretionary spending",
                    "Ensure total doesn't exceed income"
                ]
            },
            {
                "description": "Set up a simple system to track expenses going forward.",
                "time": 20,
                "priority": "High",
                "adhd_tip": "Choose a tracking method that provides dopamine hits - many apps give celebratory notifications when you meet goals.",
                "sub_steps": [
                    "Select a tracking method (app, spreadsheet, notebook)",
                    "Set up categories that match your budget",
                    "Create a routine for entering expenses",
                    "Set reminders to review your tracking regularly"
                ]
            },
            {
                "description": "Plan specific actions for your top financial goal (debt payoff, saving, etc.).",
                "time": 15,
                "priority": "Medium",
                "adhd_tip": "Create a visual progress tracker for your main financial goal to make progress concrete and rewarding.",
                "sub_steps": [
                    "Break your goal into smaller milestones",
                    "Determine specific amounts to allocate",
                    "Create a timeline for reaching milestones",
                    "Decide how to automate or systematize this action"
                ]
            },
            {
                "description": "Schedule a monthly budget review to track progress and make adjustments.",
                "time": 10,
                "priority": "Medium",
                "adhd_tip": "Set calendar reminders with specific questions to answer during your review.",
                "sub_steps": [
                    "Choose a consistent date for monthly reviews",
                    "Create a simple template for the review",
                    "Set calendar reminders with specific prompts",
                    "Plan a small reward for completing each review"
                ]
            },
            {
                "description": "Create backups or safety nets for financial emergencies.",
                "time": 15,
                "priority": "Medium",
                "adhd_tip": "Use a visual 'emergency fund thermometer' to track progress toward this important goal.",
                "sub_steps": [
                    "Determine a target amount for emergency savings",
                    "Set up a separate account if possible",
                    "Create an automatic transfer for building this fund",
                    "Identify resources available in true emergencies"
                ]
            }
        ],
        
        "general": [
            {
                "description": "Define your goal and desired outcome for this task in one clear sentence.",
                "time": 10,
                "priority": "High",
                "adhd_tip": "Write this goal somewhere visible to help maintain focus throughout the task.",
                "sub_steps": [
                    "Identify what success looks like for this task",
                    "Make sure your goal is specific and measurable",
                    "Write it down in present tense as if already achieved"
                ]
            },
            {
                "description": "Break the task into 3-5 main components or phases.",
                "time": 15,
                "priority": "High",
                "adhd_tip": "Use physical objects or sticky notes to represent each component - making it tangible helps thinking.",
                "sub_steps": [
                    "Identify the major parts of this task",
                    "Group related activities together",
                    "Arrange components in logical order"
                ]
            },
            {
                "description": "For your first component, list 2-3 specific actions needed.",
                "time": 10,
                "priority": "High",
                "adhd_tip": "Start with the easiest action to build momentum and confidence.",
                "sub_steps": [
                    "Make each action concrete and doable",
                    "Be specific about what each action involves",
                    "Break down any action that seems overwhelming"
                ]
            },
            {
                "description": "Identify any resources, tools, or information you need for these actions.",
                "time": 10,
                "priority": "Medium",
                "adhd_tip": "Gather all resources before starting to minimize distractions once you begin.",
                "sub_steps": [
                    "List physical materials needed",
                    "Identify information required",
                    "Note any people whose help you'll need"
                ]
            },
            {
                "description": "Set a specific time to work on your first action step.",
                "time": 5,
                "priority": "High",
                "adhd_tip": "Schedule this during your peak energy time if possible.",
                "sub_steps": [
                    "Choose a specific day and time",
                    "Block this time in your calendar",
                    "Set up reminders or accountability"
                ]
            },
            {
                "description": "Create a simple plan for handling distractions during your work time.",
                "time": 10,
                "priority": "Medium",
                "adhd_tip": "Keep a 'distraction pad' nearby to quickly note things that pop into your mind for later.",
                "sub_steps": [
                    "Identify likely distractions",
                    "Plan specific ways to minimize each one",
                    "Prepare your environment for focus"
                ]
            },
            {
                "description": "Complete your first action step.",
                "time": 25,
                "priority": "High",
                "adhd_tip": "Use a visual timer to create a sense of timeboxing and urgency.",
                "sub_steps": [
                    "Set up your environment for focus",
                    "Use the Pomodoro technique if helpful",
                    "Track progress visibly as you work"
                ]
            },
            {
                "description": "Review what worked and what didn't after completing the first action.",
                "time": 5,
                "priority": "Medium",
                "adhd_tip": "This reflection builds metacognition - awareness of your own working process.",
                "sub_steps": [
                    "Note what went well with this action",
                    "Identify any challenges you faced",
                    "Consider how to adjust for next steps"
                ]
            },
            {
                "description": "Break down your second component into specific actions.",
                "time": 10,
                "priority": "High",
                "adhd_tip": "Build on the momentum from your first component - notice how breaking things down helps progress.",
                "sub_steps": [
                    "List 2-3 specific actions for component two",
                    "Make sure each action is clear and doable",
                    "Arrange in logical order"
                ]
            },
            {
                "description": "Schedule and set up for your next action steps.",
                "time": 10,
                "priority": "Medium",
                "adhd_tip": "Pre-commit by telling someone else when you'll do this next step.",
                "sub_steps": [
                    "Choose specific times for next actions",
                    "Gather any additional resources needed",
                    "Set up accountability or reminders"
                ]
            },
            {
                "description": "Create a simple tracking system to monitor overall progress on the task.",
                "time": 15,
                "priority": "Medium",
                "adhd_tip": "Make tracking visual and rewarding - use colors, stickers, or other visual markers of progress.",
                "sub_steps": [
                    "Create a checklist of all action steps",
                    "Set up a way to mark components as complete",
                    "Plan small celebrations for milestones"
                ]
            }
        ],
        
        "creative_writing": [
            {
                "description": "Brainstorm 3-5 potential ideas for your writing project.",
                "time": 15,
                "priority": "High",
                "adhd_tip": "Use a mind map with colors and images to make brainstorming more engaging.",
                "sub_steps": [
                    "Set a timer and write down all ideas without judging",
                    "Consider topics that genuinely interest you",
                    "Think about what you know or want to explore"
                ]
            },
            {
                "description": "Choose ONE idea and write a one-paragraph summary of the concept.",
                "time": 10,
                "priority": "High",
                "adhd_tip": "Speak your paragraph out loud first, then write it down - sometimes talking is easier than writing.",
                "sub_steps": [
                    "Review your brainstormed ideas",
                    "Select the one that excites you most",
                    "Write a brief summary of the core concept"
                ]
            },
            {
                "description": "Create character profiles for 1-3 main characters (fiction) or outline main themes (non-fiction).",
                "time": 20,
                "priority": "High",
                "adhd_tip": "Find or draw images that represent your characters or themes to make them more concrete.",
                "sub_steps": [
                    "For characters: note personality, motivation, background",
                    "For themes: list key points to explore",
                    "Consider how these elements connect to your main concept"
                ]
            }
        ]
    }
    
    
    remaining_task_types = {
        "job_search": [
            {
                "description": "Define your job search goals and parameters.",
                "time": 15,
                "priority": "High",
                "adhd_tip": "Create a visual 'ideal job profile' with images and words that represent what you're looking for.",
                "sub_steps": [
                    "Identify target roles or job titles",
                    "List must-have and nice-to-have job features",
                    "Define acceptable salary range and location parameters",
                    "Consider company culture and environment preferences"
                ]
            },
            {
                "description": "Update your resume with current information and achievements.",
                "time": 30,
                "priority": "High",
                "adhd_tip": "Break this into smaller 10-minute sessions focused on different sections of your resume.",
                "sub_steps": [
                    "Update your contact information and job history",
                    "Add recent achievements with measurable results",
                    "Check formatting and consistency",
                    "Proofread carefully or ask someone else to review"
                ]
            }
        ],
        
        "relocation": [
            {
                "description": "Create a master checklist of all relocation tasks with deadlines.",
                "time": 25,
                "priority": "High",
                "adhd_tip": "Use a digital checklist app with reminders or a large visible calendar to track everything.",
                "sub_steps": [
                    "Note all major tasks with deadlines",
                    "Group tasks by category (housing, utilities, etc.)",
                    "Mark high-priority items that must happen first",
                    "Include contact information for important services"
                ]
            }
        ]
    }
    
    
    for task_type, steps in remaining_task_types.items():
        if task_type not in task_templates:
            task_templates[task_type] = steps
    
    
    return task_templates.get(task_type, task_templates["general"])
from typing import List, Dict, Any, Optional
