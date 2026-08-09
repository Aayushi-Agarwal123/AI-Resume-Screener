import "./HiringDecision.css";
import {
  FiCheckCircle,
  FiStar,
} from "react-icons/fi";

function HiringDecision() {

  return (

    <section className="decision-card">

      <div className="decision-left">

        <FiCheckCircle className="decision-icon"/>

        <div>

          <h2>AI Hiring Decision</h2>

          <p>
            Candidate is highly recommended
            for Technical Interview.
          </p>

        </div>

      </div>

      <div className="decision-right">

        <div>

          <span>Overall Match</span>

          <h3>94%</h3>

        </div>

        <div>

          <span>Confidence</span>

          <h3>98%</h3>

        </div>

      </div>

      <div className="decision-footer">

        <FiStar/>

        Strong React • Node • MongoDB

      </div>

    </section>

  );

}

export default HiringDecision;