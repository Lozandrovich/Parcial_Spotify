create database spotify;
use spotify;
CREATE TABLE musica (
id INT AUTO_INCREMENT PRIMARY KEY,
cancion VARCHAR(100),
artista VARCHAR(100),
album VARCHAR(100),
anio INT,
duracion INT, -- en segundos
fecha_lanzamiento DATE,
hora_estreno TIME,
descripcion TEXT,
email_contacto VARCHAR(100),
activo BOOLEAN DEFAULT TRUE
);
INSERT INTO musica (cancion, artista, album, anio, duracion, fecha_lanzamiento,
hora_estreno, descripcion, email_contacto, activo) VALUES
('Sol de verano', 'Luna García', 'Calor', 2020, 210, '2020-01-15', '10:00:00', 'Canción ideal
para el verano, totalmente gratis.', 'luna@email.com', True),
('Amor eterno', 'Carlos Ríos', 'Romántico', 2019, 250, '2019-02-14', '20:30:00', 'Una balada
que llega al alma.', NULL, True),
('Ritmo salvaje', 'DJ Max', 'Fiesta', 2021, 180, '2021-05-10', '22:00:00', 'Perfecta para bailar
toda la noche.', 'djmax@music.net', True),
('Lluvia de estrellas', 'Estela Azul', 'Galaxia', 2018, 160, '2018-11-22', '18:45:00', 'Una obra
espacial sin comparación.', NULL, True),
('Tiempos modernos', 'Retro Beat', 'Vintage', 2022, 240, '2022-03-30', '19:15:00', 'Sonidos
clásicos en tiempos modernos.', 'contacto@retro.com', True),
('Fuego y pasión', 'Valentina Rey', 'Latidos', 2023, 200, '2023-07-01', '21:00:00', 'Romance
ardiente y letras profundas.', 'valentina@rey.com', True);