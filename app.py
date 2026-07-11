# print("===================================")
# print(" AI Resume Screening Tool ")
# print(" Developed by Aayushi Agarwal ")
# print("===================================")
from parser.pdf_parser import extract_text

resume_path = "resumes/Aayushi Agarwal resume.pdf"

resume_text = extract_text(resume_path)

print("========== Resume Text ==========\n")

print(resume_text)

from parser.pdf_parser import extract_text
from preprocessing.text_cleaner import clean_text
from extractor.skills import extract_skills
from similarity.score import calculate_score
from recommadation.recommadate import get_recommendations


resume_path = "resumes/Aayushi Agarwal Resume.pdf"

resume_text = extract_text(resume_path)

cleaned_text = clean_text(resume_text)

print(cleaned_text)

skills = extract_skills(cleaned_text)

print("\nSkills Found:")
print(skills)

with open("job_description/jd.txt", "r") as file:
    job_description = file.read()
    print(job_description)

    cleaned_job = clean_text(job_description)

job_skills = extract_skills(cleaned_job)

print("\nJob Skills Found:")
print(job_skills)

matched_skills , missing_skill , score = calculate_score(skills , job_skills)
recommendations = get_recommendations(missing_skill)
print("\nMatched skills:")
print(matched_skills)
print("\nMissing Skills")
print(missing_skill)
print("\nATS Score:")
print(f"{score:.2f}%")
print("\nrecommadation")
print(recommendations)
