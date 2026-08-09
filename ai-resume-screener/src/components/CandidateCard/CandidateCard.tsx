import "./CandidateList.css";

type Candidate = {
  candidate: string;
  ats_score: number;
  matched_skills: string[];
  missing_skills: string[];
  recommendations: string[];
};

type Props = {
  candidates: Candidate[];
  onSelect: (candidate: Candidate) => void;
};

function CandidateList({ candidates, onSelect }: Props) {
  return (
    <section className="candidate-list">

      <h2>📂 All Candidates</h2>

      <div className="candidate-grid">

        {candidates.map((candidate, index) => (

          <div
            key={index}
            className="candidate-card"
            onClick={() => onSelect(candidate)}
          >

            <h3>{candidate.candidate}</h3>

            <div className="candidate-score">

              {candidate.ats_score.toFixed(1)}%

            </div>

            <p>

              Matched Skills :
              <strong>
                {" "}
                {candidate.matched_skills.length}
              </strong>

            </p>

            <p>

              Missing Skills :
              <strong>
                {" "}
                {candidate.missing_skills.length}
              </strong>

            </p>

          </div>

        ))}

      </div>

    </section>
  );
}

export default CandidateList;