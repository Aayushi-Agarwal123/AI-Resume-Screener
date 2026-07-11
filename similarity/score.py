def calculate_score(resume_skills, job_skills):

    matched_skills = []
    missing_skills = []

    for skill in resume_skills:
        if skill in job_skills:
            matched_skills.append(skill)

    for skill in resume_skills:
        if skill not in job_skills:
            missing_skills.append(skill)

        score = (len(matched_skills) / len(job_skills)) * 100


    return matched_skills , missing_skills , score  