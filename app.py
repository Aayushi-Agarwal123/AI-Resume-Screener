# print("===================================")
# print(" AI Resume Screening Tool ")
# print(" Developed by Aayushi Agarwal ")
# print("===================================")
from parser.pdf_parser import extract_text

resume_path = "resumes/Aayushi Agarwal resume.pdf"

resume_text = extract_text(resume_path)

print("========== Resume Text ==========\n")

print(resume_text)