import CoursesList from "./CoursesList";

const CoursesContent = ({ category, filters }) => {
  const categoryTitle = category === "all" ? "All" : category;

  const isValid = (valueCourse, value, name, course) => {
    if (name === "stars") return +value <= valueCourse;
    if (name === "duration") return +value <= valueCourse;
    if (name === "course-type") {
      const valueCoursePrice = Reflect.get(course, "price");
      return value === "free"
        ? valueCoursePrice === "free"
        : valueCoursePrice !== "free";
    }
    return (
      (typeof valueCourse === "string"
        ? valueCourse
        : String(valueCourse)
      ).toLowerCase() === value?.toLowerCase()
    );
  };
  return (
    <section className="section section--courses">
      <div className="section-container section-container--courses">
        <h2 className="section__title">{categoryTitle} Courses</h2>
        <p className="section__paragraph section__paragraph--courses">
          cursos disponibles
        </p>
        <CoursesList filters={filters} category={category} isValid={isValid} />
      </div>
    </section>
  );
};

export default CoursesContent;
