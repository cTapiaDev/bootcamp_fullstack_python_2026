CREATE TABLE editoriales (
    editorial_id SERIAL PRIMARY KEY,
    nombre_editorial VARCHAR(100) NOT NULL
);

CREATE TABLE autores (
    autor_id SERIAL PRIMARY KEY,
    nombre_autor VARCHAR(100) NOT NULL,
    nacionalidad VARCHAR(50)
);

-- Tabla transaccional/hija
CREATE TABLE libros (
    libro_id SERIAL PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    precio NUMERIC NOT NULL,
    autor_id INT REFERENCES autores(autor_id),
    editorial_id INT REFERENCES editoriales(editorial_id)
);

INSERT INTO editoriales (nombre_editorial)
VALUES ('Planeta'), ('Penguin Random House');

INSERT INTO autores (nombre_autor, nacionalidad)
VALUES ('Gabriel García Márquez', 'Colombiana'), ('Isabel Allende', 'Chilena');

INSERT INTO libros (titulo, precio, autor_id, editorial_id) VALUES
('Cien años de soledad', 15000, 1, 2),
('La casa de los espíritus', 12000, 2, 1)

-- Error por intentar insertar un libro con un autor que no existe.
INSERT INTO libros (titulo, precio, autor_id, editorial_id) VALUES
('Libro Fantasma', 10000, 99, 1);

-- Error porque no puedo borrar un autor que ya está relacionado a un libro.
DELETE FROM autores
WHERE autor_id = 1;

-- Para poder eliminarlo primero debemos eliminar todas sus dependencias.
DELETE FROM libros WHERE autor_id = 1;
DELETE FROM autores WHERE autor_id = 1;

SELECT
    l.titulo,
    a.nombre_autor AS "Nombre Autor",
    e.nombre_editorial AS "Editorial",
    l.precio
FROM libros AS l
INNER JOIN autores AS a ON l.autor_id = a.autor_id
INNER JOIN editoriales AS e ON l.editorial_id = e.editorial_id;