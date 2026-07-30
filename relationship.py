def build_relationships(documents):

    relationships = []

    for doc in documents:

        category = doc["category"]

        skills = doc["skills"]

        if category == "Certification":
            for skill in skills:
                relationships.append(
                    f"{doc['name']} ➜ proves {skill}"
                )

        elif category == "Project":
            for skill in skills:
                relationships.append(
                    f"{doc['name']} ➜ uses {skill}"
                )

        elif category == "Internship":
            for skill in skills:
                relationships.append(
                    f"{doc['name']} ➜ experience in {skill}"
                )

    return relationships