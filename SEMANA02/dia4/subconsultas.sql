--SUBCONSULTAS
SELECT nombre,nota 
FROM alumno
WHERE nota > (select avg(nota) from alumno);
select count(*) from alumno 
where pais = 'Peru'
and nota >= (select max(nota) from alumno where pais = 'Peru');
select pais,count(*) from alumno
where nota > (select avg(nota) from alumno)
GROUP BY pais
order by count(*) desc;
--crear consulta que retorne el total de alumnos que salieron desaprobados por pais 
select pais,count(*)
from alumno
where nota <= 10
GROUP BY pais
order by count(*) desc;