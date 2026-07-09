required_skills = [
    "python",
    "machine learning",
    "sql",
    "git",
    "communication"
]


def calculate_score(applicant):

    score = 0

    for skill in applicant.skills:

        if skill.lower() in required_skills:
            score += 20

    score += applicant.experience * 5

    if score > 100:
        score = 100

    applicant.score = score
