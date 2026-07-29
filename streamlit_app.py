import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
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
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- Session State ---------------- #

if "results" not in st.session_state:
    st.session_state.results = []

if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

# ---------------- Custom CSS ---------------- #

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"]  {
    font-family: 'Inter', sans-serif;
}

.block-container{
    padding-top:1.5rem;
    padding-bottom:3rem;
    max-width:1200px;
}

/* ---------- Headings ---------- */
h1{
    background: linear-gradient(90deg, #818CF8, #38BDF8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight:800;
}
h2, h3{
    color:#E2E8F0;
    font-weight:700;
}

/* ---------- Hero banner ---------- */
.hero-card{
    background: linear-gradient(135deg, rgba(129,140,248,0.15), rgba(56,189,248,0.08));
    border:1px solid rgba(129,140,248,0.35);
    border-radius:18px;
    padding:26px 30px;
    margin-bottom:22px;
}
.hero-title{
    font-size:30px;
    font-weight:800;
    background: linear-gradient(90deg, #A5B4FC, #67E8F9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom:6px;
}
.hero-sub{
    color:#94A3B8;
    font-size:15px;
    margin-bottom:16px;
}
.feature-pill{
    display:inline-block;
    background:rgba(255,255,255,0.06);
    border:1px solid rgba(255,255,255,0.12);
    color:#CBD5E1;
    padding:6px 14px;
    border-radius:999px;
    font-size:13px;
    margin:4px 6px 4px 0;
}

/* ---------- Metric cards ---------- */
div[data-testid="stMetric"]{
    background:linear-gradient(160deg,#111827,#0B1220);
    padding:18px;
    border-radius:16px;
    border:1px solid #262f42;
    box-shadow:0 4px 14px rgba(0,0,0,0.25);
}
div[data-testid="stMetricLabel"]{
    color:#94A3B8;
}

/* ---------- Buttons ---------- */
div.stButton>button{
    width:100%;
    height:52px;
    border-radius:12px;
    font-size:17px;
    font-weight:700;
    background: linear-gradient(90deg,#6366F1,#0EA5E9);
    color:white;
    border:none;
    letter-spacing:0.3px;
    transition:all 0.2s ease;
}
div.stButton>button:hover{
    filter:brightness(1.1);
    transform:translateY(-1px);
    box-shadow:0 6px 18px rgba(99,102,241,0.35);
}

/* ---------- Download buttons ---------- */
div.stDownloadButton>button{
    border-radius:10px;
    font-weight:600;
    border:1px solid #334155;
}

/* ---------- Section card wrapper ---------- */
.section-card{
    background:#0F172A;
    border:1px solid #1E293B;
    border-radius:16px;
    padding:20px 22px;
    margin-bottom:18px;
}

/* ---------- Skill chips ---------- */
.chip-container{
    display:flex;
    flex-wrap:wrap;
    gap:8px;
    margin:8px 0 4px 0;
}
.chip{
    padding:6px 14px;
    border-radius:999px;
    font-size:13px;
    font-weight:600;
    white-space:nowrap;
}
.chip-match{
    background:rgba(34,197,94,0.12);
    color:#4ADE80;
    border:1px solid rgba(74,222,128,0.35);
}
.chip-missing{
    background:rgba(244,63,94,0.12);
    color:#FB7185;
    border:1px solid rgba(251,113,133,0.35);
}
.chip-neutral{
    background:rgba(56,189,248,0.12);
    color:#38BDF8;
    border:1px solid rgba(56,189,248,0.35);
}
.chip-qual{
    background:rgba(129,140,248,0.14);
    color:#A5B4FC;
    border:1px solid rgba(165,180,252,0.35);
}

/* ---------- Candidate name badge ---------- */
.rank-badge{
    display:inline-block;
    font-size:13px;
    font-weight:700;
    padding:3px 10px;
    border-radius:8px;
    margin-right:8px;
}
.badge-excellent{background:rgba(34,197,94,0.15); color:#4ADE80;}
.badge-good{background:rgba(250,204,21,0.15); color:#FACC15;}
.badge-poor{background:rgba(244,63,94,0.15); color:#FB7185;}

/* ---------- Expander header polish ---------- */
div[data-testid="stExpander"]{
    border-radius:14px;
    border:1px solid #1E293B;
    background:#0B1220;
}

/* ---------- Verdict banner ---------- */
.verdict-banner{
    border-radius:14px;
    padding:16px 20px;
    font-weight:600;
    font-size:15px;
    margin:10px 0;
}
.verdict-good{ background:rgba(34,197,94,0.10); border:1px solid rgba(74,222,128,0.35); color:#4ADE80;}
.verdict-mid{ background:rgba(250,204,21,0.10); border:1px solid rgba(250,204,21,0.35); color:#FACC15;}
.verdict-bad{ background:rgba(244,63,94,0.10); border:1px solid rgba(251,113,133,0.35); color:#FB7185;}

hr{
    border-color:#1E293B !important;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#0B1220;
    border-right:1px solid #1E293B;
}

</style>
""", unsafe_allow_html=True)


def render_chips(items, style="chip-neutral"):
    """Render a list of strings as rounded chips instead of stacked full-width boxes."""
    if not items:
        st.caption("None found.")
        return
    html = '<div class="chip-container">'
    for item in items:
        html += f'<span class="chip {style}">{item}</span>'
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)


def score_verdict(score):
    if score >= 80:
        return "verdict-good", "🎉 Excellent Resume Match"
    elif score >= 60:
        return "verdict-mid", "👍 Good Match — a few gaps to close"
    else:
        return "verdict-bad", "⚠️ Needs Improvement"


def rank_badge(score):
    if score >= 80:
        return "badge-excellent", "Excellent"
    elif score >= 60:
        return "badge-good", "Good"
    else:
        return "badge-poor", "Needs Work"


# ---------------- Hero Header ---------------- #

st.markdown("""
<div class="hero-card">
    <div class="hero-title">🤖 AI Resume Screener & Candidate Ranking System</div>
    <div class="hero-sub">Analyze multiple resumes against a Job Description using AI-powered ATS scoring, skill matching, and qualification checks.</div>
    <span class="feature-pill">📄 Multi-Resume Upload</span>
    <span class="feature-pill">🎯 ATS Score</span>
    <span class="feature-pill">🎓 Qualification Match</span>
    <span class="feature-pill">📊 Dashboard Analytics</span>
    <span class="feature-pill">🏆 Candidate Ranking</span>
    <span class="feature-pill">📄 PDF Report</span>
    <span class="feature-pill">📥 CSV Export</span>
</div>
""", unsafe_allow_html=True)

# ---------------- Sidebar ---------------- #

with st.sidebar:

    st.markdown("### 📌 How it works")

    steps = [
        ("1", "Upload one or more resumes"),
        ("2", "Paste the Job Description"),
        ("3", "Click Analyze Resume"),
        ("4", "Compare & rank candidates"),
        ("5", "Download PDF / CSV report"),
    ]
    for num, text in steps:
        st.markdown(
            f"""<div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">
            <div style="background:linear-gradient(135deg,#6366F1,#0EA5E9);min-width:26px;height:26px;border-radius:50%;
            display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;color:white;">{num}</div>
            <div style="color:#CBD5E1;font-size:14px;">{text}</div>
            </div>""",
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)
    st.divider()

    st.markdown(
        """
        <div style="text-align:center;font-size:12px;color:#64748B;padding-top:10px;">
        🤖 <b>AI Resume Screener</b><br>
        Made by <b>Aayushi Agarwal</b>
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------- Inputs ---------------- #

st.markdown('<div class="section-card">', unsafe_allow_html=True)

col_a, col_b = st.columns([1, 1])

with col_a:
    st.markdown("#### 📄 Upload Resumes")
    resumes = st.file_uploader(
        "Upload one or more PDF resumes",
        type=["pdf"],
        accept_multiple_files=True,
        label_visibility="collapsed"
    )

with col_b:
    st.markdown("#### 📋 Job Description")
    jd = st.text_area(
        "Paste Job Description",
        height=180,
        placeholder="Paste the Job Description here...",
        label_visibility="collapsed"
    )

st.markdown('</div>', unsafe_allow_html=True)

analyze = st.button("🚀 Analyze Resume", use_container_width=True)

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

            st.markdown("## 📋 Candidate Analysis")

            # Resume Loop

            for resume in resumes:

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

                badge_class, badge_label = rank_badge(score)

                # ---------------- Candidate Card ---------------- #

                with st.expander(
                    f"👤  {resume.name}   •   ATS {score:.2f}%   •   {badge_label}",
                    expanded=False
                ):

                    top_c1, top_c2, top_c3 = st.columns(3)
                    with top_c1:
                        st.metric("ATS Score", f"{score:.2f}%")
                    with top_c2:
                        st.metric("Matched Skills", len(matched_skills))
                    with top_c3:
                        st.metric("Missing Skills", len(missing_skills))

                    st.progress(min(int(score), 100))

                    v_class, v_text = score_verdict(score)
                    st.markdown(
                        f'<div class="verdict-banner {v_class}">{v_text}</div>',
                        unsafe_allow_html=True
                    )

                    tab_skills, tab_qual, tab_reco, tab_coach = st.tabs(
                        ["🛠 Skills", "🎓 Qualification", "📚 Recommendations", "🤖 AI Coach"]
                    )

                    with tab_skills:
                        sk1, sk2 = st.columns(2)
                        with sk1:
                            st.markdown("**✅ Matched Skills**")
                            render_chips(matched_skills, "chip-match")
                        with sk2:
                            st.markdown("**❌ Missing Skills**")
                            render_chips(missing_skills, "chip-missing")

                        st.markdown("---")
                        sk3, sk4 = st.columns(2)
                        with sk3:
                            st.markdown("**🛠 All Resume Skills**")
                            render_chips(resume_skills, "chip-neutral")
                        with sk4:
                            st.markdown("**📋 All Job Skills**")
                            render_chips(job_skills, "chip-neutral")

                    with tab_qual:
                        q1, q2 = st.columns(2)
                        with q1:
                            st.markdown("**🎓 Resume Qualification**")
                            render_chips(resume_qualification, "chip-qual")
                        with q2:
                            st.markdown("**📚 Required Qualification**")
                            render_chips(job_qualification, "chip-qual")

                        st.markdown("")
                        if matched_qualification:
                            st.success("✅ Qualification Matched")
                        else:
                            st.error("❌ Qualification Not Matched")

                    with tab_reco:
                        recommendations = get_recommendations(missing_skills)
                        if recommendations:
                            render_chips(recommendations, "chip-neutral")
                        else:
                            st.success("✅ No recommendations. All required skills are present.")

                    with tab_coach:
                        feedback = generate_ai_feedback(
                            score,
                            matched_skills,
                            missing_skills,
                            matched_qualification
                        )
                        st.markdown(feedback)

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

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("## 📊 Dashboard Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("👥 Candidates", total_candidates)

    with col2:
        st.metric("⭐ Highest ATS", f"{highest_score:.2f}%")

    with col3:
        st.metric("📈 Average ATS", f"{average_score:.2f}%")

    with col4:
        st.metric("🎓 Qualified", qualified_candidates)

    st.markdown("<br>", unsafe_allow_html=True)

    # ================= Best Candidate ================= #

    st.markdown("## 🥇 Best Candidate")

    st.markdown(f"""
    <div class="section-card" style="border:1px solid rgba(74,222,128,0.35);">
        <div style="font-size:18px;font-weight:700;color:#4ADE80;margin-bottom:10px;">
            🏆 {best_candidate['Candidate']}
        </div>
        <div style="display:flex;gap:24px;flex-wrap:wrap;color:#CBD5E1;font-size:14px;">
            <div>⭐ ATS Score: <b>{best_candidate['Score']:.2f}%</b></div>
            <div>🎓 Qualification: <b>{best_candidate['Qualification']}</b></div>
            <div>🚀 Status: <b>{best_candidate['Status']}</b></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ================= Search & Filter ================= #

    st.markdown("## 🔍 Search & Filter")

    sf1, sf2 = st.columns([2, 1])
    with sf1:
        search = st.text_input("Search Candidate Name", placeholder="Type a candidate name...")
    with sf2:
        status_filter = st.selectbox(
            "Filter by Status",
            ["All", "Excellent", "Good", "Needs Improvement"]
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

    # ================= Comparison Table ================= #

    st.markdown("## 📋 Candidate Comparison")

    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )

    # ================= Candidate Ranking ================= #

    st.markdown("## 🏆 Candidate Ranking")

    for index, candidate in enumerate(results, start=1):

        if index == 1:
            medal = "🥇"
        elif index == 2:
            medal = "🥈"
        elif index == 3:
            medal = "🥉"
        else:
            medal = f"#{index}"

        badge_class, badge_label = rank_badge(candidate["Score"])

        with st.expander(f"{medal}  {candidate['Candidate']}  •  {badge_label}"):

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric("ATS", f"{candidate['Score']:.2f}%")
            with c2:
                st.metric("Matched Skills", candidate["Matched Skills"])
            with c3:
                st.metric("Missing Skills", candidate["Missing Skills"])

            st.markdown(f"🎓 **Qualification:** {candidate['Qualification']}")
            st.markdown(f"📌 **Status:** {candidate['Status']}")

    # ================= ATS Score Chart ================= #

    st.markdown("## 📊 ATS Score Comparison")

    fig = px.bar(
        filtered_df,
        x="Candidate",
        y="Score",
        color="Status",
        text="Score",
        title=None,
        color_discrete_map={
            "Excellent": "#4ADE80",
            "Good": "#FACC15",
            "Needs Improvement": "#FB7185"
        }
    )

    fig.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside"
    )

    fig.update_layout(
        yaxis_range=[0, 100],
        xaxis_title="Candidates",
        yaxis_title="ATS Score (%)",
        height=460,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#CBD5E1"),
        legend_title_text="Status"
    )

    st.plotly_chart(fig, use_container_width=True)

    # ================= Status Distribution ================= #

    st.markdown("## 🥧 Candidate Status Distribution")

    pie = px.pie(
        filtered_df,
        names="Status",
        hole=0.55,
        color="Status",
        color_discrete_map={
            "Excellent": "#4ADE80",
            "Good": "#FACC15",
            "Needs Improvement": "#FB7185"
        }
    )

    pie.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#CBD5E1"),
        height=420
    )

    st.plotly_chart(pie, use_container_width=True)

    # ================= Downloads ================= #

    st.markdown("## 📥 Download Reports")

    dl1, dl2 = st.columns(2)

    csv = filtered_df.to_csv(index=False)

    with dl1:
        st.download_button(
            label="📥 Download CSV Report",
            data=csv,
            file_name="Candidate_Report.csv",
            mime="text/csv",
            use_container_width=True
        )

    pdf_file = generate_report(
        results,
        best_candidate,
        total_candidates,
        highest_score,
        average_score,
        qualified_candidates
    )

    with open(pdf_file, "rb") as file:
        with dl2:
            st.download_button(
                label="📄 Download Hiring Report (PDF)",
                data=file,
                file_name="Hiring_Report.pdf",
                mime="application/pdf",
                use_container_width=True
            )

    # ================= Report Information ================= #

    st.markdown(f"""
    <div class="section-card">
        <div style="color:#94A3B8;font-size:13px;">
        📅 Report Generated: <b style="color:#E2E8F0;">{datetime.now().strftime("%d %B %Y | %I:%M %p")}</b><br>
        📊 Total Candidates: <b style="color:#E2E8F0;">{total_candidates}</b><br>
        🏆 Best Candidate: <b style="color:#E2E8F0;">{best_candidate['Candidate']}</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ================= Footer ================= #

    st.markdown("""
    <div style="text-align:center;color:#64748B;font-size:13px;padding-top:10px;">
        <b style="color:#94A3B8;">🤖 AI Resume Screener & Candidate Ranking System</b><br>
        Developed using 🐍 Python • ⚡ Streamlit • 📊 Plotly • 📄 ReportLab<br>
        © 2026 Aayushi Agarwal
    </div>
    """, unsafe_allow_html=True)