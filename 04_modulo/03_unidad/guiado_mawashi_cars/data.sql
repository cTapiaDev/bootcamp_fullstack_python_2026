CREATE TABLE autos (
    id INT PRIMARY KEY,
    marca VARCHAR(25),
    modelo VARCHAR(25),
    anio VARCHAR(25),
    color VARCHAR(25),
    precio FLOAT
);

CREATE TABLE ventas (
    id SERIAL UNIQUE NOT NULL,
    fecha VARCHAR(20),
    id_auto INT,
    cliente VARCHAR(25),
    referencia INT,
    cantidad FLOAT,
    metodo_pago VARCHAR(10),
    FOREIGN KEY (id_auto) REFERENCES autos(id)
);


INSERT INTO autos (id, marca, modelo, anio, color, precio) VALUES 
(1, 'Toyota', 'Corolla Araya', '1991', 'Blanco', 1200000),
(2, 'Mazda', 'Mazda 3', '2000', 'Azul',2000000),
(3, 'Chevrolet', 'Spark', '1998', 'Verde Oscuro', 1200000),
(4, 'Nissan', 'Versa', 2018, 'Gris Plata', 5000000),
(5, 'Hyundai', 'Accent', 2022, 'Rojo', 10500000),
(6, 'Kia', 'Rio', 2020, 'Negro', 8000000),
(7, 'Volkswagen', 'Gol', 2015, 'Azul Marino', 3500000),
(8, 'Fiat', 'Mobi', 2017, 'Blanco', 2800000),
(9, 'Suzuki', 'Swift', 2019, 'Gris Oxford', 6200000),
(10, 'Peugeot', '208', 2021, 'Rojo', 9800000);

INSERT INTO ventas (fecha, id_auto, cliente, referencia, cantidad, metodo_pago) VALUES
('2020-10-15', 1, 'Chuck', 43224, 12000000, 'Débito'),
('2020-11-15', 1, 'Donnie', 43334, 12000000, 'Transfer'),
('2020-12-15', 3, 'Jet', 43444, 12000000, 'Cheque'),
('2021-01-05', 1, 'Peter', 43335, 12000000, 'Débito'),
('2021-01-15', 1, 'Abigail', 43554, 12000000, 'Transfer'),
('2021-02-01', 3, 'Jhon', 43456, 12000000, 'Cheque'),
('2021-02-01', 2, 'Walter', 54321, 2000000, 'Efectivo'),
('2021-03-15', 3, 'Sarah', 54322, 1200000, 'Tarjeta'),
('2021-04-05', 4, 'Jessica', 54323, 5000000, 'Débito'),
('2021-05-25', 5, 'Luis', 54324, 10500000, 'Transfer');

SELECT cliente, marca, modelo 
FROM ventas 
INNER JOIN autos ON ventas.id_auto = autos.id;

-- Realizar la consulta necesaria para obtener todos los autos cuyos id no se encuentran en la tabla Ventas.

SELECT autos.*
FROM autos
LEFT JOIN ventas ON autos.id = ventas.id_auto
WHERE ventas.id IS NULL;


SELECT *
FROM autos
FULL OUTER JOIN ventas ON ventas.id_auto = autos.id
WHERE autos.id IS NULL OR ventas.id_auto IS NULL;