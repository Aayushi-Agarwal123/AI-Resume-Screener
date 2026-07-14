import streamlit as st
from parser.pdf_parser import extract_text
from preprocessing.text_cleaner import clean_text
from extractor.skills import extract_skills
from similarity.score import calculate_score
from recommadation.recommadate import get_recommendations
st.title("🤖 AI Resume Screener")
st.write("Upload your resume and job description to calculate ATS score.")
resume = st.file_uploader(
    "upload resume",
    type=["pdf"]
)
jd = st.text_area(
    "Job description",
    height = 250 ,
    placeholder = "Type Job Description "
)
analyze = st.button("🚀 Analyze Resume")
if analyze:
    st.write("Analyzing Resume...")
    if resume is None:
        st.error("Please upload your resume")
    elif jd == "":
         st.error("Please Paste Job Description")
    else:
        st.success("Everything looks perfect ") 

        resume_text= extract_text(resume)
        st.subheader("Extracted Resume text")
        st.write(resume_text)
        
        cleaned_resume = clean_text(resume_text)
        st.subheader("Cleaned Resume")
        st.write(cleaned_resume)
        resume_skills = extract_skills(cleaned_resume)
        st.write(resume_skills)

         # Job Description Processing
    cleaned_jd = clean_text(jd)

    job_skills = extract_skills(cleaned_jd)

    st.subheader("Job Skills")
    st.write(job_skills)

    # ATS Score
    matched_skills, missing_skills, score = calculate_score(
        resume_skills,
        job_skills
    )

    st.subheader("ATS Score")
    st.write(f"{score:.2f}%")

    st.subheader("ATS Score")
    st.write(f"{score:.2f}%")
    st.progress(int(score))

if score >= 80:
    st.success("Excellent Resume Match! 🎉")

elif score >= 60:
    st.warning("Good Match. You can improve by learning the missing skills.")

else:
    st.error("Low ATS Score. Improve your resume.")

st.subheader("Matched Skills")
st.write(matched_skills)

st.subheader("Missing Skills")
st.write(missing_skills)

recommendations = get_recommendations(missing_skills)

st.subheader("Recommendations")
st.write(recommendations)
    
          