DROP TABLE IF EXISTS tasks;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    artist_id INT NOT NULL REFERENCES artists(id) ON DELETE CASCADE,
    genre VARCHAR(255)
);