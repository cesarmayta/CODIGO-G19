import { AnimatePresence, motion } from "framer-motion";
import { useEffect, useState } from "react";
import Spinner from "../shared/Spinner";
import SvgEmpty from "../Svgr/SvgEmpty";
import CourseCard from "./CourseCard";

const CoursesList = ({ category, filters, isValid }) => {
  const [loading, setLoading] = useState(true);
  const [courses, setCourses] = useState([]);
  const [coursesFiltered, setCoursesFiltered] = useState([]);
  const getCourses = async () => {
    const response = await fetch(
      'http://localhost:5000/curso'
      //`https://apimocha.com/education-platform/courses/${category}`
    );
    const data = await response.json();
    console.log(data.content);
    setCourses(data.content);
    setLoading(false);
  };
  const loadFilters = () => {
    setCoursesFiltered(
      courses.filter((course) => {
        return Object.entries(filters).every(([filter, value]) => {
          const valueCourse = Reflect.get(course, filter);
          return isValid
            ? isValid(valueCourse, value, filter, course)
            : (typeof valueCourse === "string"
                ? valueCourse
                : String(valueCourse)
              ).toLowerCase() === value?.toLowerCase();
        });
      })
    );
  };
  useEffect(() => {
    setLoading(true);
    getCourses();
  }, []);
  /*useEffect(() => {
    loadFilters();
  }, [, courses]);*/

  return (
    <AnimatePresence>
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          className="cards"
        >
          {courses.map((course) => (
            <CourseCard key={course.curso_id} course={course} />
          ))}
        </motion.div>
    </AnimatePresence>
  );
};

export default CoursesList;
