import "./Results.css";

function Results() {
  return (
    <div className="results-card">

      <div className="score-section">

        <div className="score-circle">
          <span>86%</span>
        </div>

        <div>
          <h2>ATS Score</h2>
          <p>Excellent Match</p>
        </div>

      </div>

      <div className="progress-bar">

        <div className="progress-fill"></div>

      </div>

      <div className="skills-section">

        <div className="skills-box">

          <h3>✅ Matched Skills</h3>

          <div className="tags">

            <span>React</span>
            <span>Node.js</span>
            <span>MongoDB</span>
            <span>JavaScript</span>

          </div>

        </div>

        <div className="skills-box">

          <h3>❌ Missing Skills</h3>

          <div className="tags">

            <span>Docker</span>
            <span>AWS</span>
            <span>Redis</span>

          </div>

        </div>

      </div>

      <div className="recommendation">

        ⭐ Strong candidate. Resume matches most job requirements.

      </div>

    </div>
  );
}

export default Results;