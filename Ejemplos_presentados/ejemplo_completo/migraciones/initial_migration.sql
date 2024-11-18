-- initial_migration.sql

-- Crear la base de datos
-- CREATE DATABASE todo_app;

-- Conectar a la base de datos
\c test_masterclass;

-- Crear la tabla todos
CREATE TABLE todos (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar datos iniciales
INSERT INTO todos (title, description, completed) VALUES
('Tarea 1', 'Descripción de la tarea 1', false),
('Tarea 2', 'Descripción de la tarea 2', false),
('Tarea 3', 'Descripción de la tarea 3', false),
('Tarea 4', 'Descripción de la tarea 4', false),
('Tarea 5', 'Descripción de la tarea 5', false);