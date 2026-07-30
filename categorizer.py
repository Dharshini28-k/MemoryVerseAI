def categorize(filename):

    name = filename.lower()

    if "certificate" in name:
        return "Certification"

    elif "resume" in name or "cv" in name:
        return "Resume"

    elif "project" in name:
        return "Project"

    elif "intern" in name:
        return "Internship"

    elif "achievement" in name:
        return "Achievement"

    else:
        return "Other"