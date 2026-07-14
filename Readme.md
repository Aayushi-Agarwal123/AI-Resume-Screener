# AI Resume Screening and Scoring Tool


An AI-powered Resume Screening application built using **Python** and **Streamlit** that analyzes resumes against a Job Description (JD) and calculates an ATS (Applicant Tracking System) compatibility score.

---

## 📌 Features

- Upload Resume (PDF)
- Paste Job Description
- Extract Resume Text
- Clean Resume Text
- Extract Technical Skills
- Calculate ATS Score
- Display Matched Skills
- Display Missing Skills
- Qualification Analysis
- Resume Recommendations
- Resume Rating


---

## 🛠 Tech Stack

- Python
- Streamlit
- PyMuPDF (fitz)
- Regular Expressions (Regex)

---

## 📂 Project Workflow

Resume Upload
↓

PDF Text Extraction

↓

Text Cleaning

↓

Skill Extraction

↓

Qualification Extraction

↓

ATS Score Calculation

↓

Matched Skills

↓

Missing Skills

↓

Recommendations

↓

Final Resume Verdict

---

## 📊 Methodology

The application follows the following workflow:

1. The user uploads a resume in PDF format.
2. The PDF is parsed using PyMuPDF.
3. Resume text is cleaned using Regular Expressions.
4. Skills are extracted by comparing the resume with a predefined skill database.
5. The Job Description is cleaned and processed similarly.
6. Resume skills and Job Description skills are compared.
7. An ATS score is calculated based on matched skills.
8. Qualification is extracted and matched.
9. Missing skills are identified.
10. Learning recommendations are generated.

---

## ⚠ Limitations

Current limitations include:

- Works only with PDF resumes.
- Uses keyword-based skill extraction.
- Cannot understand synonyms automatically.
- Does not evaluate project quality.
- Experience matching is limited.
- Soft skills are not analyzed.
- ATS score depends on keyword availability.
- Images inside resumes are ignored.

---

## 🚀 Future Enhancements

- Compare multiple resumes simultaneously.
- AI-powered resume suggestions using LLMs.
- Experience matching.
- Certification analysis.
- Export ATS Report as PDF.
- Resume Ranking Dashboard.
- DOCX Resume Support.
- Job URL parsing.
- Recruiter Dashboard.

---

## 📈 Prototype Findings

The prototype successfully performs:

- Resume Parsing
- ATS Score Calculation
- Qualification Matching
- Skill Matching
- Missing Skill Detection
- Resume Recommendation

The application provides a quick evaluation of resume compatibility with a Job Description.

---

## 📷 Screenshots

(Add screenshots here)

---

## 👩‍💻 Developed By

Aayushi Agarwal