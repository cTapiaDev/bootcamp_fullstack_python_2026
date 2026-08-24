CREATE TABLE peliculas (
    id INT PRIMARY KEY,
    Titulo VARCHAR(255),
    Año_estreno INT,
    Director VARCHAR(255)
);

CREATE TABLE reparto (
    id_pelicula INT,
    actor VARCHAR(255),
    FOREIGN KEY (id_pelicula) REFERENCES peliculas(id)
);

-- \copy peliculas FROM 'C:\Users\ctapi\CURSOS\bootcamp_fullstack_python_2026\04_modulo\03_unidad\guiado_peliculas\peliculas.csv' csv header;
-- \copy reparto FROM 'C:\Users\ctapi\CURSOS\bootcamp_fullstack_python_2026\04_modulo\03_unidad\guiado_peliculas\reparto.csv' csv header;


-- Obtener el ID de la película “Titanic”
SELECT id
FROM peliculas
WHERE titulo = 'Titanic';

-- Listar a todos los actores que aparecen en la película "Titanic"
SELECT
    reparto.id_pelicula,
    reparto.actor AS nombre_actor,
    peliculas.titulo
FROM peliculas
INNER JOIN reparto ON peliculas.id = reparto.id_pelicula
WHERE peliculas.titulo = 'Titanic';

SELECT actor
FROM reparto
WHERE id_pelicula = (
    SELECT id
    FROM peliculas
    WHERE titulo = 'Titanic'
);

-- Consultar en cuántas películas del top 100 participa Harrison Ford
SELECT
    reparto.id_pelicula,
    reparto.actor AS nombre_actor,
    peliculas.titulo
FROM peliculas
INNER JOIN reparto ON peliculas.id = reparto.id_pelicula
WHERE reparto.actor = 'Harrison Ford';

SELECT COUNT(*) AS "Películas de Harrison Ford"
FROM reparto
WHERE actor = 'Harrison Ford';

-- Indicar las películas estrenadas entre los años 1990 y 1999 ordenadas por título de manera ascendente.
SELECT Titulo, Año_estreno
FROM peliculas
WHERE Año_estreno BETWEEN 1990 AND 1999
ORDER BY Titulo ASC;

-- Hacer una consulta SQL que muestre los títulos con su longitud, la longitud debe ser nombrado para la consulta como “longitud_titulo”.
SELECT Titulo, LENGTH(Titulo) AS longitud_titulo
FROM peliculas;

-- Consultar cual es la longitud más grande entre todos los títulos de las películas.
SELECT MAX(LENGTH(Titulo)) AS longitud_maxima
FROM peliculas;

SELECT titulo, LENGTH(titulo) AS longitud_nombre
FROM peliculas
WHERE LENGTH(titulo) = (
    SELECT MAX(LENGTH(titulo)) 
    FROM peliculas
);