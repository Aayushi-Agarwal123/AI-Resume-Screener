import Dashboard from "./Dashboard";
import FloatingCard from "./Floatingcard";

function HeroRight() {
  return (
    <div className="hero-right">
      <Dashboard />

      <FloatingCard
        title="Resume Uploaded"
        subtitle="Resume.pdf"
        className="card-top"
      />

      <FloatingCard
        title="AI Processing"
        subtitle="Matching Skills..."
        className="card-left"
      />

      <FloatingCard
        title="Analysis Complete"
        subtitle="ATS Score Ready"
        className="card-bottom"
      />
    </div>
  );
}

export default HeroRight;