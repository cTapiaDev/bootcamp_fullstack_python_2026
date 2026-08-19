CREATE TABLE empleados (
    id SERIAL PRIMARY KEY,
    rut VARCHAR(12) UNIQUE NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    edad INT CHECK (edad >= 18),
    sueldo NUMERIC DEFAULT 500000
);

INSERT INTO empleados (rut, nombre, apellido, email, edad)
VALUES ('11111111-1', 'Juan', 'Pérez', 'juan.perez@empresa.cl', 30);

-- Error por NOT NULL (apellido)
INSERT INTO empleados (rut, nombre, email, edad)
VALUES ('22222222-2', 'María', 'maria@empresa.cl', 35);

-- Error por dato duplicado, rut debe ser UNIQUE
INSERT INTO empleados (rut, nombre, apellido, edad)
VALUES ('11111111-1', 'Carlos', 'Gómez', 40);

-- Error por restricción de CHECK (Edad menor a 18)
INSERT INTO empleados (rut, nombre, apellido, edad)
VALUES ('33333333-3', 'Ana', 'Rojas', 17);

INSERT INTO empleados (rut, nombre, apellido, email, edad, sueldo)
VALUES ('44444444-4', 'Luis', 'Sánchez', 'luis@empresa.cl', 35, 850000);

SELECT * FROM empleados;