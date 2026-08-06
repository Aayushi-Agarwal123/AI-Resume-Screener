import {
  FaFileAlt,
  FaCheckCircle,
  FaChartLine,
} from "react-icons/fa";

function Dashboard() {
  return (
    <div className="dashboard">

      <div className="resume-preview">

        <FaFileAlt className="resume-icon" />

        <div>

          <h3>Resume.pdf</h3>

          <p>Uploaded Successfully</p>

        </div>

      </div>

      <div className="ats-box">

        <div>

          <span>ATS Score</span>

          <h2>92%</h2>

        </div>

        <div className="ats-ring">

          <div className="ats-inner">
            92%
          </div>

        </div>

      </div>

      <div className="skill-tags">

        <span><FaCheckCircle /> React</span>
        <span><FaCheckCircle /> TypeScript</span>
        <span><FaCheckCircle /> Node</span>
        <span><FaCheckCircle /> MongoDB</span>

      </div>

      <div className="analytics">

        <FaChartLine />

        <div>

          <h4>Candidate Ranking</h4>

          <p>#1 Best Match</p>

        </div>

      </div>

    </div>
  );
}

export default Dashboard;