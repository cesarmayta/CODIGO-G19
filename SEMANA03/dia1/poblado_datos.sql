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