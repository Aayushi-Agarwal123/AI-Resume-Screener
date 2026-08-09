import "./AIInsights.css";

type Props = {
  topCandidate: any;
};

function AIInsights({ topCandidate }: Props) {

  if (!topCandidate) return null;

  return (
    <section className="ai-insights">

      <h2>🤖 AI Hiring Insights</h2>

      <div className="insight-card">

        <h3>{topCandidate.candidate}</h3>

        <p>
          ATS Score :
          <strong> {topCandidate.ats_score}%</strong>
        </p>

        <p>
          Skills Matched :
          <strong>
            {" "}
            {topCandidate.matched_skills.length}
          </strong>
        </p>

        <p>
          Missing Skills :
          <strong>
            {" "}
            {topCandidate.missing_skills.length}
          </strong>
        </p>

        <p>

          {topCandidate.recommendations.join(", ")}

        </p>

      </div>

    </section>
  );
}

export default AIInsights;