import "./CandidateList.css";

type Candidate = {
  candidate: string;
  ats_score: number;
  matched_skills: string[];
  missing_skills?: string[];
  resume_skills?: string[];
};

type Props = {
  candidates: Candidate[];
  selected: number;
  setSelected: (index: number) => void;
  onView?: (candidate: Candidate) => void;
};

function CandidateList({
  candidates,
  selected,
  setSelected,
  onView,
}: Props) {

  return (
    <section>

      <h2>📂 All Candidates</h2>

      <p className="candidate-count">
        {candidates.length} candidates analyzed
      </p>

      <div className="candidate-grid">

        {candidates.map((c, index) => {

          const matchedSkills = c.matched_skills ?? [];
          const missingSkills = c.missing_skills ?? [];

          return (

            <div
              key={`${c.candidate}-${index}`}
              className={
                selected === index
                  ? "candidate-card active"
                  : "candidate-card"
              }
              onClick={() => setSelected(index)}
            >

              <h3 title={c.candidate}>
                {c.candidate}
              </h3>

              <p className="candidate-number">
                Candidate #{index + 1}
              </p>


              {/* ATS SCORE */}

              <div>

                <span className="ats-label">
                  🏅 ATS Score
                </span>

                <span className="ats-score">
                  {Number(c.ats_score || 0).toFixed(2)}%
                </span>

              </div>


              {/* MATCHED COUNT */}

              <p className="skills-info">
                ✓ {matchedSkills.length} Skills Matched
              </p>


              {/* MATCHED SKILLS */}

              {matchedSkills.length > 0 && (

                <div className="skill-tags">

                  {matchedSkills.map((skill) => (

                    <span
                      className="skill-tag matched"
                      key={skill}
                    >
                      ✓ {skill}
                    </span>

                  ))}

                </div>

              )}
              


              {/* MISSING COUNT */}

              <p className="missing-info">
                ⚠ {missingSkills.length} Missing
              </p>


              {/* MISSING SKILLS */}

              {missingSkills.length > 0 && (

                <div className="skill-tags">

                  {missingSkills.map((skill) => (

                    <span
                      className="skill-tag missing"
                      key={skill}
                    >
                      ⚠ {skill}
                    </span>

                  ))}

                </div>

              )}


              {/* VIEW BUTTON */}

              <button
                type="button"
                onClick={(event) => {

                  event.stopPropagation();

                  if (onView) {
                    onView(c);
                  }

                }}
              >
                👁 View Details
              </button>

            </div>

          );

        })}

      </div>

    </section>
  );
}

export default CandidateList;