import "./CandidateDrawer.css";
import {
  FiUser,
  FiDownload,
  FiAward,
  FiBriefcase,
  FiBookOpen,
  FiX,
} from "react-icons/fi";

type Props = {
  open: boolean;
  onClose: () => void;
  candidate: any;
};

function CandidateDrawer({
  open,
  onClose,
  candidate,
}: Props) {

  if (!candidate) return null;

  return (

    <div className={`drawer ${open ? "show" : ""}`}>

      <div className="drawer-header">

        <h2>Candidate Profile</h2>

        <button onClick={onClose}>
          <FiX />
        </button>

      </div>

      <div className="candidate-profile">

        <div className="avatar">
          <FiUser />
        </div>

        <h3>{candidate.candidate}</h3>

        <span>AI Resume Analysis</span>

      </div>

      <div className="drawer-info">

        <div>
          <span>
            <FiAward /> ATS Score
          </span>

          <strong>{candidate.ats_score}%</strong>
        </div>

        <div>
          <span>
            <FiBriefcase /> Experience
          </span>

          <strong>
            {candidate.experience || "Fresher"}
          </strong>
        </div>

        <div>
          <span>
            <FiBookOpen /> Education
          </span>

          <strong>
            {candidate.education || "Not Available"}
          </strong>
        </div>

      </div>

      <div className="drawer-section">

        <h4>Matched Skills</h4>

        <div className="drawer-skills">

          {(candidate.matched_skills || []).map(
            (skill: string) => (
              <span key={skill}>{skill}</span>
            )
          )}

        </div>

      </div>

      <div className="drawer-section">

        <h4>Missing Skills</h4>

        <div className="drawer-skills">

          {(candidate.missing_skills || []).map(
            (skill: string) => (
              <span
                className="missing"
                key={skill}
              >
                {skill}
              </span>
            )
          )}

        </div>

      </div>

      <div className="drawer-section">

        <h4>AI Recommendation</h4>

        <p>
          {(candidate.recommendations || []).join(", ")}
        </p>

      </div>

      <button
        className="download-btn"
        onClick={() =>
          alert("Resume download will be connected with backend.")
        }
      >
        <FiDownload />
        Download Resume
      </button>

    </div>

  );
}

export default CandidateDrawer;