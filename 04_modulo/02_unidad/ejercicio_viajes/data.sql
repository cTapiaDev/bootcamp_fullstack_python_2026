-- Crear la tabla Viajeros
CREATE TABLE Viajeros (
    viajero_id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    genero CHAR(5) NOT NULL,
    email VARCHAR(250),
    telefono CHAR(50) NOT NULL,
    rut CHAR(10) NOT NULL UNIQUE
);

-- Crear la tabla Destinos
CREATE TABLE Destinos (
    destino_id SERIAL PRIMARY KEY,
    nombre_destino VARCHAR(100) NOT NULL,
    ciudad VARCHAR(50),
    pais VARCHAR(50)
);
-- Crear la tabla Tickets
CREATE TABLE Tickets (
    ticket_id SERIAL PRIMARY KEY,
    destino_id INT REFERENCES DESTINOS (destino_id),
    viajero_id INT REFERENCES Viajeros(viajero_id),
    numero_boleto VARCHAR(50) NOT NULL UNIQUE,
    fecha_emision DATE,
    fecha_salida DATE,
    fecha_retorno DATE
);


-- Inserts para la tabla Viajeros
INSERT INTO Viajeros (nombre, genero, email, telefono, rut) VALUES
('Juan Perez', 'M', 'juan@email.com', '123456789', '1111111111'),
('Maria Rodriguez', 'F', 'maria@email.com', '987654321', '2222222222'),
('Carlos Gonzalez', 'M', 'carlos@email.com', '111222333', '3333333333'),
('Luisa Martinez', 'F', 'luisa@email.com', '444555666', '4444444444'),
('Pedro Hernandez', 'M', 'pedro@email.com', '777888999', '5555555555'),
('Ana Lopez', 'F', 'ana@email.com', '333444555', '6666666666'),
('Jorge Ramirez', 'M', 'jorge@email.com', '666777888', '7777777777'),
('Sofia Torres', 'F', 'sofia@email.com', '999000111', '8888888888'),
('Daniel Castro', 'M', 'daniel@email.com', '222333444', '9999999999'),
('Laura Garcia', 'F', 'laura@email.com', '555666777', '0000000000'),
('Manuel Silva', 'M', 'manuel@email.com', '888999000', '1231231231'),
('Elena Vargas', 'F', 'elena@email.com', '111222333', '4564564564'),
('Gabriel Morales', 'M', 'gabriel@email.com', '444555666', '7897897897'),
('Isabel Rios', 'F', 'isabel@email.com', '777888999', '0120120120'),
('Hector Mendoza', 'M', 'hector@email.com', '333444555', '9876543210');

-- Inserts para la tabla Destinos
INSERT INTO Destinos (nombre_destino, ciudad, pais) VALUES
('Playa del Carmen', 'Playa del Carmen', 'México'),
('Machu Picchu', 'Cuzco', 'Perú'),
('Torres del Paine', 'Puerto Natales', 'Chile'),
('Gran Barrera de Coral', 'Queensland', 'Australia'),
('Monte Everest', 'Khumbu', 'Nepal'),
('Santorini', 'Santorini', 'Grecia'),
('Marrakech', 'Marrakech', 'Marruecos'),
('Kioto', 'Kioto', 'Japón'),
('Marrakech', 'Marrakech', 'Marruecos'),
('Marrakech', 'Marrakech', 'Marruecos'),
('Marrakech', 'Marrakech', 'Marruecos'),
('Marrakech', 'Marrakech', 'Marruecos'),
('Marrakech', 'Marrakech', 'Marruecos'),
('Marrakech', 'Marrakech', 'Marruecos'),
('Marrakech', 'Marrakech', 'Marruecos');

-- Inserts para la tabla Tickets
INSERT INTO Tickets (viajero_id, destino_id, numero_boleto, fecha_emision, fecha_salida, fecha_retorno) VALUES
(1, 1, 'T111111', '2024-01-04', '2024-01-10', '2024-01-20'),
(2, 2, 'T222222', '2024-01-05', '2024-02-01', '2024-02-15'),
(2, 3, 'T333333', '2024-01-06', '2024-03-05', '2024-03-20'),
(4, 4, 'T444444', '2024-01-07', '2024-04-12', '2024-05-01'),
(5, 5, 'T555555', '2024-01-08', '2024-06-02', '2024-06-20'),
(6, 1, 'T666666', '2024-01-09', '2024-07-15', '2024-08-01'),
(4, 2, 'T777777', '2024-01-10', '2024-09-03', '2024-09-20'),
(8, 3, 'T888888', '2024-01-11', '2024-10-18', '2024-11-01'),
(9, 4, 'T999999', '2024-01-12', '2024-12-05', '2024-12-20'),
(10, 5, 'T101010', '2024-01-13', '2025-01-02', '2025-01-20'),
(15, 1, 'T1111111', '2024-01-14', '2025-02-10', '2025-02-25'),
(12, 2, 'T121212', '2024-01-15', '2025-03-15', '2025-04-01'),
(13, 3, 'T131313', '2024-01-16', '2025-05-02', '2025-05-20'),
(14, 4, 'T141414', '2024-01-17', '2025-06-12', '2025-06-30'),
(15, 5, 'T151515', '2024-01-18', '2025-07-20', '2025-08-05');


