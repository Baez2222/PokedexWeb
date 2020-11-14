DROP DATABASE IF EXISTS `Pokedex`;
CREATE DATABASE `Pokedex`;
USE `Pokedex`;

-- Types Table
DROP TABLE IF EXISTS `pokemonTypes`;
CREATE TABLE `pokemonTypes`(
`name` VARCHAR(10) NOT NULL,
`normal` FLOAT,
`fire` FLOAT,
`water` FLOAT,
`electric` FLOAT,
`grass` FLOAT,
`ice` FLOAT,
`fighting` FLOAT,
`poison` FLOAT,
`ground` FLOAT,
`flying` FLOAT,
`psychic` FLOAT,
`bug` FLOAT,
`rock` FLOAT,
`ghost` FLOAT,
`dragon` FLOAT,
`dark` FLOAT,
`steel` FLOAT,
`fairy` FLOAT,
`ID` INT,
PRIMARY KEY (`name`)
);

insert  into `pokemonTypes` (`name`, `normal`, `fire`, `water`, `electric`, `grass`, `ice`, `fighting`, `poison`, `ground`, `flying`, `psychic`, `bug`, `rock`, `ghost`, `dragon`, `dark`, `steel`, `fairy`, `ID`)
 values('normal', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, .5, 0, 1, 1, .5, 1, 1),
('fire', 1, .5, .5, 1, 2, 2, 1, 1, 1, 1, 1, 2, .5, 1, .5, 1, 2, 1, 2) ,
('water', 1, 2, .5, 1, .5, 1, 1, 1, 2, 1, 1, 1, 2, 1, .5, 1, 1, 1, 3),
('electric', 1, 1, 2, .5, .5, 1, 1, 1, 0, 2, 1, 1, 1, 1, .5, 1, 1, 1, 4),
('grass', 1, .5, 2, 1, .5, 1, 1, .5, 2, .5, 1, .5, 2, 1, .5, 1, .5, 1, 5),
('ice', 1, .5, .5, 1, 2, .5, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, .5, 1, 6),
('fighting', 2, 1, 1, 1, 1, 2, 1, .5, 1, .5, .5, .5, 2, 0, 1, 2, 2, .5, 7),
('poison', 1, 1, 1, 1, 2, 1, 1, .5, .5, 1, 1, 1, .5, .5, 1, 1, 0, 2, 8),
('ground',1, 2, 1, 2, .5, 1, 1, 2, 1, 0, 1, .5, 2, 1, 1, 1, 2, 1, 9),
('flying', 1, 1, 1, .5, 2, 1, 2, 1, 1, 1, 1, 2, .5, 1, 1, 1, .5, 1, 10),
('psychic',1, 1, 1, 1, 1, 1, 2, 2, 1, 1, .5, 1, 1, 1, 1, 0, .5, 1, 11),
('bug', 1, .5, 1, 1, 2, 1, .5, .5, 1, .5, 2, 1, 1, .5, 1, 2, .5, .5, 12),
('rock', 1, 2, 1, 1, 1, 2, .5, 1, .5, 2, 1, 2, 1, 1, 1, 1, .5, 1, 13),
('ghost', 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, .5, 1, 1, 14),
('dragon', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, .5, 0, 15),
('dark', 1, 1, 1, 1, 1, 1, .5, 1, 1, 1, 2, 1, 1, 2, 1, .5, 1, .5, 16),
('steel', 1, .5, .5, .5, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, .5, 2, 17),
('fairy', 1, .5, 1, 1, 1, 1, 2, .5, 1, 1, 1, 1, 1, 1, 2, 2, .5, 1, 18);



-- Move Table
DROP TABLE IF EXISTS `moves`;
CREATE TABLE `moves`(
`name` VARCHAR(30) NOT NULL,
`type` VARCHAR(10) NOT NULL,
`category` VARCHAR(10),
`PP` INT NOT NULL,
`power` INT,
`accuracy` INT,
`description` VARCHAR(200) NOT NULL,
PRIMARY KEY (`name`)/*,
FOREIGN KEY (`type`) REFERENCES `moveTypes` (`name`) ON DELETE CASCADE ON UPDATE CASCADE*/
);


-- Pokemon Table
DROP TABLE IF EXISTS `pokemon`;
CREATE TABLE `pokemon`(
`pokeID` INT NOT NULL,
`name` VARCHAR(20) NOT NULL,
`primaryType` VARCHAR(10),
`secondaryType` VARCHAR(10),
`description` VARCHAR(100),
`ability1` VARCHAR(20),
`ability2` VARCHAR(20),
`ability3` VARCHAR(20),
`hp` INT NOT NULL,
`attack` INT NOT NULL,
`defense` INT NOT NULL,
`sp_attack` INT NOT NULL,
`sp_defense` INT NOT NULL,
`speed` INT NOT NULL,
`region` VARCHAR(10),
PRIMARY KEY (`pokeID`)/*,
FOREIGN KEY (`primaryType`) REFERENCES `pokemonTypes` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (`secondaryType`) REFERENCES `pokemonTypes` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (`ability`) REFERENCES `abilities` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (`region`) REFERENCES `regions` (`name`) ON DELETE CASCADE ON UPDATE CASCADE*/
);

-- Pokemon Movesets Table
DROP TABLE IF EXISTS `pokemonMovesets`;
CREATE TABLE `pokemonMovesets`(
`pokeID` INT NOT NULL,
`moveName` VARCHAR(20) NOT NULL,
FOREIGN KEY (`pokeID`) REFERENCES `pokemon` (`pokeID`)
);



SELECT *
FROM pokemon p WHERE p.name = "Bulbasaur";

SELECT *
FROM pokemon p WHERE p.primaryType = "Grass" OR p.secondaryType = "Grass";

SELECT *
FROM pokemonTypes pt WHERE pt.name = "Normal";

SELECT pt.normal
FROM pokemonTypes pt;

SELECT *
FROM pokemonTypes pt ORDER BY pt.ID;

SELECT *
FROM moves;