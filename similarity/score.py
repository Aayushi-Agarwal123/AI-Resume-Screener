def calculate_score(resume_skills, job_skills):

    # Remove duplicates
    resume_skills = list(set(resume_skills))
    job_skills = list(set(job_skills))

    # Matched Skills
    matched_skills = []

    for skill in job_skills:
        if skill in resume_skills:
            matched_skills.append(skill)

    # Missing Skills
    missing_skills = []

    for skill in job_skills:
        if skill not in resume_skills:
            missing_skills.append(skill)

    # ATS Score
    if len(job_skills) == 0:
        score = 0
    else:
        score = (len(matched_skills) / len(job_skills)) * 100

    return matched_skills, missing_skills, score