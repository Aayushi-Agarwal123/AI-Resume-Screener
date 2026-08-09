import "./UploadJD.css";
import { useState } from "react";
import {
  FiClipboard,
  FiUploadCloud,
  FiFileText,
} from "react-icons/fi";

type UploadJDProps = {
  jobDescription: string;
  setJobDescription: React.Dispatch<
    React.SetStateAction<string>
  >;
};

function UploadJD({
  jobDescription,
  setJobDescription,
}: UploadJDProps) {

  const [activeTab, setActiveTab] =
    useState<"paste" | "upload">("paste");

  const [jdFile, setJdFile] =
    useState<File | null>(null);

  return (
    <div className="jd-card">

      <h2>Job Description</h2>

      <p>
        Paste your Job Description or upload a PDF.
      </p>

      {/* TABS */}

      <div className="jd-tabs">

        <button
          type="button"
          className={
            activeTab === "paste"
              ? "active"
              : ""
          }
          onClick={() =>
            setActiveTab("paste")
          }
        >
          <FiClipboard />
          Paste Job Description
        </button>

        <button
          type="button"
          className={
            activeTab === "upload"
              ? "active"
              : ""
          }
          onClick={() =>
            setActiveTab("upload")
          }
        >
          <FiUploadCloud />
          Upload PDF
        </button>

      </div>


      {/* PASTE JOB DESCRIPTION */}

      {activeTab === "paste" && (

        <textarea
          placeholder="Paste complete Job Description here..."
          value={jobDescription}
          onChange={(e) =>
            setJobDescription(
              e.target.value
            )
          }
        />

      )}


      {/* UPLOAD JOB DESCRIPTION PDF */}

      {activeTab === "upload" && (

        <label className="jd-upload">

          <FiUploadCloud size={40} />

          <span>
            Upload Job Description PDF
          </span>

          <input
            type="file"
            hidden
            accept=".pdf"
            onChange={(e) => {

              const file =
                e.target.files?.[0];

              if (file) {
                setJdFile(file);
              }

            }}
          />

        </label>

      )}


      {/* SHOW SELECTED PDF */}

      {jdFile && (

        <div className="jd-file">

          <FiFileText />

          <span>
            {jdFile.name}
          </span>

        </div>

      )}

    </div>
  );
}

export default UploadJD;