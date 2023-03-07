--poblado de datos para db_codigo_g19
--cursos
insert into tbl_curso(curso_nombre)
values ('HTML Y CSS'),('JAVASCRIPT'),('REACT.JS'),('PYTHON'),('FLASK'),('MYSQL');
select * from tbl_curso;

--bootcamp
insert into tbl_bootcamp(bootcamp_nombre)
values ('Desarrollo Web Fullstack'),
('Desarrollo Web con Laravel'),
('Desarrollo Web con MERN'),
('Desarrollo Móvil con Flutter');
select * from tbl_bootcamp;
--alumno
drop table tbl_matricula_curso;
drop table tbl_matricula;
alter table tbl_alumno
MODIFY COLUMN alumno_id INT NOT NULL AUTO_INCREMENT;
insert into tbl_alumno(alumno_nombre,alumno_email,alumno_celular)
values ('César Mayta','cesarmayta@gmail.com','9999999'),
('Lorena Espinoza','lorenaespinoza@gmail.com','3333333');
select * from tbl_alumno;
--matricula
insert into tbl_matricula(matricula_grupo,alumno_id,bootcamp_id)
values ('CODIGO G19',1,1),('CODIGO G19',2,1);
select * from tbl_matricula;
--matricula_curso
insert into tbl_matricula_curso(matricula_id,curso_id)
values (1,1),(1,2),(1,3),(1,4),(1,5),(1,6),
(2,1),(2,2),(2,3),(2,4),(2,5),(2,6);

--probamos la consulta inicial
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
GROUP BY a.alumno_nombre,a.alumno_email,a.alumno_celular,b.bootcamp_nombre
