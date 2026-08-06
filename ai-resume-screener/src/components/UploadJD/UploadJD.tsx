import "./UploadJD.css";

type UploadJDProps = {
  jobDescription: string;
  setJobDescription: React.Dispatch<React.SetStateAction<string>>;
};

function UploadJD({
  jobDescription,
  setJobDescription,
}: UploadJDProps) {
  return (
    <div className="jd-card">

      <div className="jd-header">
        <h2>📋 Job Description</h2>

        <span>{jobDescription.length} Characters</span>
      </div>

      <textarea
        placeholder="Paste complete Job Description here..."
        value={jobDescription}
        onChange={(e) => setJobDescription(e.target.value)}
      />

    </div>
  );
}

export default UploadJD;