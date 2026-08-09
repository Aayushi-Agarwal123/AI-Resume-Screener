
import "./ActivityFeed.css";

type Props = {
  candidates: any[];
};

function ActivityFeed({ candidates }: Props) {
  return (
    <section className="activity">

      <h2>📝 Recent Analysis</h2>

      <div className="activity-list">

        {candidates.map((candidate, index) => (

          <div
            className="activity-card"
            key={index}
          >

            <h3>{candidate.candidate}</h3>

            <p>
              ATS Score :
              <strong> {Number(candidate.ats_score).toFixed(2)}%</strong>
            </p>

            <p>

              Status :

              <span
                className={
                  candidate.ats_score >= 80
                    ? "strong-match"
                    : candidate.ats_score >= 60
                    ? "potential-match"
                    : "needs-review"
                }
              >

                {candidate.ats_score >= 80
                  ? "Strong Match"
                  : candidate.ats_score >= 60
                  ? "Potential Match"
                  : "Needs Review"}

              </span>

            </p>

          </div>

        ))}

      </div>

    </section>
  );
}

export default ActivityFeed;
