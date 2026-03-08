-- Crear base de datos
CREATE DATABASE inventario_db;

-- Usar la base
USE inventario_db;

-- Crear tabla
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    cantidad INT NOT NULL DEFAULT 0,
    precio DECIMAL(10,2) NOT NULL
);