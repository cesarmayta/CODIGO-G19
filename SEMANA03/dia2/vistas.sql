---vistas
CREATE VIEW vw_registro_alumnos as 
select a.alumno_nombre as nombre,a.alumno_email as email,a.alumno_celular as celular,
b.bootcamp_nombre,
CASE
    WHEN count(c1.curso_nombre) >= 1 THEN "HTML Y CSS"
    ELSE ""
END as Curso1,
CASE
    WHEN count(c2.curso_nombre) >= 1 THEN "JAVASCRIPT"
    ELSE ""
END as Curso2
from tbl_alumno a
INNER JOIN tbl_matricula m ON m.alumno_id = a.alumno_id
INNER JOIN tbl_bootcamp b ON m.bootcamp_id = b.bootcamp_id
INNER JOIN tbl_matricula_curso mc on mc.matricula_id = m.matricula_id
LEFT JOIN tbl_curso c1 ON mc.curso_id = c1.curso_id and c1.curso_id = 1
LEFT JOIN tbl_curso c2 ON mc.curso_id = c2.curso_id and c2.curso_id = 2
GROUP BY a.alumno_nombre,a.alumno_email,a.alumno_celular,b.bootcamp_nombre;


select nombre,bootcamp_nombre from vw_registro_alumnos;