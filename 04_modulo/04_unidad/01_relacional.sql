CREATE TABLE cliente (
    cliente_id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    direccion VARCHAR(250) NOT NULL,
    dni VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE producto (
    producto_id SERIAL PRIMARY KEY,
    codigo VARCHAR(20) UNIQUE NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    precio NUMERIC(10, 2) NOT NULL
);

CREATE TABLE compra (
    compra_id SERIAL PRIMARY KEY,
    cliente_id INT NOT NULL REFERENCES cliente(cliente_id),
    producto_id INT NOT NULL REFERENCES producto(producto_id),
    fecha DATE DEFAULT CURRENT_DATE
);

INSERT INTO cliente (nombre, apellido, direccion, dni)
VALUES ('Ana', 'Rojas', 'Calle #1', '11111111-1'), ('Luis', 'Rojas', 'Calle #1', '22211111-1');

INSERT INTO producto (codigo, nombre, precio)
VALUES ('P-002', 'Teclado', 45000), ('P-001', 'Monitor', 150000);

INSERT INTO compra (cliente_id, producto_id)
VALUES (1, 1), (1, 2), (2, 1);

-- Vistas
CREATE VIEW reporte_compras AS
SELECT
    co.compra_id,
    c.nombre AS cliente,
    p.nombre AS producto,
    p.precio,
    co.fecha
FROM compra co
INNER JOIN cliente c ON co.cliente_id = c.cliente_id
INNER JOIN producto p ON co.producto_id = p.producto_id;

SELECT * FROM reporte_compras;


-- Función & Triggers
CREATE TABLE auditoria_producto (
    id_auditoria SERIAL PRIMARY KEY,
    producto_id INT,
    precio_antiguo NUMERIC (10, 2),
    precio_nuevo NUMERIC (10, 2),
    fecha_modificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE OR REPLACE FUNCTION registrar_cambio_precio()
RETURNS TRIGGER AS $$
BEGIN
    IF OLD.precio <> NEW.precio THEN
        INSERT INTO auditoria_producto (producto_id, precio_antiguo, precio_nuevo)
        VALUES (OLD.producto_id, OLD.precio, NEW.precio);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_auditoria_precio
AFTER UPDATE ON producto
FOR EACH ROW
EXECUTE FUNCTION registrar_cambio_precio();

UPDATE producto SET precio = 180000 WHERE producto_id = 1;

SELECT * FROM producto;
SELECT * FROM auditoria_producto;