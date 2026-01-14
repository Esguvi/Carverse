CREATE DATABASE IF NOT EXISTS ciber;
USE ciber;
CREATE TABLE coches(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    precio DECIMAL(9,2) NOT NULL,
	foto VARCHAR(255),
    marca VARCHAR(255)
);
CREATE TABLE comentarios(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    descripcion VARCHAR(255) NOT NULL
);
CREATE TABLE usuarios(
	email VARCHAR(100) NOT NULL PRIMARY KEY,
    password VARCHAR(255) NOT NULL,
    name VARCHAR(100) NOT NULL
);
INSERT INTO `usuarios` (`email`, `password`, `name`) VALUES ('admin@carverse.com','1234', 'root');
