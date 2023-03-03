--SENTENCIAS DE AGRUPACIÓN
select count(*) from alumno;
select count(*) from alumno where pais = 'Peru';
select sum(nota) / count(*) from alumno;
select avg(nota) as promedio,min(nota) as minimo,max(nota) as maximo from alumno;

--GROUP BY
select pais,count(*) as cantidad from alumno
GROUP BY pais
order by count(*) desc;
select pais,count(*) as cantidad from alumno
where pais in ('Peru','Chile')
GROUP BY pais
order by count(*) desc;
--crear consulta que retorne la nota promedio,minima y maxima por pais de alumnos aprobados
select pais,avg(nota) as promedio,min(nota) as minimo,max(nota) as maximo
FROM alumno
WHERE nota > 10
GROUP BY pais
HAVING avg(nota) <= 16
order by avg(nota) desc;