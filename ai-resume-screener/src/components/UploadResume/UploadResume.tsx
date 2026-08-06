import "./UploadResume.css";

type UploadResumeProps = {
  resumeFile: File | null;
  setResumeFile: React.Dispatch<React.SetStateAction<File | null>>;
};

function UploadResume({
  resumeFile,
  setResumeFile,
}: UploadResumeProps) {

  const handleFileChange = (
    e: React.ChangeEvent<HTMLInputElement>
  ) => {

    const file = e.target.files?.[0];

    if(file){
      setResumeFile(file);
    }

  };

  return (

    <div className="upload-card">

      <label className="upload-box">

        <input
          type="file"
          hidden
          accept=".pdf,.doc,.docx"
          onChange={handleFileChange}
        />

        <div className="upload-circle">
          📄
        </div>

        <h2>Upload Resume</h2>

        <p>
          Drag & Drop or Click to Upload
        </p>

        {resumeFile && (
          <div className="file-name">
            ✅ {resumeFile.name}
          </div>
        )}

      </label>

    </div>

  );

}

export default UploadResume;