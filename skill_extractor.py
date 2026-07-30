def extract_skills(filename):

    name = filename.lower()

    skills = []

    keywords = {
        "python": "Python",
        "java": "Java",
        "ai": "Artificial Intelligence",
        "ml": "Machine Learning",
        "web": "Web Development",
        "flask": "Flask",
        "sql": "SQL",
        "html": "HTML",
        "css": "CSS",
        "javascript": "JavaScript"
    }

    for key, value in keywords.items():
        if key in name:
            skills.append(value)

    if not skills:
        skills.append("General")

    return skills