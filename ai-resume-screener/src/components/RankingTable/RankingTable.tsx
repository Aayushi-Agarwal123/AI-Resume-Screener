import "./RankingTable.css";
import {
  FiAward,
  FiCheckCircle,
  FiStar,
} from "react-icons/fi";

type Props = {
  candidates: any[];
  onView: (candidate: any) => void;
};

function RankingTable({
  candidates,
  onView,
}: Props) {
  return (
    <section className="ranking">

      <div className="ranking-header">
        <h2>
          <FiAward />
          Candidate Ranking
        </h2>

      
      </div>

      <table>

        <thead>
          <tr>
            <th>Rank</th>
            <th>Candidate</th>
            <th>ATS</th>
            <th>Status</th>
            <th>Details</th>
          </tr>
        </thead>

        <tbody>

          {candidates.map((c, index) => (

            <tr key={index}>

              <td>
                {index === 0
                  ? "🥇"
                  : index === 1
                  ? "🥈"
                  : index === 2
                  ? "🥉"
                  : index + 1}
              </td>

              <td>
                <FiStar /> {c.candidate}
              </td>

              <td>{c.ats_score.toFixed(1)}%</td>

              <td>

                <span className="hire">

                  <FiCheckCircle />

                  {c.ats_score >= 85
                    ? "Hire"
                    : c.ats_score >= 70
                    ? "Shortlist"
                    : "Review"}

                </span>

              </td>

              <td>

                <button
                  className="view-btn"
                  onClick={() => onView(c)}
                >
                  View Details
                </button>

              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </section>
  );
}

export default RankingTable;