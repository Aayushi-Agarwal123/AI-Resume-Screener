def calculate_score(resume_skills, job_skills):

    matched_skills = []

    for skill in resume_skills:
        if skill in job_skills:
            matched_skills.append(skill)

        score = (len(matched_skills) / len(job_skills)) * 100


    return matched_skills , score