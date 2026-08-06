import "./App.css";
import { useState } from "react";

import UploadResume from "./components/UploadResume/UploadResume";
import UploadJD from "./components/UploadJD/UploadJD";
import AnalyzeButton from "./components/AnalyzeButton/AnalyzeButton";
import Results from "./components/Results/Results";

function App() {
  const [resumeFile, setResumeFile] = useState<File | null>(null);
  const [jobDescription, setJobDescription] = useState("");

  return (
    <div className="app">

      <div className="background-grid"></div>

      <div className="glow glow1"></div>
      <div className="glow glow2"></div>

      <div className="container">

        <div className="hero">

          <h1>🤖 AI Resume Screener</h1>

          <p>
            Upload your Resume, paste the Job Description and
            let AI calculate ATS score, skill match and hiring recommendations.
          </p>

        </div>

        <UploadResume
          resumeFile={resumeFile}
          setResumeFile={setResumeFile}
        />

        <UploadJD
          jobDescription={jobDescription}
          setJobDescription={setJobDescription}
        />

        <AnalyzeButton />

        <Results />

      </div>

    </div>
  );
}

export default App;