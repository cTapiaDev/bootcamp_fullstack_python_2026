CREATE TABLE IF NOT EXISTS INSCRITOS (
    cantidad INT, 
    fecha DATE, 
    fuente VARCHAR
);

INSERT INTO INSCRITOS(cantidad, fecha, fuente) VALUES
( 44, '01/01/2021', 'Blog' ),
( 56, '01/01/2021', 'Página' ),
( 39, '01/02/2021', 'Blog' ),
( 81, '01/02/2021', 'Página' ),
( 12, '01/03/2021', 'Blog' ),
( 91, '01/03/2021', 'Página' ),
( 48, '01/04/2021', 'Blog' ),
( 45, '01/04/2021', 'Página' ),
( 55, '01/05/2021', 'Blog' ),
( 33, '01/05/2021', 'Página' ),
( 18, '01/06/2021', 'Blog' ),
( 12, '01/06/2021', 'Página' ),
( 34, '01/07/2021', 'Blog' ),
( 24, '01/07/2021', 'Página' ),
( 83, '01/08/2021', 'Blog' ),
( 99, '01/08/2021', 'Página' );


-- ¿Cuántos registros hay?
SELECT COUNT(*) AS "Total Registros"
FROM INSCRITOS;

-- ¿Cuántos inscritos hay en total?
SELECT SUM(cantidad) AS "Total Inscritos"
FROM INSCRITOS;

-- ¿Cuál o cuáles son los registros de mayor antigüedad?
SELECT *
FROM INSCRITOS
WHERE fecha = (
    SELECT MIN(fecha)
    FROM INSCRITOS
);

-- ¿Cuántos inscritos hay por día? (entendiendo un día como una fecha distinta de ahora en adelante)
SELECT fecha, SUM(cantidad) AS "Inscritos por día"
FROM INSCRITOS
GROUP BY fecha
ORDER BY fecha ASC;

-- ¿Qué día se inscribieron la mayor cantidad de personas y cuántas personas se inscribieron en ese día?
SELECT fecha, SUM(cantidad) AS maxima_cantidad_inscritos
FROM INSCRITOS
GROUP BY fecha
ORDER BY maxima_cantidad_inscritos DESC
LIMIT 1;