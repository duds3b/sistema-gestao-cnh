CREATE DATABASE mydb;

USE mydb;

CREATE TABLE pessoa (
    Id_pessoa INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100),
    Sobrenome VARCHAR(100)
);

CREATE TABLE habilitacao (
    Num_Habilitacao VARCHAR(50) PRIMARY KEY,
    Validade DATE,
    Pessoa_Id_pessoa INT,
    FOREIGN KEY (Pessoa_Id_pessoa)
        REFERENCES pessoa(Id_pessoa)
);