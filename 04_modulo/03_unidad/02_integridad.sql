CREATE TABLE clientes (
    id INTEGER UNIQUE NOT NULL,
    name VARCHAR(25) NOT NULL,
    email VARCHAR(50)
);

INSERT INTO clientes (id, name) VALUES 
(1, 'Nombre 1'),
(2, 'Nombre 2'),
(3, 'Nombre 3');

SELECT * FROM clientes;

ALTER TABLE clientes 
ALTER COLUMN email SET NOT NULL;

UPDATE clientes
SET email = ''
WHERE email IS NULL;

ALTER TABLE clientes
ADD COLUMN fecha DATE;

UPDATE clientes
SET fecha = COALESCE(fecha, '2024-01-01');

-------------------

CREATE TABLE autores (
    id INT NOT NULL,
    nombre VARCHAR(255) NOT NULL,

    PRIMARY KEY (id)
);

CREATE TABLE libros (
    id INT NOT NULL,
    titulo VARCHAR(255) NOT NULL,
    autor_id INT NOT NULL,

    PRIMARY KEY (id),
    FOREIGN KEY (autor_id) REFERENCES autores (id)
);

INSERT INTO autores (id, nombre) VALUES
(1, 'Juan Pérez'),
(2, 'María García'),
(3, 'Pedro Rodríguez');

INSERT INTO libros (id, titulo, autor_id) VALUES
(1, 'El Quijote', 1),
(2, 'La Divina Comedia', 2),
(3, 'Hamlet', 3);


SELECT libros.titulo, autores.nombre
FROM libros
INNER JOIN autores ON libros.autor_id = autores.id;

DELETE FROM libros;
DELETE FROM autores;
