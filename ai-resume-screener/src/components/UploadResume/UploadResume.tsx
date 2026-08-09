import "./UploadResume.css";

type UploadResumeProps = {
  resumeFiles: File[];
  setResumeFiles: React.Dispatch<React.SetStateAction<File[]>>;
};

function UploadResume({
  resumeFiles,
  setResumeFiles,
}: UploadResumeProps) {
  const handleFiles = (
    e: React.ChangeEvent<HTMLInputElement>
  ) => {
    if (!e.target.files) return;

    const files = Array.from(e.target.files);

    setResumeFiles((prev) => [...prev, ...files]);
  };

  const removeFile = (index: number) => {
    setResumeFiles((prev) =>
      prev.filter((_, i) => i !== index)
    );
  };

  return (
    <div className="upload-card">

      <label className="upload-area">

        <input
          type="file"
          multiple
          accept=".pdf,.doc,.docx"
          hidden
          onChange={handleFiles}
        />

        <h2>📂 Upload Resumes</h2>

        <p>
          Drag & Drop or Click to upload multiple resumes
        </p>

      </label>

      {resumeFiles.length > 0 && (

        <div className="resume-list">

          <h3>
            Uploaded Resumes ({resumeFiles.length})
          </h3>

          {resumeFiles.map((file, index) => (

            <div className="resume-item" key={index}>

              <span>
                📄 {file.name}
              </span>

              <button
                onClick={() => removeFile(index)}
              >
                ✖
              </button>

            </div>

          ))}

        </div>

      )}

    </div>
  );
}

export default UploadResume;