type Props = {
  title: string;
  subtitle: string;
  className: string;
};

function FloatingCard({
  title,
  subtitle,
  className,
}: Props) {
  return (
    <div className={`floating-card ${className}`}>

      <div className="floating-dot"></div>

      <div>

        <h4>{title}</h4>

        <p>{subtitle}</p>

      </div>

    </div>
  );
}

export default FloatingCard;