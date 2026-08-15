-- INNER JOIN: Intersección
SELECT
    clientes.nombre AS nombre_cliente,
    ventas.fecha_venta,
    ventas.cantidad
FROM clientes
INNER JOIN ventas ON clientes.cliente_id = ventas.cliente_id;


SELECT
    clientes.nombre AS nombre_cliente,
    productos.nombre_producto,
    ventas.cantidad
FROM ventas
INNER JOIN clientes ON ventas.cliente_id = clientes.cliente_id
INNER JOIN productos ON ventas.producto_id = productos.id


-- LEFT JOIN -> Mantener la tabla principal intacta
SELECT
    clientes.nombre,
    ventas.venta_id
FROM clientes
LEFT JOIN ventas ON clientes.cliente_id = ventas.cliente_id

SELECT
    clientes.nombre
FROM clientes
LEFT JOIN ventas ON clientes.cliente_id = ventas.cliente_id
WHERE ventas.venta_id IS NULL;