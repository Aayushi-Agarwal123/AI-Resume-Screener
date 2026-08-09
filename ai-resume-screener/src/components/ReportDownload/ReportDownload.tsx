import "./ReportDownload.css";
import { FiDownload, FiFileText } from "react-icons/fi";

type Props = {
  candidates: any[];
};

function ReportDownload({ candidates }: Props) {

  const downloadReport = () => {

    const report = {
      generated: new Date().toISOString(),
      total_candidates: candidates.length,
      candidates: candidates,
    };

    const blob = new Blob(
      [JSON.stringify(report, null, 2)],
      {
        type: "application/json",
      }
    );

    const url = URL.createObjectURL(blob);

    const a = document.createElement("a");

    a.href = url;

    a.download = "ATS_Report.json";

    document.body.appendChild(a);

    a.click();

    document.body.removeChild(a);

    URL.revokeObjectURL(url);
  };

  return (
    <section className="report-download">

      <div className="report-icon">
        <FiFileText />
      </div>

      <h2>
        📄 Download AI Report
      </h2>

      <p>
        Download the complete candidate analysis,
        ATS scores, matched skills, missing skills
        and recommendations.
      </p>

      <button
        type="button"
        onClick={downloadReport}
      >
        <FiDownload />

        Download Candidate Report
      </button>

    </section>
  );
}

export default ReportDownload;