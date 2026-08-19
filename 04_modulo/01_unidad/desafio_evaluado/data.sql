CREATE TABLE clientes (
    email VARCHAR(50),
    nombre VARCHAR,
    telefono VARCHAR(16),
    empresa VARCHAR(50),
    prioridad SMALLINT
);

INSERT INTO clientes (email, nombre, telefono, empresa, prioridad) VALUES
('usuario1@gmail.com', 'Juan', 911111111, 'Copec', 10),
('usuario2@gmail.com', 'Miguel', 922222222, 'Shell', 3),
('usuario3@gmail.com', 'Leonardo', 933333333, 'Petro', 5),
('usuario4@gmail.com', 'Felipe', 944444444, 'Shell', 8),
('usuario5@gmail.com', 'Jose',  955555555, 'Power', 1);

SELECT *
FROM clientes
ORDER BY prioridad DESC
LIMIT 3;

SELECT *
FROM clientes
WHERE empresa = 'Shell';

-- Comando para salir desde la consola
\q