import "./TopCandidate.css";
import { FiAward, FiDownload } from "react-icons/fi";

type Candidate = {
  candidate: string;
  ats_score: number;
  matched_skills: string[];
};

type Props = {
  candidate: Candidate | null;
};

function TopCandidate({ candidate }: Props) {

  if (!candidate) return null;

  return (

    <section className="top-candidate">

      <div className="candidate-glow"></div>

      <div className="candidate-left">

        <div className="badge">

          <FiAward />

          AI Top Candidate

        </div>

        <h2>{candidate.candidate}</h2>

        <p>

          Highest ATS Score among all uploaded resumes.

        </p>

        <div className="candidate-skills">

          {candidate.matched_skills.map((skill) => (

            <span key={skill}>{skill}</span>

          ))}

        </div>

      </div>

      <div className="candidate-right">

        <div className="score-circle">

          <div className="inner-circle">

            <h1>{candidate.ats_score.toFixed(1)}%</h1>

            <small>ATS</small>

          </div>

        </div>

        <button className="resume-btn">

          <FiDownload />

          Best Candidate

        </button>

      </div>

    </section>

  );

}

export default TopCandidate;