--PROCEDIMIENTOS ALMACENADOS(SP)
DELIMITER $

CREATE PROCEDURE listar_alumnos()
BEGIN
    select * from tbl_alumno;
END
$

DELIMITER ;

CALL listar_alumnos();

--BUCLES CON PROCEDIMIENTOS ALMACENADOS
DELIMITER $

CREATE PROCEDURE ejemplo_bucle(IN tope INT,OUT suma INT UNSIGNED)
BEGIN
    DECLARE contador INT;
    SET contador = 1;
    SET suma = 0;

    bucle: LOOP 
        IF contador > tope THEN
            LEAVE bucle;
        END IF;

        SET suma = suma  + contador;
        SET contador = contador + 1;
    END LOOP;
END
$
DELIMITER ;

CALL ejemplo_bucle(10,@resultado);

select @resultado;