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
              <strong> {candidate.ats_score}%</strong>
            </p>

            <p>

              Status :

              <span
                className={
                  candidate.ats_score >= 85
                    ? "hire"
                    : candidate.ats_score >= 70
                    ? "shortlist"
                    : "review"
                }
              >

                {candidate.ats_score >= 85
                  ? "Hire"
                  : candidate.ats_score >= 70
                  ? "Shortlist"
                  : "Review"}

              </span>

            </p>

          </div>

        ))}

      </div>

    </section>

  );

}

export default ActivityFeed;