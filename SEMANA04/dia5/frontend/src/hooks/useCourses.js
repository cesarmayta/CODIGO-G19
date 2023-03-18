import { useState } from "react";

export default function useCourses(
  url = `http://localhost:5000/curso`
) {
  const [loading, setLoading] = useState(true);
  const [courses, setCourses] = useState([]);
  const getCourses = async () => {
    setLoading(true);
    const headers = { 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3OTExMTY0OSwianRpIjoiMDU2OWIxMDQtOTA4MS00ZjAwLTk5ZTgtMzllYTBmNTFlNjgyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6NiwiZW1haWwiOiJjbWF5dGFjb2RpZ29nMTVAZ21haWwuY29tIn0sIm5iZiI6MTY3OTExMTY0OSwiZXhwIjoxNjc5MTEyNTQ5fQ.W7wbPC0n0zFFR1sUlD3U-wP8GQTdhGxhz_GENGv8QX0' };
    const response = await fetch(url,{headers});
    const data = await response.json();
    setCourses(data);
    console.log(data);
    setLoading(false);
  };
  return {
    courses,
    loading,
    getCourses,
  };
}
