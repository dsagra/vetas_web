-- Script SQL para crear la tabla CONSULTA_WEB
-- Esta tabla almacena las consultas recibidas desde el formulario de contacto

CREATE TABLE IF NOT EXISTS `CONSULTA_WEB` (
  `ID` INT(11) NOT NULL AUTO_INCREMENT,
  `NOMBRE` VARCHAR(255) NOT NULL COMMENT 'Nombre completo del contacto',
  `EMAIL` VARCHAR(255) NOT NULL COMMENT 'Email del contacto',
  `TELEFONO` VARCHAR(50) DEFAULT NULL COMMENT 'Teléfono del contacto',
  `EMPRESA` VARCHAR(255) DEFAULT NULL COMMENT 'Empresa del contacto',
  `PAIS` VARCHAR(100) DEFAULT NULL COMMENT 'País del contacto',
  `MENSAJE` TEXT NOT NULL COMMENT 'Mensaje o consulta',
  `FECHA` DATETIME NOT NULL COMMENT 'Fecha y hora de la consulta',
  `IDIOMA` VARCHAR(5) DEFAULT 'es' COMMENT 'Idioma en que se envió (es, en, br)',
  `LEIDO` TINYINT(1) DEFAULT 0 COMMENT 'Indica si fue leído (0=no, 1=sí)',
  `RESPONDIDO` TINYINT(1) DEFAULT 0 COMMENT 'Indica si fue respondido (0=no, 1=sí)',
  `NOTAS` TEXT DEFAULT NULL COMMENT 'Notas internas sobre la consulta',
  PRIMARY KEY (`ID`),
  KEY `idx_fecha` (`FECHA`),
  KEY `idx_leido` (`LEIDO`),
  KEY `idx_email` (`EMAIL`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='Consultas recibidas desde el formulario web';

-- Índices adicionales para optimizar consultas
CREATE INDEX idx_idioma ON CONSULTA_WEB(IDIOMA);
CREATE INDEX idx_respondido ON CONSULTA_WEB(RESPONDIDO);
