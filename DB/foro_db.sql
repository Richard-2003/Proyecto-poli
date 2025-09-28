--copiar en mysql y ejecutar
-- Script para crear la base de datos y las tablas necesarias
-- Nombre de la base de datos: foro_db

CREATE DATABASE foro_db;

USE foro_db; -- cada que se vaya hacer algo en la base de datos hay que poner USE foro_db

CREATE TABLE usuarios (
  id int PRIMARY KEY AUTO_INCREMENT,
  nombre varchar(255),
  email varchar(255),
  password varchar(255),
  rol_id int
);

CREATE TABLE roles (
  id int PRIMARY KEY AUTO_INCREMENT,
  nombre varchar(255),
  Permisos varchar(255)
);

CREATE TABLE post (
  id int PRIMARY KEY AUTO_INCREMENT,
  titulo varchar(255),
  contenido text,
  imagen text,
  usuario_id int
);

CREATE TABLE Comentarios (
  id int PRIMARY KEY AUTO_INCREMENT,
  contenido text,
  post_id int,
  usuario_id int
);

CREATE TABLE Respuestas (
  id int PRIMARY KEY AUTO_INCREMENT,
  contenido text,
  comentario_id int,
  usuario_id int
);

ALTER TABLE usuarios ADD FOREIGN KEY (rol_id) REFERENCES roles (id);
ALTER TABLE post ADD FOREIGN KEY (usuario_id) REFERENCES usuarios (id);
ALTER TABLE Comentarios ADD FOREIGN KEY (post_id) REFERENCES post (id);
ALTER TABLE Comentarios ADD FOREIGN KEY (usuario_id) REFERENCES usuarios (id);
ALTER TABLE Respuestas ADD FOREIGN KEY (comentario_id) REFERENCES Comentarios (id);
ALTER TABLE Respuestas ADD FOREIGN KEY (usuario_id) REFERENCES usuarios (id);
