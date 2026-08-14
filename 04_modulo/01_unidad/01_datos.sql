-- CREATE
CREATE TABLE departamentos (
    id SERIAL PRIMARY KEY,
    nombre_depto VARCHAR(50) NOT NULL
);

CREATE TABLE categorias (
    id SERIAL PRIMARY KEY,
    nombre_categoria VARCHAR(50) NOT NULL
);

CREATE TABLE empleados (
    empleado_id INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    sueldo NUMERIC,
    departamento_id INT,
    fecha_contratacion DATE
);

CREATE TABLE clientes (
    cliente_id INT PRIMARY KEY,
    nombre VARCHAR(50),
    email VARCHAR(100),
    activo BOOLEAN
);

CREATE TABLE productos (
    id INT PRIMARY KEY,
    nombre_producto VARCHAR(100),
    precio NUMERIC,
    categoria_id INT,
    stock INT
);

CREATE TABLE ventas (
    venta_id SERIAL PRIMARY KEY,
    cliente_id INT,
    empleado_id INT,
    producto_id INT,
    cantidad INT,
    fecha_venta DATE
);

-- INSERT
INSERT INTO departamentos (nombre_depto) VALUES
('Ventas'), ('Marketing'), ('Tecnología'), ('Recursos Humanos'), ('Finanzas'), ('Logística');

INSERT INTO categorias (nombre_categoria) VALUES
('Electrónica'), ('Muebles'), ('Software'), ('Oficina');

INSERT INTO empleados VALUES
(1, 'Juan', 'Pérez', 3000, 1, '2022-01-15'),
(2, 'María', 'González', 3500, 2, '2021-11-20'),
(3, 'Carlos', 'Rodríguez', 4200, 3, '2020-05-10'),
(4, 'Ana', 'Martínez', 2800, 4, '2023-03-01'),
(5, 'Luis', 'García', 3200, 5, '2019-08-25'),
(6, 'Elena', 'Rojas', 3100, 1, '2022-06-12'),
(7, 'Pedro', 'Sánchez', 3900, 3, '2021-02-18'),
(8, 'Laura', 'Gómez', 2950, 4, '2023-01-10');

INSERT INTO clientes VALUES
(1, 'Empresa A', 'contacto@empresaa.com', TRUE),
(2, 'Empresa B', 'ventas@empresab.com', TRUE),
(3, 'Empresa C', NULL, FALSE),
(4, 'Empresa D', 'info@empresad.com', TRUE),
(5, 'Empresa E', NULL, FALSE);

INSERT INTO productos VALUES
(101, 'Laptop', 1200, 1, 15),
(102, 'Monitor 27"', 300, 1, 45),
(103, 'Teclado Mecánico', 100, 1, 100),
(201, 'Silla Ergonómica', 250, 2, 25),
(202, 'Escritorio', 450, 2, 10),
(301, 'Licencia Antivirus', 50, 3, 500),
(401, 'Resma Papel', 5, 4, 1000);

INSERT INTO ventas (cliente_id, empleado_id, producto_id, cantidad, fecha_venta) VALUES
(1, 1, 101, 2, '2024-01-05'),
(1, 1, 102, 4, '2024-01-05'),
(2, 6, 201, 10, '2024-01-12'),
(3, 2, 301, 50, '2024-02-01'),
(4, 1, 401, 100, '2024-02-15'),
(1, 6, 103, 5, '2024-02-20'),
(5, 5, 202, 2, '2024-03-05'),
(2, 1, 101, 1, '2024-03-10'),
(1, 6, 201, 5, '2024-03-12');

-- SELECT
SELECT id, nombre_depto FROM departamentos;
SELECT cliente_id, nombre, email, activo FROM clientes;