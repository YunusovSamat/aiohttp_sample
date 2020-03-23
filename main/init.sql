DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS files;

CREATE TABLE users (
    id_user SERIAL PRIMARY KEY,
    email VARCHAR(40) UNIQUE NOT NULL,
    name VARCHAR(30) NOT NULL,
    surname VARCHAR(30) NOT NULL,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE files (
    id_file SERIAL PRIMARY KEY,
    id_user INT REFERENCES users (id_user),
    file VARCHAR(40) NOT NULL,
    url VARCHAR(150) NOT NULL,
    url_download VARCHAR(150) NOT NULL
)