SELECT viajeros.nombre, tickets.numero_boleto, destinos.nombre_destino
FROM viajeros
LEFT JOIN tickets ON viajeros.viajero_id = tickets.viajero_id
LEFT JOIN destinos ON tickets.destino_id = destinos.destino_id;


-- Información de un boleto en específico
SELECT Viajeros.*, Tickets.*, Destinos.*
FROM Tickets
JOIN Viajeros ON Tickets.viajero_id = Viajeros.viajero_id
JOIN Destinos ON Tickets.destino_id = Destinos.destino_id
WHERE Tickets.numero_boleto = 'T666666';

-- Listar todos los viajeros que tienen fecha de salida o de retorno el '2024-01-10'
SELECT Viajeros.*
FROM Viajeros
JOIN Tickets ON Viajeros.viajero_id = Tickets.viajero_id
WHERE Tickets.fecha_salida = '2024-01-10' OR Tickets.fecha_retorno = '2024-01-10';

-- Obtener el número total de boletos por cada género
SELECT Viajeros.genero, COUNT(Tickets.ticket_id) AS "Total Boletos"
FROM viajeros
LEFT JOIN Tickets ON Viajeros.viajero_id = Tickets.viajero_id
GROUP BY Viajeros.genero;

-- Obtener un listado de todos los viajeros que han viajado a Playa del Carmen
SELECT Viajeros.*
FROM viajeros
JOIN Tickets ON Viajeros.viajero_id = Tickets.viajero_id
JOIN Destinos ON Tickets.destino_id = Destinos.destino_id
WHERE Destinos.nombre_destino = 'Playa del Carmen';

-- INSERTS
INSERT INTO Tickets (destino_id, viajero_id, numero_boleto, fecha_salida, fecha_retorno)
VALUES (3, 4, 'T171717', '2024-03-28', '2024-04-01');

-- Falla porque el numero de boleto es UNIQUE
INSERT INTO Tickets (destino_id, viajero_id, numero_boleto, fecha_salida, fecha_retorno)
VALUES (5, 10, 'T888888', '2024-03-28', '2024-04-01');

INSERT INTO Tickets (destino_id, numero_boleto, fecha_salida, fecha_retorno)
VALUES (4, 'T202020', '2024-03-28', '2024-04-01')


-- DELETES
DELETE FROM Tickets WHERE ticket_id = 4;

DELETE FROM Viajeros WHERE viajero_id = 2;
-- No se puede borrar por tener tickets asociados

DELETE FROM Destinos WHERE destino_id = 5;
-- No se puede borrar por tener tickets asociados

DELETE FROM Tickets
WHERE viajero_id = 2 OR destino_id = 5;
-- Primero necesito borrar las dependencias para poder eliminar el viajero 2 y el destino 5.


CREATE TABLE Paises (
    pais_id SERIAL PRIMARY KEY,
    nombre_pais VARCHAR(100) NOT NULL,
    ciudad VARCHAR(50),
    codigo_postal VARCHAR(20) NOT NULL
);

INSERT INTO Paises (nombre_pais, ciudad, codigo_postal) VALUES
('México', 'Playa del Carmen', '12345'),
('Perú', 'Cuzco', '54321'),
('Chile', 'Puerto Natales', '67890'),
('Australia', 'Queensland', '11111'),
('Nepal', 'Khumbu', '22222'),
('Grecia', 'Santorini', '33333'),
('Marruecos', 'Marrakech', '44444'),
('Japón', 'Kioto', '55555');

ALTER TABLE destinos
ADD COLUMN pais_id INT REFERENCES Paises(pais_id);

UPDATE Destinos
SET pais_id = (
    SELECT pais_id
    FROM Paises
    WHERE Paises.nombre_pais = Destinos.pais
    LIMIT 1
);

ALTER TABLE destinos
DROP COLUMN pais,
DROP COLUMN ciudad;