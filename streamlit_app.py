import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

from parser.pdf_parser import extract_text
from preprocessing.text_cleaner import clean_text
from extractor.skills import extract_skills
from similarity.score import calculate_score
from recommadation.recommadate import get_recommendations
from extractor.Qualification import extract_qualification
from reports.pdf_reports import generate_report
from ai_resume_coach import generate_ai_feedback


# ---------------- Page Config ---------------- #

st.set_page_config(
    page_title="AI Resume Screener",
    page_icon="🤖",
    layout="wide"
)

# ---------------- Session State ---------------- #

if "results" not in st.session_state:
    st.session_state.results = []

if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

# ---------------- Custom CSS ---------------- #

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

h1,h2,h3{
    color:#4F8BF9;
}

div[data-testid="stMetric"]{
    background:#111827;
    padding:18px;
    border-radius:15px;
    border:1px solid #2f3542;
}

div.stButton>button{
    width:100%;
    height:55px;
    border-radius:12px;
    font-size:18px;
    font-weight:bold;
    background:#4F8BF9;
    color:white;
}

div.stButton>button:hover{
    background:#2563EB;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Title ---------------- #

st.title("🤖 AI Resume Screener & Candidate Ranking System")

st.markdown("""
Analyze multiple resumes against a Job Description using AI-powered ATS scoring.

### Features

- 📄 Multiple Resume Upload
- 🎯 ATS Score
- 🎓 Qualification Matching
- 📊 Dashboard Analytics
- 🏆 Candidate Ranking
- 📈 Charts
- 📄 PDF Report
- 📥 CSV Export

""")

# ---------------- Sidebar ---------------- #

with st.sidebar:

    st.header("📌 Instructions")

    st.info("""
1️⃣ Upload one or more resumes

2️⃣ Paste Job Description

3️⃣ Click Analyze Resume

4️⃣ Compare Candidates

5️⃣ Download PDF / CSV Report
""")

            
    

    st.markdown(
"""
<div style="
margin-top : 200px;
text-align:center;
font-size:11px;
color:#6B7280;
padding-bottom:5px;
">

🤖 AI Resume Screener

Made by <b>Aayushi Agarwal</b>

</div>
""",
unsafe_allow_html=True
)


# ---------------- Inputs ---------------- #

st.divider()

resumes = st.file_uploader(
    "📄 Upload Multiple Resumes",
    type=["pdf"],
    accept_multiple_files=True
)

jd = st.text_area(
    "📋 Job Description",
    height=250,
    placeholder="Paste Job Description Here..."
)

analyze = st.button(
    "🚀 Analyze Resume",
    use_container_width=True
)

# ---------------- Analysis ---------------- #

if analyze:

    if not resumes:
        st.error("Please upload at least one resume.")

    elif jd.strip() == "":
        st.error("Please paste the Job Description.")

    else:

        with st.spinner("Analyzing resumes..."):

            results = []

            cleaned_jd = clean_text(jd)

            job_skills = extract_skills(cleaned_jd)

            job_qualification = extract_qualification(cleaned_jd)

            # Resume Loop

            for resume in resumes:
                st.subheader(f"📄 Candidate : {resume.name}")

                resume_text = extract_text(resume)

                cleaned_resume = clean_text(resume_text)

                resume_skills = extract_skills(cleaned_resume)

                resume_qualification = extract_qualification(
                    cleaned_resume
                )

                matched_skills, missing_skills, score = calculate_score(
                    resume_skills,
                    job_skills
                )

                matched_qualification = []

                for qualification in resume_qualification:

                    if qualification in job_qualification:

                        matched_qualification.append(
                            qualification
                        )

                # ---------------- Candidate Card ---------------- #

                with st.expander(
                    f"👤 {resume.name} | ATS : {score:.2f}%"
                ):

                    col1, col2 = st.columns(2)

                    with col1:

                        st.subheader("🛠 Resume Skills")

                        st.write(resume_skills)

                    with col2:

                        st.subheader("📋 Job Skills")

                        st.write(job_skills)

                    st.divider()

                    col1, col2 = st.columns(2)

                    with col1:

                        st.subheader("🎓 Resume Qualification")

                        if resume_qualification:

                            for qualification in resume_qualification:

                                st.success(qualification)

                        else:

                            st.warning(
                                "No qualification found."
                            )

                    with col2:

                        st.subheader("📚 Required Qualification")

                        if job_qualification:

                            for qualification in job_qualification:

                                st.info(qualification)

                        else:

                            st.warning(
                                "No qualification mentioned."
                            )

                    st.divider()

                    st.subheader("📊 ATS Score")

                    st.metric(
                        "Overall Match",
                        f"{score:.2f}%"
                    )

                    st.progress(int(score))

                    if score >= 80:

                        st.success(
                            "🎉 Excellent Resume Match"
                        )

                    elif score >= 60:

                        st.warning(
                            "👍 Good Match"
                        )

                    else:

                        st.error(
                            "⚠ Needs Improvement"
                        )

                    st.divider()

                    st.subheader("✅ Matched Skills")

                    for skill in matched_skills:

                        st.success(skill)

                    st.subheader("❌ Missing Skills")

                    for skill in missing_skills:

                        st.error(skill)

                    recommendations = get_recommendations(
                        missing_skills
                    )

                    # ================= Recommendations =================

                    st.subheader("📚 Recommendations")

                    recommendations = get_recommendations(missing_skills)

                    if recommendations:

                        for recommendation in recommendations:
                                st.info(recommendation)

                    else:
                             st.success("✅ No recommendations. All required skills are present.")

# ================= AI Resume Coach =================

                    st.subheader("🤖 AI Resume Coach")

                    feedback = generate_ai_feedback(
                    score,
                    matched_skills,
                    missing_skills,
                    matched_qualification
)

                    st.info(feedback)

                       
                    
                        

                # ---------------- Save Result ---------------- #

                results.append({

                    "Rank": len(results) + 1,

                    "Candidate": resume.name,

                    "Score": score,

                    "Matched Skills": len(
                        matched_skills
                    ),

                    "Missing Skills": len(
                        missing_skills
                    ),

                    "Qualification":

                        "Matched"

                        if matched_qualification

                        else "Not Matched",

                    "Status":

                        "Excellent"

                        if score >= 80

                        else

                        "Good"

                        if score >= 60

                        else

                        "Needs Improvement"

                })

            # Resume Loop Finished

            st.session_state.results = results

            st.session_state.analysis_done = True

            # ================= Dashboard ================= #

if st.session_state.analysis_done:

    results = st.session_state.results

    results.sort(
        key=lambda x: x["Score"],
        reverse=True
    )

    total_candidates = len(results)

    highest_score = max(
        candidate["Score"]
        for candidate in results
    )

    average_score = sum(
        candidate["Score"]
        for candidate in results
    ) / total_candidates

    qualified_candidates = sum(
        1
        for candidate in results
        if candidate["Qualification"] == "Matched"
    )

    best_candidate = results[0]

    st.divider()

    st.header("📊 Dashboard Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "👥 Candidates",
            total_candidates
        )

    with col2:
        st.metric(
            "⭐ Highest ATS",
            f"{highest_score:.2f}%"
        )

    with col3:
        st.metric(
            "📈 Average ATS",
            f"{average_score:.2f}%"
        )

    with col4:
        st.metric(
            "🎓 Qualified",
            qualified_candidates
        )

    st.divider()

    # ================= Best Candidate ================= #

    st.header("🥇 Best Candidate")

    st.success(
        f"""
🏆 Candidate : {best_candidate['Candidate']}

⭐ ATS Score : {best_candidate['Score']:.2f}%

🎓 Qualification : {best_candidate['Qualification']}

🚀 Status : {best_candidate['Status']}
"""
    )

    st.divider()

    # ================= Search ================= #

    st.header("🔍 Search Candidate")

    search = st.text_input(
        "Search Candidate Name"
    )

    # ================= Filter ================= #

    status_filter = st.selectbox(

        "Filter by Status",

        [
            "All",
            "Excellent",
            "Good",
            "Needs Improvement"
        ]
    )

    df = pd.DataFrame(results)

    filtered_df = df.copy()

    if search:

        filtered_df = filtered_df[
            filtered_df["Candidate"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

    if status_filter != "All":

        filtered_df = filtered_df[
            filtered_df["Status"] == status_filter
        ]

    st.divider()

    # ================= Comparison Table ================= #

    st.header("📋 Candidate Comparison")

    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # ================= Candidate Ranking ================= #

    st.header("🏆 Candidate Ranking")

    for index, candidate in enumerate(results, start=1):

        if index == 1:
            medal = "🥇"

        elif index == 2:
            medal = "🥈"

        elif index == 3:
            medal = "🥉"

        else:
            medal = f"#{index}"

        with st.expander(
            f"{medal} {candidate['Candidate']}"
        ):

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric(
                    "ATS",
                    f"{candidate['Score']:.2f}%"
                )

            with c2:
                st.metric(
                    "Matched Skills",
                    candidate["Matched Skills"]
                )

            with c3:
                st.metric(
                    "Missing Skills",
                    candidate["Missing Skills"]
                )

            st.write(
                f"🎓 Qualification : {candidate['Qualification']}"
            )

            st.write(
                f"📌 Status : {candidate['Status']}"
            )

                # ================= ATS Score Chart ================= #

    st.divider()

    st.header("📊 ATS Score Comparison")

    fig = px.bar(
        filtered_df,
        x="Candidate",
        y="Score",
        color="Status",
        text="Score",
        title="Candidate ATS Score Comparison"
    )

    fig.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside"
    )

    fig.update_layout(
        yaxis_range=[0, 100],
        xaxis_title="Candidates",
        yaxis_title="ATS Score (%)",
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ================= Status Distribution ================= #

    st.header("🥧 Candidate Status Distribution")

    pie = px.pie(
        filtered_df,
        names="Status",
        title="Candidate Status"
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

    # ================= CSV Download ================= #

    st.divider()

    st.header("📥 Download Reports")

    csv = filtered_df.to_csv(index=False)

    st.download_button(
        label="📥 Download CSV Report",
        data=csv,
        file_name="Candidate_Report.csv",
        mime="text/csv"
    )

    # ================= PDF Download ================= #

    pdf_file = generate_report(
        results,
        best_candidate,
        total_candidates,
        highest_score,
        average_score,
        qualified_candidates
    )

    with open(pdf_file, "rb") as file:

        st.download_button(
            label="📄 Download Hiring Report (PDF)",
            data=file,
            file_name="Hiring_Report.pdf",
            mime="application/pdf"
        )

    # ================= Report Information ================= #

    st.divider()

    st.info(
        f"""
📅 Report Generated :

{datetime.now().strftime("%d %B %Y | %I:%M %p")}

📊 Total Candidates : {total_candidates}

🏆 Best Candidate : {best_candidate['Candidate']}
"""
    )

    # ================= Footer ================= #

    st.divider()

    st.markdown(
        """
<center>

### 🤖 AI Resume Screener & Candidate Ranking System

Developed using

🐍 Python • ⚡ Streamlit • 📊 Plotly • 📄 ReportLab

© 2026 Aayushi Agarwal

</center>
""",
        unsafe_allow_html=True
    )

                