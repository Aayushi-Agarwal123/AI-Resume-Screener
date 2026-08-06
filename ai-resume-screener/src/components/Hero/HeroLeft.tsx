import { FiArrowRight } from "react-icons/fi";
import { FaRobot } from "react-icons/fa";

function HeroLeft() {
  return (
    <div className="hero-left">

      <div className="hero-badge">
        <FaRobot />
        AI Powered Recruitment
      </div>

      <h1 className="hero-title">
        Smart Resume
        <br />
        <span>Screening</span>
        <br />
        with AI
      </h1>

      <p className="hero-description">
        Screen hundreds of resumes in seconds using AI. Match candidates
        with job descriptions, calculate ATS scores, identify skill gaps,
        and rank applicants instantly.
      </p>

      <div className="hero-buttons">

        <button className="primary-btn">
          Upload Resume
          <FiArrowRight />
        </button>

        <button className="secondary-btn">
          Upload Job Description
        </button>

      </div>

    </div>
  );
}

export default HeroLeft;