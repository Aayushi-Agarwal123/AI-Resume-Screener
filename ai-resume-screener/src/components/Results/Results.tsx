import "./Results.css";

import {
  FiAward,
  FiTrendingUp,
  FiCheckCircle,
  FiAlertCircle,
  FiUserCheck,
} from "react-icons/fi";

type ResultsProps = {
  atsScore: number;
  matchedSkills: string[];
  missingSkills: string[];
  recommendation: string;
};

function Results({
  atsScore,
  matchedSkills,
  missingSkills,
  recommendation,
}: ResultsProps) {

  let hiringStatus = "Rejected";

  if (atsScore >= 85)
    hiringStatus = "Strong";

  else if (atsScore >= 70)
    hiringStatus = "Good";

  else if (atsScore >= 50)
    hiringStatus = "Average";

  return (

    <section className="results">

      <div className="stats-grid">

        <div className="stat-card">

          <FiAward />

          <h2>{atsScore.toFixed(1)}%</h2>

          <p>ATS Score</p>

        </div>

        <div className="stat-card">

          <FiTrendingUp />

          <h2>{matchedSkills.length}</h2>

          <p>Matched Skills</p>

        </div>

        <div className="stat-card">

          <FiUserCheck />

          <h2>{hiringStatus}</h2>

          <p>Hiring Status</p>

        </div>

      </div>

      <div className="results-grid">

        <div className="glass-card">

          <h3>✅ Matched Skills</h3>

          <div className="skills">

            {matchedSkills.length === 0 ? (

              <p>No matched skills.</p>

            ) : (

              matchedSkills.map((skill) => (

                <span key={skill}>

                  <FiCheckCircle />

                  {skill}

                </span>

              ))

            )}

          </div>

        </div>

        <div className="glass-card">

          <h3>⚠ Missing Skills</h3>

          <div className="skills">

            {missingSkills.length === 0 ? (

              <p>No missing skills 🎉</p>

            ) : (

              missingSkills.map((skill) => (

                <span className="missing" key={skill}>

                  <FiAlertCircle />

                  {skill}

                </span>

              ))

            )}

          </div>

        </div>

      </div>

      <div className="recommendation-card">

        <h3>🤖 AI Recommendation</h3>

        <p>{recommendation}</p>

      </div>

    </section>

  );

}

export default Results;