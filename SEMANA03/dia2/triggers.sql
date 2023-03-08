--TRIGGER
ALTER TABLE tbl_alumno
ADD alumno_codigo VARCHAR(20);


DELIMITER $

DROP TRIGGER tg_alumno_codigo
$

CREATE TRIGGER tg_alumno_codigo
BEFORE INSERT
ON tbl_alumno FOR EACH ROW
BEGIN
    DECLARE aluId INT;
    select max(alumno_id) into aluId from tbl_alumno;

    set NEW.alumno_codigo = CONCAT(YEAR(CURRENT_DATE()),LPAD(aluId + 1,5,'0'));
END

DELIMITER ;

select * from tbl_alumno;

insert into tbl_alumno(alumno_nombre,alumno_email,alumno_celular)
values ('Carlos Soto','csoto@hotmail.com','2222332');

