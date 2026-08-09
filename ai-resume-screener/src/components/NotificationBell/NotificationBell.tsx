import "./NotificationBell.css";
import { FiBell } from "react-icons/fi";
import { useState } from "react";

type Props = {
  total: number;
  top: string;
  average: number;
};

function NotificationBell({
  total,
  top,
  average,
}: Props) {

  const [open, setOpen] = useState(false);

  return (

    <div className="notification-bell">

      <div
        className="bell-icon"
        onClick={() => setOpen(!open)}
      >
        <FiBell />
        <span className="badge">4</span>
      </div>

      {open && (

        <div className="notification-dropdown">

          <h3>Notifications</h3>

          <div className="notification-item">
            ✅ Analysis Completed
          </div>

          <div className="notification-item">
            👥 {total} Candidates Analyzed
          </div>

          <div className="notification-item">
            🥇 Top Candidate
            <br />
            <strong>{top}</strong>
          </div>

          <div className="notification-item">
            📊 Average ATS
            <br />
            <strong>{average}%</strong>
          </div>

        </div>

      )}

    </div>

  );

}

export default NotificationBell;