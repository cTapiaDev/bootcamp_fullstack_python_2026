CREATE TABLE peliculas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255),
    anno INT
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    tag VARCHAR(32)
);

CREATE TABLE pelicula_tag (
    pelicula_id INT REFERENCES peliculas(id),
    tag_id INT REFERENCES tags(id),
    PRIMARY KEY (pelicula_id, tag_id)
);

INSERT INTO peliculas (nombre, anno) VALUES
('Interestelar', 2014),
('El Padrino', 1972),
('Inception', 2010),
('Matrix', 1999),
('Avatar', 2009);

INSERT INTO tags (tag) VALUES
('Ciencia Ficción'),
('Drama'),
('Acción'),
('Suspenso'),
('Aventura');

INSERT INTO pelicula_tag (pelicula_id, tag_id) VALUES
(1, 1), (1, 3), (1, 5),
(2, 2), (2, 4);

-- Cuenta la cantidad de tags que tiene cada película. Si una película no tiene tags debe mostrar 0.
SELECT p.nombre, COUNT(pt.tag_id) AS cantidad_tags
FROM peliculas p
LEFT JOIN pelicula_tag pt ON p.id = pt.pelicula_id
GROUP BY p.nombre, p.id
ORDER BY p.id ASC;


------------------------------------

CREATE TABLE preguntas (
    id SERIAL PRIMARY KEY,
    pregunta VARCHAR (255),
    respuesta_correcta VARCHAR
);

CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255),
    edad INT
);

CREATE TABLE respuestas (
    id SERIAL PRIMARY KEY,
    respuesta VARCHAR(255),
    usuario_id INT REFERENCES usuarios(id),
    pregunta_id INT REFERENCES preguntas(id)
);

INSERT INTO usuarios (nombre, edad) VALUES
('Javier', 25), ('Maria', 30), ('Pedro', 40), ('Diego', 22), ('Ana', 28);

INSERT INTO preguntas (pregunta, respuesta_correcta) VALUES
('¿Capital de Chile?', 'Santiago'),
('¿Cuánto es 2+2?', '4'),
('¿Color del cielo despejado?', 'Azul'),
('¿Planeta más cercano al sol?', 'Mercurio'),
('¿Símbolo químico del agua?', 'H2O');

INSERT INTO respuestas (respuesta, usuario_id, pregunta_id) VALUES
('Santiago', 1, 1),
('Santiago', 2, 1),
('4', 3, 2),
('Verde', 4, 3),
('Tierra', 5, 4);

-- Cuenta la cantidad de respuestas correctas totales por usuario (independiente de la pregunta).
SELECT u.nombre, COUNT(p.id) AS respuestas_correctas
FROM usuarios u
LEFT JOIN respuestas r ON u.id = r.usuario_id
LEFT JOIN preguntas p ON r.pregunta_id = p.id AND r.respuesta = p.respuesta_correcta
GROUP BY u.id, u.nombre
ORDER BY u.id;

-- Por cada pregunta, en la tabla preguntas, cuenta cuántos usuarios tuvieron la respuesta correcta.
SELECT p.pregunta, COUNT(r.id) AS usuarios_correctos
FROM preguntas p
LEFT JOIN respuestas r ON p.id = r.pregunta_id AND p.respuesta_correcta = r.respuesta
GROUP BY p.pregunta, p.id
ORDER BY p.id;

-- Implementa borrado en cascada de las respuestas al borrar un usuario y borrar el primer usuario para probar la implementación.
ALTER TABLE respuestas DROP CONSTRAINT respuestas_usuario_id_fkey;
ALTER TABLE respuestas ADD CONSTRAINT respuestas_usuario_id_fkey
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE;

DELETE FROM usuarios WHERE id = 1;

-- Crea una restricción que impida insertar usuarios menores de 18 años en la base de datos.
ALTER TABLE usuarios ADD CONSTRAINT check_edad CHECK (edad >= 18);

-- Altera la tabla existente de usuarios agregando el campo email con la restricción de único.
ALTER TABLE usuarios ADD COLUMN email VARCHAR(150) UNIQUE;