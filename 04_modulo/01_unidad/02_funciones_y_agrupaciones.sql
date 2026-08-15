-- Alias y Funciones
SELECT 
    cliente_id,
    UPPER(nombre) AS empresa,
    LOWER(nombre) AS empresa_min,
    LENGTH(nombre) AS longitud_nombre,
    COALESCE(email, 'SIN CORREO REGISTRADO') AS contacto
FROM clientes;

SELECT
    nombre_producto,
    precio,
    (precio * 1.19) AS precio_con_iva
FROM productos;

SELECT
    COUNT(*) AS total_productos_registrados,
    MIN(precio) AS producto_mas_barato,
    MAX(precio) AS producto_mas_caro,
    AVG(precio) AS promedio_precios
FROM productos;

-- Agrupación Simple (GROUP BY)
SELECT
    categoria_id,
    COUNT(*) AS cantidad_por_categoria
FROM productos
GROUP BY categoria_id;

-- Agrupación matemática
SELECT
    empleado_id,
    SUM(cantidad) AS unidades_totales_vendidas,
    SUM(cantidad * 100) AS estimacion_ganancia
FROM ventas
GROUP BY empleado_id;

-- Filtros (HAVING) -> Filtra datos agrupados
SELECT
    empleado_id,
    SUM(cantidad) AS unidades_totales_vendidas
FROM ventas
GROUP BY empleado_id
HAVING SUM(cantidad) > 25;

