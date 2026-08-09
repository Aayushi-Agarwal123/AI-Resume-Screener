import "./Stats.css";
import {
  FiUsers,
  FiAward,
  FiCheckCircle,
  FiXCircle,
} from "react-icons/fi";

function Stats() {

  const cards = [

    {
      title:"Total Resumes",
      value:128,
      icon:<FiUsers />,
      color:"blue"
    },

    {
      title:"Average ATS",
      value:"82%",
      icon:<FiAward />,
      color:"purple"
    },

    {
      title:"Selected",
      value:24,
      icon:<FiCheckCircle />,
      color:"green"
    },

    {
      title:"Rejected",
      value:67,
      icon:<FiXCircle />,
      color:"red"
    }

  ];

  return (

    <section className="stats">

      {cards.map((card,index)=>(

        <div
          key={index}
          className={`stat-card ${card.color}`}
        >

          <div className="icon">

            {card.icon}

          </div>

          <h2>{card.value}</h2>

          <p>{card.title}</p>

        </div>

      ))}

    </section>

  );

}

export default Stats;