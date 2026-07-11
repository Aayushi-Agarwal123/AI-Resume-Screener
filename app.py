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


resume_path = "resumes/Aayushi Agarwal Resume.pdf"

resume_text = extract_text(resume_path)

cleaned_text = clean_text(resume_text)

print(cleaned_text)

skills = extract_skills(cleaned_text)

print("\nSkills Found:")
print(skills)

with open("job_description/jd.txt", "r") as file:
    job_description = file.read()

    cleaned_job = clean_text(job_description)

job_skills = extract_skills(cleaned_job)

print("\nJob Skills Found:")
print(job_skills)

matched_skills = calculate_score(skills , job_skills)
print("\nMatched skills:")
print(matched_skills)
