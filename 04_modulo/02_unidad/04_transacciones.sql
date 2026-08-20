CREATE TABLE cuentas (
    numero_cuenta INT NOT NULL UNIQUE PRIMARY KEY,
    balance FLOAT CHECK(balance >= 0.00)
);

INSERT INTO cuentas (numero_cuenta, balance) VALUES
(1, 1000),
(2, 1000),
(3, 1000);

SELECT * FROM cuentas;

-- Transacción simple
BEGIN; --Inicio

UPDATE cuentas SET balance = balance - 1000 WHERE numero_cuenta = 1;
UPDATE cuentas SET balance = balance + 1000 WHERE numero_cuenta = 2;

COMMIT; --Cierre

SELECT * FROM cuentas ORDER BY numero_cuenta;


-- Transacción con Rollback
BEGIN;

UPDATE cuentas SET balance = balance + 2000 WHERE numero_cuenta = 3;
-- UPDATE cuentas SET balance = balance - 2000 WHERE numero_cuenta = 2;

ROLLBACK;


SELECT * FROM cuentas ORDER BY numero_cuenta;



-- Transacción con SAVEPOINT
BEGIN;

UPDATE cuentas SET balance = balance + 50;

SAVEPOINT comision_agregada;

UPDATE cuentas SET balance = balance + 5000 WHERE numero_cuenta = 1;

ROLLBACK TO SAVEPOINT comision_agregada;

COMMIT;


-- Transacción con SET
BEGIN;

SET TRANSACTION READ ONLY;

SELECT SUM(balance) AS liquidez_total
FROM cuentas;

UPDATE cuentas SET balance = balance + 100 WHERE numero_cuenta = 1;

COMMIT;