import "./ATSCharts.css";

type Candidate = {
  candidate: string;
  ats_score: number;
};

type Props = {
  data: Candidate[];
};

function ATSChart({ data }: Props) {
  if (!data || data.length === 0) {
    return null;
  }

  return (
    <section className="ats-chart">

      <div className="chart-header">
        <h2>📈 Candidate ATS Analysis</h2>

        <p>
          ATS score comparison of all analyzed candidates
        </p>
      </div>

      <div className="chart-list">

        {data.map((candidate, index) => (

          <div
            className="chart-row"
            key={`${candidate.candidate}-${index}`}
          >

            <div className="chart-name">

              <span>
                #{index + 1}
              </span>

              <strong>
                {candidate.candidate}
              </strong>

            </div>

            <div className="chart-bar-container">

              <div
                className="chart-bar"
                style={{
                  width: `${Math.min(
                    Math.max(candidate.ats_score, 0),
                    100
                  )}%`,
                }}
              />

            </div>

            <strong className="chart-score">
              {candidate.ats_score}%
            </strong>

          </div>

        ))}

      </div>

      <div className="chart-footer">

        <span>
          🟢 Higher score = stronger match
        </span>

        <span>
          Total analyzed: {data.length}
        </span>

      </div>

    </section>
  );
}

export default ATSChart;