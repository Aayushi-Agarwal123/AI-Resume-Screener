import "./RecruiterStats.css";
import {
  FiUsers,
  FiAward,
  FiTrendingUp,
  FiClock,
  FiCheckCircle,
  FiTarget,
} from "react-icons/fi";

function RecruiterStats() {
  const stats = [
    {
      title: "Total Resumes",
      value: "128",
      sub: "+12 Today",
      icon: <FiUsers />,
    },
    {
      title: "Highest ATS",
      value: "96%",
      sub: "Excellent",
      icon: <FiAward />,
    },
    {
      title: "Average ATS",
      value: "81%",
      sub: "Above Average",
      icon: <FiTrendingUp />,
    },
    {
      title: "Shortlisted",
      value: "42",
      sub: "Ready to Interview",
      icon: <FiCheckCircle />,
    },
    {
      title: "Selection Rate",
      value: "33%",
      sub: "Current Batch",
      icon: <FiTarget />,
    },
    {
      title: "Avg Screening",
      value: "4.2s",
      sub: "Per Resume",
      icon: <FiClock />,
    },
  ];

  return (
    <section className="recruiter-stats">

      {stats.map((item, index) => (

        <div className="recruiter-card" key={index}>

          <div className="card-top">

            <div className="stat-icon">
              {item.icon}
            </div>

            <span>{item.title}</span>

          </div>

          <h2>{item.value}</h2>

          <p>{item.sub}</p>

        </div>

      ))}

    </section>
  );
}

export default RecruiterStats;