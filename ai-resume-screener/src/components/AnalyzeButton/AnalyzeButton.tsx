import "./AnalyzeButton.css";
import { FiCpu, FiArrowRight } from "react-icons/fi";

type AnalyzeButtonProps = {
  onAnalyze: () => void;
};

function AnalyzeButton({
  onAnalyze
}: AnalyzeButtonProps) {

  return (

    <div className="analyze-container">

      <button
        type="button"
        className="analyze-button"
        onClick={onAnalyze}
      >

        <FiCpu className="cpu-icon" />

        <span>
          Analyze Candidates
        </span>

        <FiArrowRight
          className="arrow-icon"
        />

      </button>


      <p className="analyze-text">
        AI will rank candidates automatically
        in a few seconds.
      </p>

    </div>

  );

}

export default AnalyzeButton;
