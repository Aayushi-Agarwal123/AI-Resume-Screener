import "./Hero.css";
import HeroLeft from "./HeroLeft";
import HeroRight from "./HeroRight";

function Hero() {
  return (

    <section className="hero">
    <div className="hero-grid"></div>


  <div className="hero-glow glow1"></div>

  <div className="hero-glow glow2"></div>

      <div className="hero-container">

        <HeroLeft />

        <HeroRight />

      </div>

    </section>
  );
}

export default Hero;