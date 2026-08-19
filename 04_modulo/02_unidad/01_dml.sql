CREATE TABLE cocina_chilena (
    id INT,
    nombre VARCHAR(50)
);

INSERT INTO cocina_chilena (id, nombre) VALUES
(1, 'Pastel de choclo'),
(2, 'Umitas'),
(3, 'Cazuela'),
(4, 'Empanada'),
(5, 'Charquicán');

ALTER TABLE cocina_chilena ADD COLUMN region_origen VARCHAR(50);
ALTER TABLE cocina_chilena ADD COLUMN precio INT;
ALTER TABLE cocina_chilena ADD COLUMN disponible BOOLEAN;

UPDATE cocina_chilena
SET disponible = TRUE, precio = 500;

UPDATE cocina_chilena
SET nombre = 'Humitas', precio = 3500, region_origen = 'Zona Central'
WHERE id = 2;

UPDATE cocina_chilena
SET precio = 6000
WHERE id IN (1, 3);

DELETE FROM cocina_chilena
WHERE id = 5;

SELECT * FROM cocina_chilena ORDER BY id;