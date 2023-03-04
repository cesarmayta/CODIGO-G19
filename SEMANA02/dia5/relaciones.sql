-- Active: 1677888840983@@127.0.0.1@3306@cursos
--RELACIONES
--RELACIÓN DE UNO A MUCHOS
CREATE TABLE IF NOT EXISTS alumno(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(200),
    nota DOUBLE DEFAULT 0
 );

DROP TABLE asistencia;

 CREATE TABLE IF NOT EXISTS asistencia(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    alumno_id INT NOT NULL,
    fecha_asistencia DATE NOT NULL,
    asistio TINYINT DEFAULT 1,
    FOREIGN KEY(alumno_id) REFERENCES alumno(id)
 );

 INSERT INTO asistencia(alumno_id,fecha_asistencia,asistio)
 VALUES
 (2,CURDATE(),1),
 (3,CURDATE(),0),
 (4,CURDATE(),1),
 (5,CURDATE(),1),
 (6,CURDATE(),0),
 (7,CURDATE(),1),
 (8,CURDATE(),0),
 (9,CURDATE(),1),
 (10,CURDATE(),1);
 
 
--INTEGRIDAD REFERENCIAL
 INSERT INTO asistencia(alumno_id,fecha_asistencia,asistio)
 VALUES (0,CURDATE(),1);

 DELETE FROM alumno where id = 10;

 --RELACIONES DE UNO A UNO
INSERT INTO asistencia(alumno_id,fecha_asistencia,asistio)
 VALUES
 (1,'2023-02-28',1),
 (1,'2023-03-02',0);

select * from asistencia where alumno_id = 1 order by fecha_asistencia ASC;

CREATE TABLE usuario(
    ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    usuario_nombre VARCHAR(20) NOT NULL UNIQUE,
    usuario_password VARCHAR(20) NOT NULL 
);

ALTER TABLE alumno
ADD COLUMN usuario_id INT UNIQUE;

insert into usuario(usuario_nombre,usuario_password)
VALUES ('admin','admin');

 ALTER TABLE alumno
 ADD CONSTRAINT fk_alumno_usuario FOREIGN KEY(usuario_id) REFERENCES usuario(id);
--LE AGREGAMOS UNIQUE PARA QUE EL USUARIO NO SE REPITA EN LA TABLA ALUMNO
ALTER TABLE alumno
MODIFY COLUMN usuario_id INT UNIQUE;

select * from alumno;
-- RELACIÓN DE MUCHOS A MUCHOS
-- ESTA RELACIÓN SE DEBE EVITAR CREANDO UNA TABLA INTERMEDIA
CREATE TABLE curso(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL
);
CREATE TABLE alumno_curso(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    curso_id INT NOT NULL,
    alumno_id INT NOT NULL,
    nota DOUBLE DEFAULT 0,
    FOREIGN KEY(curso_id) REFERENCES curso(id),
    FOREIGN KEY(alumno_id) REFERENCES alumno(id)
);
INSERT INTO curso(nombre) 
VALUES ('HTML Y CSS'),('JAVASCRIPT'),('REACT'),('PYTHON'),('FLASK'),('MYSQL');
select * from curso;
INSERT INTO alumno_curso(curso_id,alumno_id,nota)
VALUES 
(1,1,11),(1,2,10),(1,3,20),(1,4,15),(1,5,11),(1,6,19),(1,7,12),(1,8,6),(1,9,0),(1,10,20)
,(2,1,11),(2,2,10),(2,3,20),(2,4,15),(2,5,11),(2,6,19),(2,7,12),(2,8,6),(2,9,0),(2,10,20)
,(3,1,11),(3,2,10),(3,3,20),(3,4,15),(3,5,11),(3,6,19),(3,7,12),(3,8,6),(3,9,0),(3,10,20)

