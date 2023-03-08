-- PROCEDIMIENTO PARA MATRICULA DE ALUMNOS
DELIMITER $

DROP PROCEDURE IF EXISTS sp_matricula_alumno
$
CREATE PROCEDURE sp_matricular_alumno(IN alumnoId INT,IN bootcampId INT,IN grupo VARCHAR(255))
BEGIN
     DECLARE matriculaId INT;
     DECLARE cursoId INT;
     DECLARE totalCursos INT;
     set matriculaId = 0;
     set cursoId = 1;
     set totalCursos = 0;

     --registramos la matricula
     insert into tbl_matricula(alumno_id,bootcamp_id,matricula_grupo)
     values (alumnoId,bootcampId,grupo);

     
     select max(matricula_id) into matriculaId from tbl_matricula;

     select count(*) into totalCursos from tbl_curso;

     --registramos los cursos a matricular por alumno
    WHILE cursoId <= totalCursos DO
        insert into tbl_matricula_curso(matricula_id,curso_id)
        values (matriculaId,cursoId);

        SET cursoId = cursoId + 1;
    END WHILE;

END 
$

DELIMITER ;

CALL sp_matricular_alumno(1,2,'GODIGO 2023-1');

select * from tbl_matricula;
select * from tbl_matricula_curso;