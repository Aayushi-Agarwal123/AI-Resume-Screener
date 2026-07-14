import streamlit as st
st.set_page_config(
    page_title="AI Resume Screener",
    page_icon="🤖",
    layout="wide"
)
st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

h1{
    color:#4F8BF9;
}

div[data-testid="stMetric"]{
    background-color:#1E1E1E;
    border-radius:12px;
    padding:15px;
    border:1px solid #333;
}

div.stButton > button{
    width:100%;
    height:55px;
    border-radius:12px;
    font-size:18px;
    font-weight:bold;
}

</style>
""",unsafe_allow_html=True)
from parser.pdf_parser import extract_text
from preprocessing.text_cleaner import clean_text
from extractor.skills import extract_skills
from similarity.score import calculate_score
from recommadation.recommadate import get_recommendations
from extractor.Qualification import extract_qualification
st.title("🤖 AI Resume Screener")

st.markdown("""
Analyze your resume against a Job Description using AI-powered ATS scoring.

✨ Upload Resume
📄 Paste Job Description
📊 Get ATS Score
🎯 Improve Your Resume
""")
with st.sidebar:
    st.header("📌 Instructions")

    st.write("""
1. Upload Resume (PDF)
2. Paste Job Description
3. Click Analyze Resume
4. View ATS Score
5. Improve Missing Skills
    """)

st.divider()
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
        st.success("Everything looks perfect! 🎉")

        # ================= Resume Processing =================

        resume_text = extract_text(resume)

        st.subheader("📄 Extracted Resume Text")
        st.write(resume_text)

        cleaned_resume = clean_text(resume_text)

        st.subheader("🧹 Cleaned Resume")
        st.write(cleaned_resume)

        resume_skills = extract_skills(cleaned_resume)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🛠 Resume Skills")
            st.write(resume_skills)

        cleaned_jd = clean_text(jd)

        job_skills = extract_skills(cleaned_jd)

        with col2:
            st.subheader("📋 Job Skills")
            st.write(job_skills)

        # ================= Qualification =================

        resume_qualification = extract_qualification(cleaned_resume)
        job_qualification = extract_qualification(cleaned_jd)
 
        matched_qualification = []

        for qualification in resume_qualification:
            if qualification in job_qualification:
                matched_qualification.append(qualification)

        st.subheader("🎓 Qualification Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🎓 Resume Qualification")

            if resume_qualification:
                for qualification in resume_qualification:
                    st.success(qualification)
            else:
                st.warning("No qualification found in Resume.")

        with col2:
            st.subheader("📋 Required Qualification")

            if job_qualification:
                for qualification in job_qualification:
                    st.info(qualification)
            else:
                    st.warning("No qualification mentioned in Job Description.")

# ----------- Qualification Status --------------

        st.subheader("🎯 Qualification Status")

        if matched_qualification:
            st.success("✅ Qualification Matched")
        else:
            st.error("❌ Qualification Not Matched")

        # ================= ATS Score =================

        matched_skills, missing_skills, score = calculate_score(
            resume_skills,
            job_skills
        )

        st.subheader("📊 ATS Score")

        st.metric(
            label="Overall Match",
            value=f"{score:.2f}%"
        )

        st.progress(int(score))

        if score >= 80:
            st.success("🎉 Excellent Resume Match!")

        elif score >= 60:
            st.warning("👍 Good Match. Improve the missing skills.")

        else:
            st.error("⚠️ Low ATS Score. Improve your resume.")

        # ================= Matched Skills =================

        st.subheader("✅ Matched Skills")

        for skill in matched_skills:
            st.success(skill)

        # ================= Missing Skills =================

        st.subheader("❌ Missing Skills")

        for skill in missing_skills:
            st.error(skill)

        st.subheader("📈 Analysis Summary")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Matched Skills", len(matched_skills))

        with col2:
            st.metric("Missing Skills", len(missing_skills))

        with col3:
            st.metric("Qualifications", len(matched_qualification))

        st.subheader("💪 Resume Strength")

        strengths = []

        if len(matched_skills) >= 5:
            strengths.append("Strong technical skill set")

        if matched_qualification:
            strengths.append("Qualification matches the job requirements")

        if score >= 80:
            strengths.append("High ATS compatibility")

        if strengths:
            for strength in strengths:
                st.success("✔ " + strength)
        else:
            st.warning("No major strengths identified.")

        # ================= Recommendations =================

        recommendations = get_recommendations(missing_skills)

        st.subheader("📚 Recommendations")

        for recommendation in recommendations:
            st.info(recommendation)

        # ================= Resume Verdict =================

        st.subheader("🏆 Final Resume Verdict")

        if score >= 80 and matched_qualification:
            st.success("🎯 Excellent Candidate - Recommended for Interview")

        elif score >= 60:
            st.warning("👍 Good Candidate - Improve missing skills for a better match.")

        else:
            st.error("📌 Resume needs improvement before applying.")

        st.success("🎉 Resume analysis completed successfully!")
        st.subheader("📋 Candidate Summary")

        st.write(f"🎯 ATS Score : {score:.2f}%")

        st.write(f"✅ Matched Skills : {len(matched_skills)}")

        st.write(f"❌ Missing Skills : {len(missing_skills)}")

        if matched_qualification:
            st.write("🎓 Qualification : Matched ✅")
        else:
            st.write("🎓 Qualification : Not Matched ❌")
        st.subheader("🏆 Final Verdict")

        if score >= 80 and matched_qualification:
            st.success(
        "Excellent Match! The candidate satisfies the required qualification and possesses most of the required technical skills."
        )

        elif score >= 60:
            st.warning(
        "Good Match! The candidate has potential but should improve the missing skills."
        )

        else:
            st.error(
        "Needs Improvement. The candidate should improve both skills and overall profile before applying."
        )
        st.divider()

        st.caption("🤖 AI Resume Screener")
        st.caption("Developed using Python • Streamlit • PyMuPDF")