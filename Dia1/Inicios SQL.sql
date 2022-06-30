-- SQL > Structured Query Lenguage ( Lenguaje de consultas estructurado)
-- Registro > conjunto de datos 
-- Dato > un valor que por si solo no da una buena referencia
-- Las BD estan compuestas por una o varias tabalas y cada tabla puede contener uno
-- o varios registros 
-- en el lenguaje de bd siempre tenemos que colocar el ";" asi se da cuenta que la instruccion ha terminado
CREATE DATABASE prueba;

-- Sirve para indicar en que vd queremos trabajar 
USE prueba;

CREATE table productos(
	-- Obligatorio para crear una tabla debemos crear al menos una columna
    -- Solo se puede usar auto_incremet una vez por tabla 
    id int auto_increment primary key,
    nombre varchar(50),
    fecha_vencimiento date
);
