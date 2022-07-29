-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema pollution-db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema pollution-db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `pollution-db` DEFAULT CHARACTER SET utf8 ;
USE `pollution-db` ;

-- -----------------------------------------------------
-- Table `pollution-db`.`station`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pollution-db`.`station` ;

CREATE TABLE IF NOT EXISTS `pollution-db`.`station` (
  `id` INT NOT NULL,
  `name` VARCHAR(100) NOT NULL,
  `geo_point_2d` VARCHAR(30) NOT NULL,
  UNIQUE INDEX `geo_point_2d_UNIQUE` (`name` ASC) VISIBLE,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pollution-db`.`readings`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pollution-db`.`readings` ;

CREATE TABLE IF NOT EXISTS `pollution-db`.`readings` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `type` VARCHAR(45) NULL,
  `instrument_type_id` INT NULL,
  `nox` FLOAT NULL,
  `no2` FLOAT NULL,
  `no` FLOAT NULL,
  `pm_10` FLOAT NULL,
  `nvpm_10` FLOAT NULL,
  `vpm_10` FLOAT NULL,
  `nvpm_25` FLOAT NULL,
  `pm_25` FLOAT NULL,
  `vpm_25` FLOAT NULL,
  `co` FLOAT NULL,
  `03` FLOAT NULL,
  `so2` FLOAT NULL,
  `air_temperature` FLOAT NULL,
  `rh` FLOAT NULL,
  `air_pressure` FLOAT NULL,
  `date_start` DATETIME NULL,
  `date_end` DATETIME NULL,
  `current` TINYINT NULL,
  `instrument_type` VARCHAR(45) NULL,
  `station_id` INT NOT NULL,
  `Date_Time` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_station_id_idx` (`station_id` ASC) VISIBLE,
  CONSTRAINT `fk_station_id`
    FOREIGN KEY (`station_id`)
    REFERENCES `pollution-db`.`station` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pollution-db`.`schema`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pollution-db`.`schema` ;

CREATE TABLE IF NOT EXISTS `pollution-db`.`schema` (
  `id` INT NULL,
  `measure` VARCHAR(45) NULL,
  `desc` VARCHAR(45) NULL,
  `unit` VARCHAR(45) NULL)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
