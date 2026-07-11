def extract_skills(text):

    skills_database = [

        "python",
        "java",
        "c",
        "c++",
        "javascript",
        "react",
        "node.js",
        "express",
        "mongodb",
        "mysql",
        "sql",
        "html",
        "css",
        "docker",
        "git",
        "github",
        "aws",
        "azure",
        "gcp",
        "tensorflow",
        "machine learning",
        "deep learning",
        "kotlin"

    ]

    found_skills = []

    text = text.lower()

    for skill in skills_database:

        if skill in text:
            found_skills.append(skill)

    return found_skills