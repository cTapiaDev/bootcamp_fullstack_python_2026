CREATE TABLE clientes (
    rut INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    email VARCHAR(50)
);

CREATE TABLE matriculas (
    id SERIAL PRIMARY KEY,
    monto VARCHAR(50),
    estado BOOLEAN,
    cliente_rut INT REFERENCES clientes(rut)
);

INSERT INTO clientes VALUES 
(999999999, 'Cliente 1', 'Apellido cliente 1', 'cliente1@email.com'),
(888888888, 'Cliente 2', 'Apellido cliente 2', 'cliente2@email.com'),
(777777777, 'Cliente 3', 'Apellido cliente 3', 'cliente3@email.com'),
(666666666, 'Cliente 4', 'Apellido cliente 4', 'cliente4@email.com'),
(555555555, 'Cliente 5', 'Apellido cliente 5', 'cliente5@email.com');

INSERT INTO matriculas (monto, estado, cliente_rut) VALUES 
(40000, TRUE, '999999999'),
(40000, FALSE, '888888888'),
(55000, TRUE, '555555555'),
(35000, TRUE, '777777777'),
(35000, TRUE, '777777777'),
(60000, FALSE, '666666666');


-- SELECT
--     clientes.email,
--     clientes.rut,
--     matriculas.monto,
--     matriculas.estado
-- FROM clientes
-- INNER JOIN matriculas ON clientes.rut = matriculas.cliente_rut

-- INNER JOIN
SELECT
    c.email,
    c.rut,
    m.monto,
    m.estado
FROM clientes AS c
INNER JOIN matriculas AS m 
ON c.rut = m.cliente_rut


-- ORDER BY
SELECT
    c.email,
    c.rut,
    m.monto,
    m.estado
FROM clientes AS c
INNER JOIN matriculas AS m 
ON c.rut = m.cliente_rut
ORDER BY m.monto ASC


-- GROUP BY & HAVING
SELECT
    monto,
    COUNT(monto)
FROM matriculas
GROUP BY monto
HAVING COUNT(monto) >= 2


SELECT
    c.email,
    c.rut,
    m.monto,
    m.estado,
    COUNT(m.id)
FROM clientes AS c
INNER JOIN matriculas AS m
ON c.rut = m.cliente_rut
GROUP BY c.email, c.rut, m.monto, m.estado
HAVING COUNT(m.id) >= 2


-- Borra los campos insertados en una tabla
DELETE FROM matriculas;

-- Elimina completamente la tabla
DROP TABLE matriculas;

CREATE TABLE matriculas (
    id SERIAL PRIMARY KEY,
    monto INT,
    estado BOOLEAN,
    cliente_rut INT REFERENCES clientes(rut)
);


SELECT
    cliente_rut,
    SUM(monto) AS total_invertido
FROM matriculas
WHERE estado = TRUE
GROUP BY cliente_rut
HAVING SUM(monto) > 40000;

SELECT
    id,
    cliente_rut,
    monto
FROM matriculas
WHERE monto > (
    SELECT AVG(monto) FROM matriculas
);