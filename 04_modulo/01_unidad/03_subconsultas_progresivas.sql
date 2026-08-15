-- Consulta aislada
SELECT AVG(sueldo) FROM empleados;

-- Filtrado WHERE -> con datos no agrupados
SELECT nombre, apellido, sueldo
FROM empleados
WHERE sueldo > (
    SELECT AVG(sueldo) FROM empleados
); -- Subconsulta


-- Distinct te retorna una lista
SELECT DISTINCT cliente_id FROM ventas;

SELECT nombre, email
FROM clientes
WHERE cliente_id IN (
    SELECT DISTINCT cliente_id FROM ventas
)