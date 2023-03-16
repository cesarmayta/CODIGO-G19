import { GiSettingsKnobs } from "react-icons/gi";
import { Link } from "react-router-dom";
import getStars from "../../utils/getStars";
import Stars from "../shared/Stars";

const CourseCard = ({ course }) => {
  const stars = getStars(course);
  return (
    <article className="card">
      <Link className="card-container" to={`/course/${course.curso_id}`}>
        <header className="card__header">
          <img
            className="card__img"
            width={340}
            height={178}
            src={course.curso_imagen}
            alt={`Course ${course.curso_titulo}`}
          />
        </header>
        <div className="card__main">
          <h3 className="card__title">{course.curso_titulo}</h3>
          <p className="card__paragraph">{course.curso_descripcion}</p>
          <h4 className="card__subtitle">{course.autor_id}</h4>

          <ul className="menu menu--features">
            <li className="menu__item">
              <span className="menu__item__feature">
                {course.curso_duracion} total hours
              </span>
            </li>
            <li className="menu__item">
              <span className="menu__item__feature menu__item__feature--dot">
                ·
              </span>
            </li>
            <li className="menu__item">
              <span className="menu__item__feature">
                {course.curso_clases} clases
              </span>
            </li>
          </ul>
        </div>
        <footer className="card__footer">
          <h6 className="card__level">
            <GiSettingsKnobs size={15} color="#718096" /> {course.nivel_id} level
          </h6>
          <Stars className="card" stars={stars} aria-label="Stars" />
          <h3 className="card__price">
            {course.curso_precio === 0 ? "Gratis" : `$${course.curso_precio}`}
          </h3>
        </footer>
      </Link>
    </article>
  );
};

export default CourseCard;
