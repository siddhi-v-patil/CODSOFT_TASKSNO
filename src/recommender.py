# recommender.py

from career_data import CAREERS
from skill_gap import analyze_recommended_careers


# ============================================================
# 1. NORMALIZE ITEMS
# ============================================================

def normalize_items(items):
    """
    Convert user input into clean lowercase items.
    """

    if isinstance(items, str):
        items = items.split(",")

    return {
        item.strip().lower()
        for item in items
        if item and item.strip()
    }


# ============================================================
# 2. CALCULATE MATCH
# ============================================================

def calculate_match(user_items, career_items):
    """
    Calculate how many career requirements
    match the user's items.
    """

    user_items = normalize_items(user_items)
    career_items = normalize_items(career_items)

    if not career_items:
        return 0

    matches = user_items.intersection(career_items)

    return len(matches) / len(career_items)


# ============================================================
# 3. CALCULATE CAREER SCORE
# ============================================================

def calculate_career_score(profile, career):
    """
    Calculate overall career suitability score.

    Weights:
    Interests        = 35%
    Skills           = 30%
    Preferences      = 20%
    Priorities       = 15%
    """

    interest_score = calculate_match(
        profile.get("interests", []),
        career.get("interests", [])
    )

    skill_score = calculate_match(
        profile.get("skills", []),
        career.get("skills", [])
    )

    preference_score = calculate_match(
        profile.get("work_preferences", []),
        career.get("work_preferences", [])
    )

    priority_score = calculate_match(
        profile.get("priorities", []),
        career.get("priorities", [])
    )

    final_score = (
        interest_score * 35
        + skill_score * 30
        + preference_score * 20
        + priority_score * 15
    )

    return round(final_score, 2)


# ============================================================
# 4. RECOMMEND CAREERS
# ============================================================

def recommend_careers(profile):
    """
    Score every career and return them
    in descending order.
    """

    results = []

    for career_name, career_data in CAREERS.items():

        score = calculate_career_score(
            profile,
            career_data
        )

        results.append({
            "career": career_name,
            "score": score
        })

    # Highest score first
    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results


# ============================================================
# 5. DISPLAY CAREER RECOMMENDATIONS
# ============================================================

def display_recommendations(results):
    """
    Display career recommendations.
    """

    print("\n" + "=" * 50)
    print("          CAREER RECOMMENDATIONS")
    print("=" * 50)

    if not results:
        print("No career recommendations found.")
        return

    for index, result in enumerate(results, start=1):

        print(
            f"{index}. {result['career']} "
            f"→ {result['score']:.2f}%"
        )

    print("=" * 50)


# ============================================================
# 6. CREATE PERSONALIZED LEARNING PATH
# ============================================================

def create_learning_path(skill_gap_results):
    """
    Create a personalized learning path from the
    missing skills identified by skill-gap analysis.
    """

    # Sensible prerequisite order
    prerequisite_order = [
        "python",
        "sql",
        "statistics",
        "numpy",
        "pandas",
        "data analysis",
        "machine learning",
        "scikit-learn",
        "deep learning",
        "tensorflow",
        "pytorch",
        "natural language processing",
        "transformers",
        "generative ai",
        "langchain",
        "vector databases",
        "cloud computing",
        "aws",
        "azure",
        "docker",
        "kubernetes"
    ]

    # Create priority positions
    priority = {
        skill.lower(): index
        for index, skill in enumerate(
            prerequisite_order
        )
    }

    learning_paths = []

    for result in skill_gap_results:

        missing_skills = result.get(
            "missing_skills",
            []
        )

        # Sort missing skills according
        # to prerequisite order
        ordered_skills = sorted(
            missing_skills,
            key=lambda skill: priority.get(
                skill.lower(),
                len(prerequisite_order)
            )
        )

        learning_paths.append({
            "career": result.get(
                "career",
                "Unknown Career"
            ),

            "score": result.get(
                "score",
                0
            ),

            "skill_match": result.get(
                "match_percentage",
                0
            ),

            "learning_path": ordered_skills
        })

    return learning_paths


# ============================================================
# 7. DISPLAY PERSONALIZED LEARNING PATH
# ============================================================

