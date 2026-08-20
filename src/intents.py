# CareerBot - Intent Knowledge Base
# Task 1: Rule-Based Chatbot

INTENTS = {

    # ============================================================
    # GREETING
    # ============================================================

    "greeting": {

        "patterns": [
            "hi",
            "hello",
            "hey",
            "hey there",
            "good morning",
            "good afternoon",
            "good evening"
        ],

        "responses": [
            "Hello! I'm CareerBot. How can I help you with your career?",
            "Hi! I'm CareerBot. Ask me about internships, skills, resumes, or interviews."
        ]
    },


    # ============================================================
    # INTERNSHIP
    # ============================================================

    "internship": {

        "patterns": [
            "how can I get an internship",
            "how to get an internship",
            "where can I find internships",
            "internship opportunities",
            "I want an internship",
            "how do I apply for an internship"
        ],

        "responses": [
            "To get an internship, build relevant skills, create a strong resume, work on practical projects, and apply through company career pages and trusted job platforms.",

            "Start by choosing a career field, building 2-3 relevant projects, preparing your resume, and applying consistently to suitable internships."
        ]
    },


    # ============================================================
    # SKILLS
    # ============================================================

    "skills": {

        "patterns": [
            "what skills should I learn",
            "which skills should I learn",
            "skills for a job",
            "what skills are important",
            "how can I improve my skills"
        ],

        "responses": [
            "Focus on technical skills related to your target role, along with communication, problem-solving, teamwork, and practical project experience.",

            "Choose skills based on your target career. For AI and Data Science, Python, SQL, statistics, data analysis, machine learning, and GenAI are useful areas to develop."
        ]
    },


    # ============================================================
    # RESUME
    # ============================================================

    "resume": {

        "patterns": [
            "how to make a resume",
            "resume tips",
            "how can I improve my resume",
            "what should I include in my resume",
            "resume for internship"
        ],

        "responses": [
            "Keep your resume concise and highlight your skills, projects, internships, certifications, and measurable achievements relevant to the role.",

            "For an internship resume, focus on strong projects, technical skills, education, certifications, and any practical experience."
        ]
    },


    # ============================================================
    # INTERVIEW
    # ============================================================

    "interview": {

        "patterns": [
            "how to prepare for an interview",
            "interview preparation",
            "how can I prepare for an interview",
            "interview tips",
            "how to crack an interview"
        ],

        "responses": [
            "Prepare by researching the company, revising your technical fundamentals, practicing common interview questions, and preparing clear explanations of your projects.",

            "Practice both technical and behavioral questions. Be ready to explain what you built, why you built it, and what challenges you solved."
        ]
    },


    # ============================================================
    # CAREER GUIDANCE
    # ============================================================

    "career_guidance": {

        "patterns": [
            "I don't know what career to choose",
            "which career should I choose",
            "help me choose a career",
            "career advice",
            "I am confused about my career",
            "what career is best for me"
        ],

        "responses": [
            "Start by identifying your interests, strengths, preferred type of work, and the skills required by different careers. Then explore those careers through projects and internships.",

            "A good career choice should match your interests and strengths while also offering opportunities to grow. Try small projects before committing to a path."
        ]
    },


    # ============================================================
    # GOODBYE
    # ============================================================

    "goodbye": {

        "patterns": [
            "bye",
            "goodbye",
            "see you",
            "talk to you later",
            "exit"
        ],

        "responses": [
            "Goodbye! Keep learning and building. Good luck with your career!",

            "See you! Keep working on your skills and projects."
        ]
    }
}