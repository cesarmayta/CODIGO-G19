-- JOINS 
-- INNER JOIN
select alumno.*,asistencia.*
from alumno INNER JOIN asistencia ON alumno.id = asistencia.alumno_id;
select alumno.nombre,asistencia.fecha_asistencia,asistencia.asistio
from alumno INNER JOIN asistencia ON alumno.id = asistencia.alumno_id;
--LEFT JOIN
select curso.nombre,alumno_curso.nota
from curso LEFT JOIN alumno_curso ON curso.id = alumno_curso.curso_id;
select c.nombre as curso,avg(ac.nota) as nota_promedio
from curso c LEFT JOIN alumno_curso ac ON ac.curso_id = c.id
GROUP BY c.nombre
ORDER BY avg(ac.nota) DESC;
--RIGHT JOIN
select c.nombre,count(ac.alumno_id) as cantidad
FROM alumno_curso ac RIGHT JOIN curso c on ac.curso_id = c.id
GROUP BY c.nombre;
select a.nombre as alumno,c.nombre as curso,ac.nota as nota 
FROM alumno_curso ac 
INNER JOIN alumno a ON ac.alumno_id = a.id
INNER JOIN curso c ON ac.curso_id = c.id;
--CREAR CONSULTA PARA RETORNAR EL NOMBRE DEL ALUMNO 
--Y EL PROMEDIO DE NOTA DE TODOS LOS CURSOS;
select a.nombre as alumno,avg(ac.nota) as promedio
FROM alumno a INNER JOIN alumno_curso ac ON a.id = ac.alumno_id
GROUP BY a.nombre;
--CREAR CONSULTA PARA RETORNAR UN LISTADO DE ALUMNOS CON SUS DIFERENTES NOTAS X CURSO
--INCLUYENDO EL PROMEDIO FINAL DE TODAS LAS NETWORK_NAMESPACE
-- DEBE TENER LA SIGUIENTES COLUMNAS
-- ALUMNO | HTML Y CSS | JAVASCRIPT | REACT | PYTHON | MYSQL | PROMEDIO
select a.nombre as alumno,
(select ac.nota from alumno_curso ac where ac.curso_id = 1 and ac.alumno_id = a.id) as 'HTML Y CSS'
from alumno a limit 10;
--
select a.nombre as alumno,
COALESCE(n1.nota,0) as 'HTML Y CSS',
COALESCE(n2.nota,0) as 'JAVASCRIPT',
COALESCE(n3.nota,0) as 'REACT',
COALESCE(n4.nota,0) as 'PYTHON',
COALESCE(n5.nota,0) as 'FLASK',
COALESCE(n6.nota,0) as 'MYSQL',
AVG(COALESCE(n.nota,0)) as PROMEDIO
from alumno a
INNER JOIN alumno_curso n ON n.alumno_id = a.id
LEFT JOIN alumno_curso n1 ON n1.alumno_id = a.id and n1.curso_id = 1
LEFT JOIN alumno_curso n2 ON n2.alumno_id = a.id and n2.curso_id = 2
LEFT JOIN alumno_curso n3 ON n3.alumno_id = a.id and n3.curso_id = 3
LEFT JOIN alumno_curso n4 ON n4.alumno_id = a.id and n4.curso_id = 4
LEFT JOIN alumno_curso n5 ON n5.alumno_id = a.id and n5.curso_id = 5
LEFT JOIN alumno_curso n6 ON n6.alumno_id = a.id and n6.curso_id = 6
GROUP BY a.nombre,n1.nota,n2.nota,n3.nota,n4.nota,n5.nota,n6.nota;