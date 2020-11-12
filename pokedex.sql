DROP DATABASE IF EXISTS `Pokedex`;
CREATE DATABASE `Pokedex`;
USE `Pokedex`;

-- Pokemon Type Table
DROP TABLE IF EXISTS `pokemonTypes`;
CREATE TABLE `pokemonTypes`(
`name` VARCHAR(10) NOT NULL,
`dmg_from_normal` VARCHAR(10),
`dmg_from_water` VARCHAR(10),
`dmg_from_electric` VARCHAR(10),
`dmg_from_fighting` VARCHAR(10),
`dmg_from_ground` VARCHAR(10),
`dmg_from_psychic` VARCHAR(10),
`dmg_from_rock` VARCHAR(10),
`dmg_from_dark` VARCHAR(10),
`dmg_from_steel` VARCHAR(10),
`dmg_from_fire` VARCHAR(10),
`dmg_from_grass` VARCHAR(10),
`dmg_from_ice` VARCHAR(10),
`dmg_from_poison` VARCHAR(10),
`dmg_from_flying` VARCHAR(10),
`dmg_from_bug` VARCHAR(10),
`dmg_from_ghost` VARCHAR(10),
`dmg_from_dragon` VARCHAR(10),
`dmg_from_fairy` VARCHAR(10),
PRIMARY KEY (`name`)
);

-- Move Types Table
DROP TABLE IF EXISTS `moveTypes`;
CREATE TABLE `moveTypes`(
`name` VARCHAR(10) NOT NULL,
`dmg_to_normal` VARCHAR(10),
`dmg_to_water` VARCHAR(10),
`dmg_to_electric` VARCHAR(10),
`dmg_to_fighting` VARCHAR(10),
`dmg_to_ground` VARCHAR(10),
`dmg_to_psychic` VARCHAR(10),
`dmg_to_rock` VARCHAR(10),
`dmg_to_dark` VARCHAR(10),
`dmg_to_steel` VARCHAR(10),
`dmg_to_fire` VARCHAR(10),
`dmg_to_grass` VARCHAR(10),
`dmg_to_ice` VARCHAR(10),
`dmg_to_poison` VARCHAR(10),
`dmg_to_flying` VARCHAR(10),
`dmg_to_bug` VARCHAR(10),
`dmg_to_ghost` VARCHAR(10),
`dmg_to_dragon` VARCHAR(10),
`dmg_to_fairy` VARCHAR(10),
PRIMARY KEY (`name`)
);

-- Move Table
DROP TABLE IF EXISTS `moves`;
CREATE TABLE `moves`(
`name` VARCHAR(20) NOT NULL,
`type` VARCHAR(10) NOT NULL,
`category` VARCHAR(10) NOT NULL,
`PP` INT NOT NULL,
`power` INT NOT NULL,
`accuracy` INT NOT NULL,
`description` VARCHAR(100) NOT NULL,
PRIMARY KEY (`name`),
FOREIGN KEY (`type`) REFERENCES `moveTypes` (`name`) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Abilities Table
DROP TABLE IF EXISTS `abilities`;
CREATE TABLE `abilities`(
`name` VARCHAR(20) NOT NULL,
`description` VARCHAR(100) NOT NULL,
PRIMARY KEY (`name`)
);

-- Regions Table
DROP TABLE IF EXISTS `regions`;
CREATE TABLE `regions`(
`name` VARCHAR(10) NOT NULL,
`description` VARCHAR(100) NOT NULL,
PRIMARY KEY (`name`)
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
FROM pokemon;

