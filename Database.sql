CREATE DATABASE voter_storage;

CREATE TABLE votes (
    id INT NOT NULL AUTO_INCREMENT,
    candidate INT NOT NULL,
    PRIMARY KEY (id)
);
