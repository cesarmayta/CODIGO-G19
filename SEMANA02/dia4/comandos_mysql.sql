#para ver version de mysql
mysql --version
#acceder a mysql
mysql  -h localhost -u root -p
#para crear una base de datos
create database cursos
#para ingresar a la base de datos creada
use cursos;
#para crear una tabal
CREATE TABLE alumno(
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(200)
);
#modificar tabla para agregar clave primaria al inicio
ALTER TABLE alumno ADD COLUMN id INT NOT NULL PRIMARY KEY AUTO_INCREMENT FIRST;

#para modificar una tabla agrega run campo
ALTER TABLE alumno
ADD COLUMN pais VARCHAR(100) DEFAULT 'Perú';

#para insertar registros
insert into alumno(nombre,email) values('cesar mayta','cesarmayta@gmail.com');
insert into alumno(nombre,pais) values('ada morales','Colombia');

#para insertar varios registros
insert into alumno(nombre,email) values
('Jose Luna','pepe@hotmail.com'),
('Laura Lopez','laurital89@gmail.com');

#para ver los registros insertados
select * from alumno
