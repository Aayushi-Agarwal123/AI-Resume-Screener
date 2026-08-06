import "./Navbar.css";

function Navbar() {
  return (
    <header className="navbar">

      <div className="logo">
        Resume<span>AI</span>
      </div>

      <nav>

        <a href="#">Home</a>

        <a href="#">Features</a>

        <a href="#">About</a>

        <a href="#">Contact</a>

      </nav>

      <button className="login-btn">
        Get Started
      </button>

    </header>
  );
}

export default Navbar;