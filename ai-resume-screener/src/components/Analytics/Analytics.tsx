import "./Analytics.css";


type Props = {
  totalCandidates: number;
  averageScore: number;
  highest: any;
  lowest: any;
  qualified: number;
};


function Analytics({
  totalCandidates,
  averageScore,
  highest,
  lowest,
  qualified
}: Props) {


  return (

    <section className="analytics">

      <h2>
        📊 Recruitment Analytics
      </h2>


      <div className="analytics-grid">

        <div className="analytics-card">

          <h3>
            Total Candidates
          </h3>

          <h1>
            {totalCandidates}
          </h1>

        </div>


        <div className="analytics-card">

          <h3>
            Average ATS
          </h3>

          <h1>
            {averageScore}%
          </h1>

        </div>


        <div className="analytics-card">

          <h3>
            Highest ATS
          </h3>

          <h1>
            {highest
              ? highest.ats_score
              : 0}%
          </h1>

          <p>
            {highest?.candidate || "No candidate"}
          </p>

        </div>


        <div className="analytics-card">

          <h3>
            Lowest ATS
          </h3>

          <h1>
            {lowest
              ? lowest.ats_score
              : 0}%
          </h1>

          <p>
            {lowest?.candidate || "No candidate"}
          </p>

        </div>


        <div className="analytics-card">

          <h3>
            Qualified Candidates
          </h3>

          <h1>
            {qualified}
          </h1>

          <p>
            ATS ≥ 70%
          </p>

        </div>

      </div>

    </section>

  );

}


export default Analytics;