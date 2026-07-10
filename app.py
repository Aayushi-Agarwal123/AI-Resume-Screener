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

resume_path = "resumes/Aayushi Agarwal Resume.pdf"

resume_text = extract_text(resume_path)

cleaned_text = clean_text(resume_text)

print(cleaned_text)

skills = extract_skills(cleaned_text)

print("\nSkills Found:")
print(skills)