import "./Loading.css";
import { FiCpu, FiCheckCircle } from "react-icons/fi";

function Loading() {
  return (
    <div className="loading-overlay">

      <div className="loading-card">

        <div className="loading-icon">
          <FiCpu />
        </div>

        <h2>AI Resume Analysis</h2>

        <p>Analyzing candidates with AI...</p>

        <div className="progress">

          <div className="progress-fill"></div>

        </div>

        <div className="steps">

          <div className="step">
            <FiCheckCircle />
            Parsing Resume
          </div>

          <div className="step">
            <FiCheckCircle />
            Extracting Skills
          </div>

          <div className="step">
            <FiCheckCircle />
            Matching Job Description
          </div>

          <div className="step">
            <FiCheckCircle />
            Ranking Candidates
          </div>

          <div className="step">
            <FiCheckCircle />
            Generating ATS Report
          </div>

        </div>

      </div>

    </div>
  );
}

export default Loading;