-- 1FN

CREATE TABLE pelicula_no_normalizada (
    id_pelicula INT,
    pelicula VARCHAR(100),
    genero VARCHAR(50),
    id_actor INT,
    actor VARCHAR(100)
);

INSERT INTO pelicula_no_normalizada VALUES
(1, 'Interestelar', 'Ficción', 1, 'Matthew McConaughey'),
(1, 'Interestelar', 'Ficción', 2, 'Anne Hathaway'),
(2, 'En busca de la felicidad', 'Drama', 3, 'Will Smith'),
(2, 'En busca de la felicidad', 'Drama', 4, 'Jaden Smith');

SELECT * FROM pelicula_no_normalizada;

CREATE TABLE pelicula (
    id_pelicula SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    genero VARCHAR(50) NOT NULL
);

CREATE TABLE actor (
    id_actor SERIAL PRIMARY KEY,
    nombre_actor VARCHAR(100) NOT NULL
);

INSERT INTO pelicula (titulo, genero) VALUES
('Interestelar', 'Ficción'),
('En busca de la felicidad', 'Drama');

INSERT INTO actor (nombre_actor) VALUES
('Matthew McConaughey'), ('Anne Hathaway'),
('Will Smith'), ('Jaden Smith');

SELECT * FROM pelicula;
SELECT * FROM actor;

-- 2FN
CREATE TABLE participacion (
    id_participacion SERIAL PRIMARY KEY,
    id_pelicula INT NOT NULL REFERENCES pelicula(id_pelicula) ON DELETE CASCADE,
    id_actor INT NOT NULL REFERENCES actor(id_actor) ON DELETE CASCADE
);

INSERT INTO participacion (id_pelicula, id_actor) VALUES
(1, 1), (1, 2), (2, 3), (2, 4);

SELECT * FROM participacion;