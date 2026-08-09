import "./Comparison.css";

type Candidate = {
  candidate: string;
  ats_score: number;
  matched_skills?: string[];
  missing_skills?: string[];
  recommendations?: string[];
  education?: string;
  experience?: string;
};

type Props = {
  candidates: Candidate[];
};

function Comparison({ candidates }: Props) {
  if (!candidates || candidates.length === 0) {
    return (
      <section className="comparison-section">
        <div className="comparison-header">
          <div>
            <h2>⚖️ Candidate Comparison</h2>
            <p>No candidates available for comparison.</p>
          </div>
        </div>
      </section>
    );
  }

  return (
    <section className="comparison-section">

      {/* HEADER */}
      <div className="comparison-header">
        <div>
          <h2>⚖️ Candidate Comparison</h2>
          <p>
            Compare candidates based on ATS score, skills and experience
          </p>
        </div>

        <div className="candidate-count">
          {candidates.length} Candidates
        </div>
      </div>

      {/* CANDIDATE CARDS */}
      <div className="comparison-grid">

        {candidates.map((candidate, index) => {

          const matchedSkills =
            candidate.matched_skills ?? [];

          const missingSkills =
            candidate.missing_skills ?? [];

          const recommendations =
            candidate.recommendations ?? [];

          const score =
            Math.min(
              Math.max(candidate.ats_score ?? 0, 0),
              100
            );

          return (

            <div
              className={`comparison-card ${
                index === 0
                  ? "best-comparison-card"
                  : ""
              }`}
              key={`${candidate.candidate}-${index}`}
            >

              {/* RANK */}
              <div className="comparison-rank">
                {index === 0
                  ? "🏆 #1"
                  : `#${index + 1}`}
              </div>

              {/* NAME */}
              <h3 className="comparison-name">
                {candidate.candidate}
              </h3>

              {/* ATS SCORE */}
              <div className="comparison-score">

                <span>
                  ATS Score
                </span>

                <strong>
                  {score.toFixed(1)}%
                </strong>

              </div>

              {/* PROGRESS */}
              <div className="comparison-progress">

                <div
                  className="comparison-progress-fill"
                  style={{
                    width: `${score}%`,
                  }}
                />

              </div>

              {/* BASIC INFORMATION */}
              <div className="comparison-info">

                <div>

                  <span>
                    🎓 Education
                  </span>

                  <strong>
                    {candidate.education ||
                      "Not Available"}
                  </strong>

                </div>

                <div>

                  <span>
                    💼 Experience
                  </span>

                  <strong>
                    {candidate.experience ||
                      "Not Available"}
                  </strong>

                </div>

              </div>

              {/* MATCHED SKILLS */}
              <div className="skill-box matched-box">

                <div className="skill-title">

                  <span>✅</span>

                  <strong>
                    Matched Skills
                  </strong>

                  <small>
                    {matchedSkills.length}
                  </small>

                </div>

                {matchedSkills.length > 0 ? (

                  <div className="skill-list">

                    {matchedSkills.map(
                      (skill) => (

                        <span
                          className="skill-tag matched-tag"
                          key={skill}
                        >
                          {skill}
                        </span>

                      )
                    )}

                  </div>

                ) : (

                  <p className="empty-skill">
                    No matched skills
                  </p>

                )}

              </div>

              {/* MISSING SKILLS */}
              <div className="skill-box missing-box">

                <div className="skill-title">

                  <span>⚠️</span>

                  <strong>
                    Missing Skills
                  </strong>

                  <small>
                    {missingSkills.length}
                  </small>

                </div>

                {missingSkills.length > 0 ? (

                  <div className="skill-list">

                    {missingSkills.map(
                      (skill) => (

                        <span
                          className="skill-tag missing-tag"
                          key={skill}
                        >
                          {skill}
                        </span>

                      )
                    )}

                  </div>

                ) : (

                  <p className="empty-skill">
                    No missing skills 🎉
                  </p>

                )}

              </div>

              {/* RECOMMENDATIONS */}
              {recommendations.length > 0 && (

                <div className="recommendation-box">

                  <div className="recommendation-title">
                    🤖 AI Recommendation
                  </div>

                  {recommendations.map(
                    (recommendation, recommendationIndex) => (

                      <p
                        key={recommendationIndex}
                      >
                        • {recommendation}
                      </p>

                    )
                  )}

                </div>

              )}

            </div>

          );

        })}

      </div>

    </section>
  );
}

export default Comparison;