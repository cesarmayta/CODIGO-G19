-- Active: 1677809697746@@127.0.0.1@3306@cursos
--SENTENCIAS SELECT
select distinct pais from alumno;
select nombre,email from alumno 
where pais = 'Chile';
select nombre,email,nota from alumno 
where pais = 'Peru' and nota > 10;
select nombre,email,nota from alumno 
where pais = 'Colombia' and nota BETWEEN 14 AND 18;
select nombre,email,pais from alumno
where pais = 'Chile' or pais = 'Venezuela';
select nombre,email,pais from alumno
where pais IN ('Chile','Peru','Ecuador');
select nombre,email from alumno
where pais NOT IN ('Peru');
select nombre,email,pais,nota from alumno
where nombre like 'A%';
select nombre,email,pais from alumno
where email like '%@outlook.com';
select distinct SUBSTR(email,POSITION('@' in email) + 1,LENGTH(email) - POSITION('@' in email)) from alumno limit 10;