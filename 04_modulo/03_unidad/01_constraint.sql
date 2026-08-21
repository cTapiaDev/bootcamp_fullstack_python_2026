CREATE TABLE clientes (
    cliente_id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    rut VARCHAR(12) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE
);

SELECT * FROM clientes;

CREATE TABLE matriculas (
    matricula_id SERIAL PRIMARY KEY,
    monto NUMERIC(10, 2) NOT NULL,
    estado BOOLEAN NOT NULL DEFAULT TRUE,

    CONSTRAINT chk_monto_positivo CHECK (monto >= 0.00)
);

ALTER TABLE matriculas
ADD COLUMN cliente_id INT,
ADD CONSTRAINT fk_cliente_matricula
    FOREIGN KEY (cliente_id)
    REFERENCES clientes(cliente_id)
    ON DELETE CASCADE; -- Si eliminamos un cliente, su matricula se borra


INSERT INTO clientes (nombre, apellido, rut, email)
VALUES ('Juan', 'Pérez', '12.345.678-9', 'juanperez@gmail.com');

INSERT INTO matriculas (monto, estado, cliente_id)
VALUES (-500.00, TRUE, 1); -- FALLA porque no cumple con el constraint de check

INSERT INTO matriculas (monto, estado, cliente_id)
VALUES (35000.00, TRUE, 1);

SELECT c.nombre, c.rut, m.monto, m.estado
FROM clientes AS c
INNER JOIN matriculas AS m
ON c.cliente_id = m.cliente_id;