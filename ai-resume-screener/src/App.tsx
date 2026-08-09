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


  // =====================================================
  // ANALYZE
  // =====================================================

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


    formData.append(
      "job_description",
      jobDescription
    );


    try {

      console.log(
        "📤 Sending request to FastAPI..."
      );


      const controller =
        new AbortController();


      const timeoutId =
        setTimeout(() => {

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


      console.log(
        "📥 Response:",
        response.status
      );


      const responseText =
        await response.text();


      console.log(
        "📦 Backend response:",
        responseText
      );


      if (!response.ok) {

        throw new Error(
          `Backend Error ${response.status}: ${responseText}`
        );

      }


      let data;


      try {

        data = JSON.parse(responseText);

      } catch {

        throw new Error(
          "Backend returned invalid JSON."
        );

      }


      console.log(
        "✅ DATA:",
        data
      );


      if (data.success === false) {

        throw new Error(
          data.error ||
          "No resume could be analyzed."
        );

      }


      if (
        !data.ranking ||
        !Array.isArray(data.ranking)
      ) {

        throw new Error(
          "Backend did not return ranking data."
        );

      }


      if (
        data.ranking.length === 0
      ) {

        throw new Error(
          "No candidates found."
        );

      }


      // -----------------------------------------------
      // SAVE RESULT
      // -----------------------------------------------

      setResult(data);

      setSelectedCandidate(0);

      setDrawerCandidate(
        data.ranking[0]
      );


      console.log(
        "🎉 RESULTS LOADED"
      );


    } catch (error: any) {

      console.error(
        "❌ ANALYZE ERROR:",
        error
      );


      if (
        error?.name === "AbortError"
      ) {

        alert(
          "Backend took too long to respond. Check FastAPI terminal."
        );

      } else {

        alert(
          error?.message ||
          "Something went wrong."
        );

      }


    } finally {

      setLoading(false);

      console.log(
        "🏁 ANALYSIS FINISHED"
      );

    }

  };


  // =====================================================
  // SELECT CANDIDATE
  // =====================================================

  const handleSelectCandidate = (
    index: number
  ) => {

    setSelectedCandidate(index);

  };


  // =====================================================
  // VIEW CANDIDATE
  // =====================================================

  const handleViewCandidate = (
    candidate: any
  ) => {

    setDrawerCandidate(candidate);

    setDrawerOpen(true);

  };


  // =====================================================
  // UI
  // =====================================================

  return (

    <div className="app">


      <div className="background-grid"></div>

      <div className="glow glow1"></div>

      <div className="glow glow2"></div>


      {/* ================================================
          NOTIFICATION
      ================================================= */}

      {result && (

        <NotificationBell

          total={
            result.total_candidates
          }

          top={
            result.top_candidate?.candidate ||
            "N/A"
          }

          average={
            result.average_ats_score
          }

        />

      )}


      <div className="container">


        {/* ==============================================
            HERO
        =============================================== */}

        <div className="hero">

          <h1>
            🤖 AI Resume Screener
          </h1>

          <p>
            Upload multiple resumes,
            compare candidates,
            rank applicants and
            generate AI hiring reports.
          </p>

        </div>


        {/* ==============================================
            RESUME UPLOAD
        =============================================== */}

        <UploadResume

          resumeFiles={resumeFiles}

          setResumeFiles={setResumeFiles}

        />


        {/* ==============================================
            JOB DESCRIPTION
        =============================================== */}

        <UploadJD

          jobDescription={jobDescription}

          setJobDescription={setJobDescription}

        />


        {/* ==============================================
            ANALYZE BUTTON
        =============================================== */}

        <AnalyzeButton

          onAnalyze={handleAnalyze}

        />


        {/* ==============================================
            LOADING
        =============================================== */}

        {loading && (

          <Loading />

        )}


        {/* ==============================================
            RESULTS
        =============================================== */}

        {result &&
          result.ranking &&
          result.ranking.length > 0 && (

          <>


            {/* CANDIDATE LIST */}

            <CandidateList

              candidates={result.ranking}

              selected={selectedCandidate}

              setSelected={
                handleSelectCandidate
              }

              onView={
                handleViewCandidate
              }

            />


            {/* COMPARISON */}

            <Comparison

              candidates={result.ranking}

            />


            {/* RANKING */}

            <RankingTable

              candidates={result.ranking}

              onView={
                handleViewCandidate
              }

            />


            {/* TOP CANDIDATE */}

            <TopCandidate

              candidate={
                result.top_candidate
              }

            />


            {/* ANALYTICS */}

            <Analytics

              totalCandidates={
                result.total_candidates
              }

              averageScore={
                result.average_ats_score
              }

              highest={
                result.highest
              }

              lowest={
                result.lowest
              }

              qualified={
                result.qualified
              }

            />


            {/* ATS CHART */}

            <ATSChart

              data={result.ranking}

            />


            {/* SELECTED CANDIDATE */}

            {result.ranking[
              selectedCandidate
            ] && (

              <Results

                atsScore={
                  result.ranking[
                    selectedCandidate
                  ].ats_score
                }

                matchedSkills={
                  result.ranking[
                    selectedCandidate
                  ].matched_skills
                }

                missingSkills={
                  result.ranking[
                    selectedCandidate
                  ].missing_skills
                }

                recommendation={

                  result.ranking[
                    selectedCandidate
                  ]
                    .recommendations
                    ?.join(", ")

                }

              />

            )}


            {/* AI INSIGHTS */}

            <AIInsights

              topCandidate={
                result.top_candidate
              }

            />


            {/* ACTIVITY */}

            <ActivityFeed

              candidates={
                result.ranking
              }

            />


            {/* REPORT */}

            <ReportDownload

              candidates={
                result.ranking
              }

            />

          </>

        )}


        {/* ==============================================
            DRAWER
        =============================================== */}

        <CandidateDrawer

          open={drawerOpen}

          candidate={drawerCandidate}

          onClose={() =>
            setDrawerOpen(false)
          }

        />


      </div>

    </div>

  );

}


export default App;

