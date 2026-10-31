
import "./App.css";
import { useState } from "react";

import UploadResume from "./components/UploadResume/UploadResume";
import UploadJD from "./components/UploadJD/UploadJD";
import AnalyzeButton from "./components/AnalyzeButton/AnalyzeButton";
import Loading from "./components/Loading/Loading";

import CandidateList from "./components/CandidateList/CandidateList";
import Comparison from "./components/Comparison/Comparison";
import RankingTable from "./components/RankingTable/RankingTable";
import TopCandidate from "./components/TopCandidate/TopCandidate";
import Analytics from "./components/Analytics/Analytics";
import Results from "./components/Results/Results";
import AIInsights from "./components/AIInsights/AIInsights";
import ActivityFeed from "./components/ActivityFeed/ActivityFeed";
import ReportDownload from "./components/ReportDownload/ReportDownload";

import NotificationBell from "./components/NotificationBell/NotificationBell";
import CandidateDrawer from "./components/CandidateDrawer/CandidateDrawer";

import ATSChart from "./components/Charts/ATSCharts";

function App() {
  const [resumeFiles, setResumeFiles] = useState<File[]>([]);
  const [jobDescription, setJobDescription] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<any>(null);
  const [selectedCandidate, setSelectedCandidate] = useState(0);
  const [drawerOpen, setDrawerOpen] = useState(false);
  const [drawerCandidate, setDrawerCandidate] = useState<any>(null);

  // ANALYZE — existing backend logic preserved
  const handleAnalyze = async () => {
    console.log("🚀 ANALYZE STARTED");

    if (resumeFiles.length === 0) {
      alert("Please upload at least one resume.");
      return;
    }

    if (jobDescription.trim() === "") {
      alert("Please enter Job Description.");
      return;
    }

    setLoading(true);

    const formData = new FormData();

    resumeFiles.forEach((file) => {
      formData.append("resumes", file);
    });

    formData.append("job_description", jobDescription);

    try {
      console.log("📤 Sending request to FastAPI...");

      const controller = new AbortController();

      const timeoutId = setTimeout(() => {
        controller.abort();
      }, 60000);

      const response = await fetch(
        "https://ai-resume-screener-ynpp.onrender.com/analyze",
        {
          method: "POST",
          body: formData,
          signal: controller.signal,
        }
      );

      clearTimeout(timeoutId);

      console.log("📥 Response:", response.status);

      const responseText = await response.text();

      console.log("📦 Backend response:", responseText);

      if (!response.ok) {
        throw new Error(
          `Backend Error ${response.status}: ${responseText}`
        );
      }

      let data;

      try {
        data = JSON.parse(responseText);
      } catch {
        throw new Error("Backend returned invalid JSON.");
      }

      console.log("✅ DATA:", data);

      if (data.success === false) {
        throw new Error(
          data.error || "No resume could be analyzed."
        );
      }

      if (!data.ranking || !Array.isArray(data.ranking)) {
        throw new Error(
          "Backend did not return ranking data."
        );
      }

      if (data.ranking.length === 0) {
        throw new Error("No candidates found.");
      }

      setResult(data);
      setSelectedCandidate(0);
      setDrawerCandidate(data.ranking[0]);

      console.log("🎉 RESULTS LOADED");

    } catch (error: any) {
      console.error("❌ ANALYZE ERROR:", error);

      if (error?.name === "AbortError") {
        alert(
          "Backend took too long to respond. Check FastAPI terminal."
        );
      } else {
        alert(
          error?.message || "Something went wrong."
        );
      }

    } finally {
      setLoading(false);
      console.log("🏁 ANALYSIS FINISHED");
    }
  };

  const handleSelectCandidate = (index: number) => {
    setSelectedCandidate(index);
  };

  const handleViewCandidate = (candidate: any) => {
    setDrawerCandidate(candidate);
    setDrawerOpen(true);
  };

  // DASHBOARD DATA
  const ranking = result?.ranking ?? [];

  const totalCandidates = Number(
    result?.total_candidates ?? ranking.length ?? 0
  );

  const averageScore = Number(
    result?.average_ats_score ?? 0
  );

  const qualifiedCount = Number(
    result?.qualified ??
    ranking.filter((c: any) => Number(c.ats_score) >= 70).length
  );

  const topCandidateName =
    result?.top_candidate?.candidate ??
    ranking[0]?.candidate ??
    "Awaiting analysis";

  return (
    <div className="app-shell">

      {/* SIDEBAR */}
      <aside className="sidebar">

        <a className="brand" href="#overview" aria-label="AI Resume Screener home">
          <span className="brand-mark">AI</span>
          <span className="brand-copy">
            <strong>Talent<span>IQ</span></strong>
            <small>RESUME INTELLIGENCE</small>
          </span>
        </a>

        <div className="sidebar-label">WORKSPACE</div>

        <nav className="side-nav" aria-label="Main navigation">
          <a className="active" href="#overview">
            <span>▦</span> Overview
          </a>
          <a href="#screening">
            <span>＋</span> New screening
          </a>
          <a href="#candidates">
            <span>♙</span> Candidates
          </a>
          <a href="#analytics">
            <span>▥</span> Analytics
          </a>
          <a href="#reports">
            <span>▤</span> Reports
          </a>
        </nav>

        <div className="sidebar-label sidebar-label-spaced">
          PREFERENCES
        </div>

        <nav className="side-nav">
          <a href="#screening">
            <span>⚙</span> Screening setup
          </a>
          <a href="#help">
            <span>?</span> Help & support
          </a>
        </nav>

        <div className="sidebar-bottom">
          <div className="sidebar-help-icon">✦</div>
          <strong>Smarter hiring starts here</strong>
          <p>
            Screen resumes, compare talent and make confident decisions.
          </p>
          <a href="#screening">
            Start screening <span>→</span>
          </a>
        </div>

        <div className="sidebar-user">
          <div className="user-avatar">HR</div>
          <div>
            <strong>Recruiter workspace</strong>
            <small>Hiring team</small>
          </div>
          <span className="user-menu">•••</span>
        </div>

      </aside>

      {/* MAIN DASHBOARD */}
      <main className="dashboard-main">

        {/* TOP NAVIGATION */}
        <header className="topbar">
          <div className="breadcrumb">
            Workspace <span>/</span> <strong>Overview</strong>
          </div>

          <div className="topbar-actions">
            <div className="system-status">
              <i /> Screening system ready
            </div>

            <button
              className="icon-action"
              type="button"
              aria-label="Notifications"
            >
              ♧
            </button>

            <div className="topbar-profile">
              <div className="user-avatar">HR</div>
              <div>
                <strong>Recruiter</strong>
                <small>Administrator</small>
              </div>
            </div>
          </div>
        </header>

        <div className="dashboard-content">

          {result && (
            <div className="dashboard-notification">
              <NotificationBell
                total={result.total_candidates}
                top={result.top_candidate?.candidate || "N/A"}
                average={result.average_ats_score}
              />
            </div>
          )}

          {/* WELCOME */}
          <section className="welcome-row" id="overview">
            <div>
              <div className="eyebrow">
                RECRUITMENT WORKSPACE
              </div>
              <h1>Dashboard overview</h1>
              <p>
                Track your screening activity and discover the strongest candidates.
              </p>
            </div>

            <a className="primary-action" href="#screening">
              <span>＋</span> New screening
            </a>
          </section>

          {/* KPI CARDS */}
          <section className="metric-grid" aria-label="Recruitment metrics">

            <article className="metric-card">
              <div className="metric-top">
                <span>Total candidates</span>
                <span className="metric-icon blue">♙</span>
              </div>
              <div className="metric-value">
                {totalCandidates}
              </div>
              <div className="metric-foot">
                <span className="metric-dot blue-dot" />
                Resumes analyzed
              </div>
            </article>

            <article className="metric-card">
              <div className="metric-top">
                <span>Average ATS score</span>
                <span className="metric-icon purple">◉</span>
              </div>
              <div className="metric-value">
                {averageScore.toFixed(1)}<small>%</small>
              </div>
              <div className="metric-foot">
                <span className="metric-dot purple-dot" />
                Candidate match average
              </div>
            </article>

            <article className="metric-card">
              <div className="metric-top">
                <span>Shortlisted</span>
                <span className="metric-icon green">✓</span>
              </div>
              <div className="metric-value">
                {qualifiedCount}
              </div>
              <div className="metric-foot">
                <span className="metric-dot green-dot" />
                ATS score 70% or higher
              </div>
            </article>

            <article className="metric-card">
              <div className="metric-top">
                <span>Top candidate</span>
                <span className="metric-icon amber">★</span>
              </div>
              <div
                className="metric-value metric-name"
                title={topCandidateName}
              >
                {topCandidateName}
              </div>
              <div className="metric-foot">
                <span className="metric-dot amber-dot" />
                {result
                  ? `${Number(
                      result.top_candidate?.ats_score ??
                      ranking[0]?.ats_score ??
                      0
                    ).toFixed(1)}% ATS match`
                  : "Waiting for first screening"}
              </div>
            </article>

          </section>

          {/* NEW SCREENING */}
          <section className="screening-workspace" id="screening">

            <div className="section-heading">
              <div>
                <div className="eyebrow">GET STARTED</div>
                <h2>New resume screening</h2>
                <p>
                  Upload resumes and add a job description to evaluate candidate fit.
                </p>
              </div>

              <span className="secure-label">
                <i /> Secure workspace
              </span>
            </div>

            <div className="screening-grid">

              <div className="screening-panel resume-panel">
                <div className="panel-heading">
                  <span className="step-number">01</span>
                  <div>
                    <h3>Upload resumes</h3>
                    <p>Add multiple candidate files</p>
                  </div>
                </div>

                <UploadResume
                  resumeFiles={resumeFiles}
                  setResumeFiles={setResumeFiles}
                />
              </div>

              <div className="screening-panel jd-panel">
                <div className="panel-heading">
                  <span className="step-number">02</span>
                  <div>
                    <h3>Job description</h3>
                    <p>Define the role requirements</p>
                  </div>
                </div>

                <UploadJD
                  jobDescription={jobDescription}
                  setJobDescription={setJobDescription}
                />
              </div>

            </div>

            <div className="screening-submit">
              <div>
                <strong>Ready to evaluate candidates?</strong>
                <span>
                  {resumeFiles.length} resume(s) added ·{" "}
                  {jobDescription.trim()
                    ? "Job description provided"
                    : "Job description required"}
                </span>
              </div>

              <AnalyzeButton onAnalyze={handleAnalyze} />
            </div>

            {loading && <Loading />}

          </section>

          {/* RESULTS */}
          {result && ranking.length > 0 && (
            <>

              <section className="results-section" id="candidates">
                <div className="section-heading">
                  <div>
                    <div className="eyebrow">YOUR TALENT POOL</div>
                    <h2>Candidate overview</h2>
                    <p>
                      Review candidate matches and open profiles for more detail.
                    </p>
                  </div>
                  <span className="result-count">
                    {ranking.length} analyzed
                  </span>
                </div>

                <CandidateList
                  candidates={ranking}
                  selected={selectedCandidate}
                  setSelected={handleSelectCandidate}
                  onView={handleViewCandidate}
                />
              </section>

              <section className="results-section" id="analytics">
                <div className="section-heading">
                  <div>
                    <div className="eyebrow">PERFORMANCE</div>
                    <h2>Recruitment analytics</h2>
                    <p>
                      Insights calculated from the resumes processed in this screening.
                    </p>
                  </div>
                </div>

                <Analytics
                  totalCandidates={result.total_candidates}
                  averageScore={result.average_ats_score}
                  highest={result.highest}
                  lowest={result.lowest}
                  qualified={result.qualified}
                />

                <div className="analytics-lower-grid">
                  <ATSChart data={ranking} />
                  <TopCandidate candidate={result.top_candidate} />
                </div>
              </section>

              <section className="results-section" id="ranking">
                <RankingTable
                  candidates={ranking}
                  onView={handleViewCandidate}
                />

                <Comparison candidates={ranking} />

                {ranking[selectedCandidate] && (
                  <Results
                    atsScore={ranking[selectedCandidate].ats_score}
                    matchedSkills={ranking[selectedCandidate].matched_skills}
                    missingSkills={ranking[selectedCandidate].missing_skills}
                    recommendation={ranking[selectedCandidate].recommendations?.join(", ")}
                  />
                )}
              </section>

              <section className="results-section extra-results" id="reports">
                <AIInsights topCandidate={result.top_candidate} />
                <ActivityFeed candidates={ranking} />
                <ReportDownload candidates={ranking} />
              </section>

            </>
          )}

          {!result && !loading && (
            <section className="empty-dashboard" id="help">
              <div className="empty-illustration">✧</div>
              <div>
                <strong>Your candidate insights will appear here</strong>
                <p>
                  Complete your first screening to see candidate rankings,
                  ATS analytics and hiring recommendations.
                </p>
              </div>
              <a href="#screening">
                Start your first screening →
              </a>
            </section>
          )}

          <footer className="dashboard-footer">
            <span>TalentIQ · AI Resume Screener</span>
            <span>Recruitment intelligence workspace</span>
          </footer>

        </div>

        <CandidateDrawer
          open={drawerOpen}
          candidate={drawerCandidate}
          onClose={() => setDrawerOpen(false)}
        />

      </main>
    </div>
  );
}

export default App;