def display_learning_paths(learning_paths):
    """
    Display the personalized learning path.
    """

    print("\n" + "=" * 60)
    print("              PERSONALIZED LEARNING PATH")
    print("=" * 60)

    if not learning_paths:
        print("No learning path available.")
        return

    for path in learning_paths:

        print(f"\n{path['career']}")

        print(
            f"Career Score : "
            f"{path['score']:.2f}%"
        )

        print(
            f"Skill Match  : "
            f"{path['skill_match']:.2f}%"
        )

        print("\nRecommended order:")

        if path["learning_path"]:

            for index, skill in enumerate(
                path["learning_path"],
                start=1
            ):
                print(
                    f"  {index}. Learn {skill}"
                )

        else:

            print(
                "  You already have "
                "the required skills!"
            )

        print("-" * 60)

    print("=" * 60)


# ============================================================
# 8. DISPLAY SKILL GAP ANALYSIS
# ============================================================

def display_skill_gap(skill_gap_results):
    """
    Display skill-gap analysis for recommended careers.
    """

    print("\n" + "=" * 50)
    print("              SKILL GAP ANALYSIS")
    print("=" * 50)

    if not skill_gap_results:
        print("No skill-gap information available.")
        return

    for result in skill_gap_results:

        print(
            f"\n{result['career']}"
        )

        print(
            f"Career Score: "
            f"{result['score']:.2f}%"
        )

        print(
            f"Skill Match: "
            f"{result['match_percentage']:.2f}%"
        )

        # Matched skills
        print("\nMatched Skills:")

        if result["matched_skills"]:

            for skill in result["matched_skills"]:
                print(f"  ✓ {skill}")

        else:
            print("  None")

        # Missing skills
        print("\nSkills to Learn:")

        if result["missing_skills"]:

            for skill in result["missing_skills"]:
                print(f"  ✗ {skill}")

        else:

            print(
                "  You already have "
                "all required skills!"
            )

    print("\n" + "=" * 50)


# ============================================================
# 9. COMPLETE RECOMMENDATION FLOW
# ============================================================

def run_recommendation_flow(user_profile):
    """
    Complete career recommendation flow.

    Steps:
    1. Recommend careers
    2. Analyze skill gaps
    3. Create learning path
    4. Display results
    """

    # --------------------------------------------------------
    # STEP 1: CAREER RECOMMENDATIONS
    # --------------------------------------------------------

    results = recommend_careers(
        user_profile
    )

    display_recommendations(
        results
    )

    if not results:
        return {
            "recommendations": [],
            "skill_gaps": [],
            "learning_paths": []
        }

    # --------------------------------------------------------
    # STEP 2: SKILL GAP ANALYSIS
    # --------------------------------------------------------

    skill_gap_results = analyze_recommended_careers(
        results,
        user_profile.get("skills", []),
        top_n=3
    )

    # --------------------------------------------------------
    # STEP 3: PERSONALIZED LEARNING PATH
    # --------------------------------------------------------

    learning_paths = create_learning_path(
        skill_gap_results
    )

    # --------------------------------------------------------
    # STEP 4: DISPLAY SKILL GAP
    # --------------------------------------------------------

    display_skill_gap(
        skill_gap_results
    )

    # --------------------------------------------------------
    # STEP 5: DISPLAY LEARNING PATH
    # --------------------------------------------------------

    display_learning_paths(
        learning_paths
    )

    # --------------------------------------------------------
    # RETURN ALL RESULTS
    # --------------------------------------------------------

    return {
        "recommendations": results,
        "skill_gaps": skill_gap_results,
        "learning_paths": learning_paths
    }


# ============================================================
# 10. TEST THE RECOMMENDER
# ============================================================

if __name__ == "__main__":

    user_profile = {

        "interests": [
            "artificial intelligence",
            "generative ai",
            "chatbots",
            "automation"
        ],

        "skills": [
            "python",
            "artificial intelligence",
            "machine learning"
        ],

        "work_preferences": [
            "building systems",
            "problem solving",
            "automation"
        ],

        "priorities": [
            "high salary",
            "career growth",
            "innovation"
        ]
    }

    run_recommendation_flow(
        user_profile
    )