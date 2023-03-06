-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema BioparkEdificios
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema BioparkEdificios
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `BioparkEdificios` DEFAULT CHARACTER SET utf8 ;
USE `BioparkEdificios` ;

-- -----------------------------------------------------
-- Table `BioparkEdificios`.`Edificios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BioparkEdificios`.`Edificios` (
  `id_edificio` INT NOT NULL,
  `bloco_edificio` VARCHAR(45) NULL,
  PRIMARY KEY (`id_edificio`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BioparkEdificios`.`Apartamentos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BioparkEdificios`.`Apartamentos` (
  `nr_apartamento` INT NOT NULL,
  `mensalidade_apt` FLOAT NULL,
  `disponibilidade` VARCHAR(45) NULL,
  `id_edificio_apt` INT NULL,
  PRIMARY KEY (`nr_apartamento`),
  INDEX `fk_Apartamentos_Edificios1_idx` (`id_edificio_apt` ASC) VISIBLE,
  CONSTRAINT `fk_Apartamentos_Edificios1`
    FOREIGN KEY (`id_edificio_apt`)
    REFERENCES `BioparkEdificios`.`Edificios` (`id_edificio`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BioparkEdificios`.`Locatarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BioparkEdificios`.`Locatarios` (
  `nome_completo` VARCHAR(150) NULL,
  `cpf` VARCHAR(20) NOT NULL,
  `celular` VARCHAR(20) NULL,
  `mensalidade` FLOAT NULL,
  `id_edificio_loc` INT NULL,
  `nr_apartamento_loc` INT NULL,
  `disponibilidade_apt` VARCHAR(45) NULL,
  PRIMARY KEY (`cpf`),
  INDEX `fk_Locatario_Edificio_A_idx` (`nr_apartamento_loc` ASC) VISIBLE,
  CONSTRAINT `fk_Locatario_Edificio_A`
    FOREIGN KEY (`nr_apartamento_loc`)
    REFERENCES `BioparkEdificios`.`Apartamentos` (`nr_apartamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
