# skill_gap.py

from career_data import CAREERS


# ============================================================
# 1. ANALYZE SKILL GAP
# ============================================================

def analyze_skill_gap(career, user_skills):
    """
    Compare a user's skills with the skills required
    for a selected career.
    """

    career = career.strip()

    # Check whether career exists
    if career not in CAREERS:
        return None

    # Required skills for the selected career
    required_skills = {
        skill.lower().strip()
        for skill in CAREERS[career]["skills"]
    }

    # User's current skills
    user_skills = {
        skill.lower().strip()
        for skill in user_skills
        if skill and skill.strip()
    }

    # Find matching and missing skills
    matched_skills = required_skills.intersection(
        user_skills
    )

    missing_skills = required_skills.difference(
        user_skills
    )

    # Calculate match percentage
    if required_skills:

        match_percentage = (
            len(matched_skills)
            / len(required_skills)
        ) * 100

    else:

        match_percentage = 0

    return {
        "career": career,
        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(missing_skills),
        "match_percentage": round(
            match_percentage,
            2
        )
    }


# ============================================================
# 2. PRINT SKILL GAP
# ============================================================

def print_skill_gap(result):
    """
    Display the skill-gap analysis.
    """

    print("\n" + "=" * 50)
    print("       CAREER SKILL-GAP ANALYSIS")
    print("=" * 50)

    print(
        f"\nCareer: "
        f"{result['career'].title()}"
    )

    print(
        f"\nSkill Match: "
        f"{result['match_percentage']}%"
    )

    # --------------------------------------------------------
    # Skills already available
    # --------------------------------------------------------

    print("\nSkills You Already Have:")

    if result["matched_skills"]:

        for skill in result["matched_skills"]:
            print(f"  ✓ {skill}")

    else:

        print("  No matching skills found.")

    # --------------------------------------------------------
    # Skills that are missing
    # --------------------------------------------------------

    print("\nSkills You Need to Learn:")

    if result["missing_skills"]:

        for skill in result["missing_skills"]:
            print(f"  ✗ {skill}")

    else:

        print(
            "  Great! You have all required skills."
        )

    # --------------------------------------------------------
    # Recommended next steps
    # --------------------------------------------------------

    print("\nRecommended Next Steps:")

    if result["missing_skills"]:

        for index, skill in enumerate(
            result["missing_skills"][:5],
            start=1
        ):

            print(
                f"  {index}. Learn {skill}"
            )

    else:

        print(
            "  Continue improving your existing skills!"
        )

    print("=" * 50)


# ============================================================
# 3. ANALYZE TOP RECOMMENDED CAREERS
# ============================================================

def analyze_recommended_careers(
    results,
    user_skills,
    top_n=3
):
    """
    Perform skill-gap analysis for the top
    recommended careers.
    """

    analyses = []

    # Only analyze the top N careers
    for result in results[:top_n]:

        career = result["career"]

        analysis = analyze_skill_gap(
            career,
            user_skills
        )

        if analysis:

            analyses.append({

                "career": career,

                "score": result["score"],

                "matched_skills":
                    analysis["matched_skills"],

                "missing_skills":
                    analysis["missing_skills"],

                "match_percentage":
                    analysis["match_percentage"]
            })

    return analyses


# ============================================================
# 4. TEST SKILL-GAP ANALYSIS
# ============================================================

if __name__ == "__main__":

    career = "AI/ML Engineer"

    my_skills = [
        "python",
        "sql",
        "numpy",
        "pandas"
    ]

    result = analyze_skill_gap(
        career,
        my_skills
    )

    if result:

        print_skill_gap(result)

    else:

        print(
            f"\nCareer '{career}' was not found."
        )