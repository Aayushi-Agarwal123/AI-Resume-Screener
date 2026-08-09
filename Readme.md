# 🤖 AI Resume Screener & Candidate Ranking System

An intelligent full-stack **Resume Screening and Candidate Ranking System** that helps recruiters analyze multiple resumes against a Job Description (JD), calculate ATS compatibility scores, identify skill gaps, rank candidates, and generate recruitment insights and hiring reports.

The project combines a modern **React + TypeScript frontend** with a **Python FastAPI backend** for resume processing and candidate analysis.

---

## 🌐 Live Demo

### 🚀 Frontend

https://ai-resume-screener-hr6x.vercel.app

### ⚙️ Backend API

https://ai-resume-screener-ynpp.onrender.com

### 💻 GitHub Repository

https://github.com/Aayushi-Agarwal123/AI-Resume-Screener

---

# ✨ Features

## 📄 Resume Screening

* Upload multiple Resume PDFs
* Extract resume text automatically
* Analyze multiple candidates in a single request
* Compare candidates against a Job Description

## 🤖 ATS Analysis

* Calculate ATS compatibility scores
* Identify matched skills
* Detect missing skills
* Evaluate candidate-job compatibility
* Display scores with recruiter-friendly formatting

## 🏆 Candidate Ranking

* Automatically rank candidates based on ATS scores
* Identify the highest-scoring candidate
* Compare multiple candidates
* View detailed candidate information

## 📊 Recruitment Analytics

* Total candidates analyzed
* Average ATS score
* Highest ATS score
* Lowest ATS score
* Qualified candidates
* Candidate selection rate
* ATS score visualization

## 📌 Candidate Status

Candidates are categorized based on their ATS score:

| ATS Score | Status             |
| --------- | ------------------ |
| 80%+      | 🟢 Strong Match    |
| 60–79.99% | 🟡 Potential Match |
| Below 60% | 🔴 Needs Review    |

## 📑 Reports & Insights

* Candidate analysis dashboard
* Candidate comparison
* Recruitment activity feed
* PDF hiring reports
* CSV data export
* Resume improvement recommendations

---

# 🖥️ Application Preview

The application provides a recruiter-friendly dashboard where users can:

1. Upload multiple resumes.
2. Enter a Job Description.
3. Analyze all candidates.
4. View ATS scores and skill matches.
5. Compare candidates.
6. View candidate rankings.
7. Identify the strongest candidates.
8. Review recruitment analytics.
9. Generate hiring reports.

---

# 🛠️ Tech Stack

## Frontend

* React.js
* TypeScript
* CSS
* Vite

## Backend

* Python
* FastAPI
* REST API
* CORS Middleware

## Resume Processing

* PyMuPDF
* PDF text extraction
* Skill extraction
* Text preprocessing

## Data & Visualization

* Pandas
* Plotly

## Report Generation

* ReportLab
* CSV Export

## Deployment

* Vercel — Frontend
* Render — Backend

---

# 🧩 Core Modules

```text
Resume Upload
      ↓
PDF Text Extraction
      ↓
Text Preprocessing
      ↓
Skill Extraction
      ↓
Job Description Skill Extraction
      ↓
ATS Score Calculation
      ↓
Matched / Missing Skills
      ↓
Candidate Ranking
      ↓
Recruitment Analytics
      ↓
Reports & Recommendations
```

---

# 📂 Project Structure

```text
AI-Resume-Screener/
│
├── extractor/
│   └── skills.py
│
├── parser/
│   └── pdf_parser.py
│
├── preprocessing/
│   └── text_cleaner.py
│
├── similarity/
│   └── score.py
│
├── recommadation/
│   └── recommadate.py
│
├── reports/
│
├── frontend/
│   ├── src/
│   ├── components/
│   └── ...
│
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Backend Installation

### Clone Repository

```bash
git clone https://github.com/Aayushi-Agarwal123/AI-Resume-Screener.git
```

### Navigate to Project

```bash
cd AI-Resume-Screener
```

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Run FastAPI Backend

```bash
uvicorn main:app --reload
```

The API will be available locally at:

```text
http://127.0.0.1:8000
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 🎨 Frontend Setup

Navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will run locally on the Vite development server.

---

# 🔌 API Endpoint

The main resume analysis endpoint is:

```text
POST /analyze
```

It accepts:

```text
resumes
job_description
```

and returns candidate analysis including:

* ATS scores
* Matched skills
* Missing skills
* Candidate ranking
* Recruitment statistics
* Top candidate information

---

# 📊 ATS Scoring

The current ATS scoring system compares the skills extracted from the resume with the skills identified from the Job Description.

```text
ATS Score =
(Matched Job Skills / Total Job Skills) × 100
```

The resulting score is rounded to two decimal places for a cleaner recruiter-facing interface.

---

# 🔄 Project Workflow

### Step 1 — Upload Resumes

Recruiters can upload one or multiple PDF resumes.

### Step 2 — Enter Job Description

The recruiter provides the required Job Description.

### Step 3 — Analyze

The FastAPI backend processes the uploaded resumes.

### Step 4 — Extract Skills

Skills are extracted from both resumes and the Job Description.

### Step 5 — Calculate ATS Score

Each candidate receives an ATS compatibility score.

### Step 6 — Rank Candidates

Candidates are ranked according to their ATS scores.

### Step 7 — Review Analytics

Recruiters can view:

* Total candidates
* Average ATS
* Highest score
* Lowest score
* Qualified candidates
* Candidate rankings

### Step 8 — Generate Reports

Recruiters can review candidate information and generate hiring reports.

---

# 🚀 Deployment Architecture

```text
                  ┌─────────────────────────┐
                  │      React Frontend     │
                  │       TypeScript        │
                  │         Vercel          │
                  └────────────┬────────────┘
                               │
                               │ POST /analyze
                               ▼
                  ┌─────────────────────────┐
                  │     FastAPI Backend     │
                  │         Python          │
                  │         Render          │
                  └────────────┬────────────┘
                               │
                 ┌─────────────┼─────────────┐
                 ▼             ▼             ▼
              PDF Parser   Skill Engine   ATS Engine
                 │             │             │
                 └─────────────┼─────────────┘
                               ▼
                    Candidate Ranking
                               │
                               ▼
                     Recruitment Analytics
```

---

# 📌 Key Highlights

* 🤖 Intelligent Resume Screening
* 📄 Multi-Resume Analysis
* 🎯 Job Description Matching
* 📊 ATS Compatibility Scoring
* 🛠️ Skill Gap Identification
* 🏆 Candidate Ranking
* 📈 Recruitment Analytics
* 👥 Candidate Comparison
* 📑 Hiring Report Generation
* 📥 CSV Export
* ⚡ FastAPI REST API
* 🌐 Full-Stack Deployment
* 📱 Responsive Recruiter Dashboard

---

# 🔮 Future Improvements

The project can be further enhanced with:

* 🔄 AI-powered Resume Tailoring
* ✨ Personalized Resume Improvement Suggestions
* 📝 Advanced Keyword Optimization
* 📄 ATS-Friendly Resume Generation
* 🧠 Semantic Resume-JD Matching using Embeddings
* 🔐 User Authentication & Authorization
* 🗄️ Candidate Database
* ☁️ Cloud Storage for Resumes
* 📧 Automated Recruiter Notifications
* 📊 Advanced Recruitment Analytics
* 🤖 LLM-based Candidate Insights

---

# 👩‍💻 Developed By

## Aayushi Agarwal

**Full Stack Developer | MERN Stack | Python | AI Enthusiast**

### GitHub

https://github.com/Aayushi-Agarwal123

### LinkedIn

https://www.linkedin.com/in/aayushi-agarwal-961a47333

---

# ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

Your support and feedback are greatly appreciated!
