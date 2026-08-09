import "./RecruiterToolbar.css";
import {
  FiSearch,
  FiDownload,
  FiFileText,
  FiFilter,
} from "react-icons/fi";

function RecruiterToolbar() {
  return (
    <div className="toolbar">

      <div className="search-box">

        <FiSearch />

        <input
          type="text"
          placeholder="Search candidate..."
        />

      </div>

      <div className="toolbar-actions">

        <select>

          <option>All Candidates</option>
          <option>Hire</option>
          <option>Shortlist</option>
          <option>Review</option>

        </select>

        <button>

          <FiFileText />

          Export PDF

        </button>

        <button>

          <FiDownload />

          Export CSV

        </button>

      </div>

    </div>
  );
}

export default RecruiterToolbar;