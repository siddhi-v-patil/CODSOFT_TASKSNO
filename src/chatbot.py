import random
import re

from intents import INTENTS
from skill_gap import analyze_skill_gap, print_skill_gap
from recommender import run_recommendation_flow


def normalize_text(text):
    """Clean and normalize user input."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", "", text)
    return text


def detect_intent(user_input):
    """Find the best matching intent using keyword/pattern matching."""
    text = normalize_text(user_input)

    best_intent = None
    best_score = 0

    for intent_name, intent_data in INTENTS.items():
        score = 0

        for pattern in intent_data["patterns"]:
            pattern_words = normalize_text(pattern).split()

            if all(word in text.split() for word in pattern_words):
                score += len(pattern_words)

        if score > best_score:
            best_score = score
            best_intent = intent_name

    return best_intent


def generate_response(user_input):
    """Generate a response based on the detected intent."""
    intent = detect_intent(user_input)

    if intent is None:
        return (
            "I'm not sure I understood that. "
            "You can ask me about careers, skills, internships, "
            "resumes, interviews, or career guidance."
        )

    responses = INTENTS[intent]["responses"]

    return random.choice(responses)


def get_list_input(question):
    """
    Ask the user for multiple items separated by commas.
    """
    while True:
        answer = input(question).strip()

        if answer:
            items = [
                item.strip()
                for item in answer.split(",")
                if item.strip()
            ]

            if items:
                return items

        print("CareerBot: Please enter at least one item.")


def collect_user_profile():
    """
    Collect the information required by the career recommender.
    """

    print("\n" + "=" * 60)
    print("PERSONALIZED CAREER ASSESSMENT")
    print("=" * 60)

    print("\nCareerBot: Let's find the careers that best match you!")

    interests = get_list_input(
        "\nCareerBot: What are your interests? "
        "\nExamples: artificial intelligence, data, cloud, technology"
        "\nYou: "
    )

    skills = get_list_input(
        "\nCareerBot: What skills do you currently have?"
        "\nExamples: Python, SQL, machine learning, Excel"
        "\nYou: "
    )

    work_preferences = get_list_input(
        "\nCareerBot: What type of work do you prefer?"
        "\nExamples: problem solving, building systems, automation"
        "\nYou: "
    )

    priorities = get_list_input(
        "\nCareerBot: What are your career priorities?"
        "\nExamples: high salary, career growth, innovation"
        "\nYou: "
    )

    user_profile = {
        "interests": interests,
        "skills": skills,
        "work_preferences": work_preferences,
        "priorities": priorities
    }

    return user_profile


def run_personalized_career_flow():
    """
    Collect user information and run the complete
    recommendation → skill gap → learning path pipeline.
    """

    user_profile = collect_user_profile()

    print("\nCareerBot: Analyzing your profile...")
    print("CareerBot: Ranking careers based on your interests, skills,")
    print("           work preferences, and priorities.")

    run_recommendation_flow(user_profile)


def main():
    print("\n" + "=" * 60)
    print("                    CAREERBOT")
    print("=" * 60)

    print(
        "\nCareerBot: Hello! I am CareerBot, your personalized "
        "career guidance assistant."
    )

    print("\nWhat would you like to do?")

    print("\n1. Get personalized career recommendations")
    print("2. Check a skill gap")
    print("3. Chat about careers")
    print("4. Exit")

    while True:

        choice = input("\nYou: ").strip().lower()

        if choice in ["1", "recommend", "recommendation", "career recommendation"]:

            run_personalized_career_flow()

            print("\nCareerBot: Your personalized career analysis is complete.")

            again = input(
                "\nCareerBot: Would you like to run another assessment? (yes/no): "
            ).strip().lower()

            if again in ["yes", "y"]:
                continue
            else:
                print(
                    "\nCareerBot: Great! Keep learning, building projects, "
                    "and improving your skills."
                )
                break

        elif choice in ["2", "skill gap", "skillgap"]:

            print("\nAvailable careers:")
            print("1. AI/ML Engineer")
            print("2. Data Scientist")
            print("3. GenAI Engineer")
            print("4. Cloud Engineer")

            career = input("\nEnter your career: ")

            skills_input = input(
                "Enter your current skills separated by commas: "
            )

            user_skills = skills_input.split(",")

            result = analyze_skill_gap(
                career,
                user_skills
            )

            if result:
                print_skill_gap(result)
            else:
                print("\nCareer not found.")

        elif choice in ["3", "chat", "career", "help"]:

            user_input = input(
                "\nCareerBot: What would you like to know?\nYou: "
            )

            response = generate_response(user_input)

            print("CareerBot:", response)

        elif choice in ["4", "bye", "goodbye", "exit", "quit"]:

            print(
                "\nCareerBot: Goodbye! Keep learning and building "
                "your career."
            )
            break

        else:

            print(
                "\nCareerBot: Please choose 1, 2, 3, or 4."
            )


if __name__ == "__main__":
    main()