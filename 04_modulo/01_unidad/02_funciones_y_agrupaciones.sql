-- Alias y Funciones
SELECT 
    cliente_id,
    UPPER(nombre) AS empresa,
    LENGTH(nombre) AS longitud_nombre,
    COALESCE(email, 'SIN CORREO REGISTRADO') AS contacto
FROM clientes;