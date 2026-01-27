-- ============================================
-- TABLA DE SUSCRIPTORES - VETAS
-- Sistema de suscripción por email
-- ============================================

-- Crear tabla de suscriptores
CREATE TABLE IF NOT EXISTS SUSCRIPTORES (
  -- ID único autoincremental
  ID INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  
  -- Datos del suscriptor
  EMAIL VARCHAR(255) NOT NULL UNIQUE COMMENT 'Email del suscriptor (único)',
  NOMBRE VARCHAR(255) DEFAULT NULL COMMENT 'Nombre del suscriptor (opcional)',
  
  -- Configuración
  IDIOMA VARCHAR(5) DEFAULT 'es' COMMENT 'Idioma preferido: es, en, br',
  ACTIVO TINYINT(1) DEFAULT 1 COMMENT '1=Activo, 0=Inactivo/Desuscrito',
  
  -- Metadatos
  FECHA DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Fecha y hora de suscripción',
  IP VARCHAR(50) DEFAULT NULL COMMENT 'IP del suscriptor al momento de suscribirse',
  TOKEN VARCHAR(64) DEFAULT NULL COMMENT 'Token único para desuscripción',
  
  -- Timestamps
  CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UPDATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  
  -- Índices para optimización
  INDEX idx_email (EMAIL),
  INDEX idx_activo (ACTIVO),
  INDEX idx_fecha (FECHA),
  INDEX idx_idioma (IDIOMA),
  INDEX idx_token (TOKEN)
  
) ENGINE=InnoDB 
  DEFAULT CHARSET=utf8mb4 
  COLLATE=utf8mb4_unicode_ci 
  COMMENT='Suscriptores de la revista VETAS';

-- ============================================
-- Trigger para generar TOKEN automáticamente
-- ============================================

DELIMITER //

CREATE TRIGGER before_insert_suscriptores
BEFORE INSERT ON SUSCRIPTORES
FOR EACH ROW
BEGIN
  -- Generar token único para desuscripción
  IF NEW.TOKEN IS NULL THEN
    SET NEW.TOKEN = MD5(CONCAT(NEW.EMAIL, NOW(), RAND()));
  END IF;
END//

DELIMITER ;

-- ============================================
-- Vista para suscriptores activos
-- ============================================

CREATE OR REPLACE VIEW v_suscriptores_activos AS
SELECT 
  ID,
  EMAIL,
  NOMBRE,
  IDIOMA,
  FECHA,
  CREATED_AT
FROM SUSCRIPTORES
WHERE ACTIVO = 1
ORDER BY FECHA DESC;

-- ============================================
-- Procedimiento para desuscribir por token
-- ============================================

DELIMITER //

CREATE PROCEDURE sp_desuscribir(IN p_token VARCHAR(64))
BEGIN
  UPDATE SUSCRIPTORES 
  SET ACTIVO = 0,
      UPDATED_AT = NOW()
  WHERE TOKEN = p_token
    AND ACTIVO = 1;
    
  -- Retornar resultado
  SELECT ROW_COUNT() AS rows_affected;
END//

DELIMITER ;

-- ============================================
-- Procedimiento para reactivar suscripción
-- ============================================

DELIMITER //

CREATE PROCEDURE sp_reactivar_suscripcion(IN p_email VARCHAR(255))
BEGIN
  UPDATE SUSCRIPTORES 
  SET ACTIVO = 1,
      UPDATED_AT = NOW()
  WHERE EMAIL = p_email
    AND ACTIVO = 0;
    
  SELECT ROW_COUNT() AS rows_affected;
END//

DELIMITER ;

-- ============================================
-- Estadísticas de suscriptores
-- ============================================

CREATE OR REPLACE VIEW v_estadisticas_suscriptores AS
SELECT 
  COUNT(*) AS total_suscriptores,
  SUM(CASE WHEN ACTIVO = 1 THEN 1 ELSE 0 END) AS activos,
  SUM(CASE WHEN ACTIVO = 0 THEN 1 ELSE 0 END) AS inactivos,
  SUM(CASE WHEN IDIOMA = 'es' THEN 1 ELSE 0 END) AS espanol,
  SUM(CASE WHEN IDIOMA = 'en' THEN 1 ELSE 0 END) AS ingles,
  SUM(CASE WHEN IDIOMA = 'br' THEN 1 ELSE 0 END) AS portugues,
  DATE(MIN(FECHA)) AS primera_suscripcion,
  DATE(MAX(FECHA)) AS ultima_suscripcion
FROM SUSCRIPTORES;

-- ============================================
-- Datos de prueba (opcional - remover en producción)
-- ============================================

-- Insertar suscriptores de prueba
INSERT INTO SUSCRIPTORES (EMAIL, NOMBRE, IDIOMA, FECHA, IP, ACTIVO) VALUES
('test1@example.com', 'Usuario Test 1', 'es', NOW(), '127.0.0.1', 1),
('test2@example.com', 'Usuario Test 2', 'en', NOW(), '127.0.0.1', 1),
('test3@example.com', 'Usuario Test 3', 'br', NOW(), '127.0.0.1', 1);

-- ============================================
-- Queries útiles
-- ============================================

-- Ver todos los suscriptores activos
-- SELECT * FROM v_suscriptores_activos;

-- Ver estadísticas
-- SELECT * FROM v_estadisticas_suscriptores;

-- Buscar suscriptor por email
-- SELECT * FROM SUSCRIPTORES WHERE EMAIL = 'ejemplo@email.com';

-- Desuscribir usando procedimiento
-- CALL sp_desuscribir('TOKEN_AQUI');

-- Reactivar suscripción
-- CALL sp_reactivar_suscripcion('ejemplo@email.com');

-- Suscriptores por idioma
-- SELECT IDIOMA, COUNT(*) as cantidad 
-- FROM SUSCRIPTORES 
-- WHERE ACTIVO = 1 
-- GROUP BY IDIOMA;

-- Suscriptores por mes
-- SELECT 
--   DATE_FORMAT(FECHA, '%Y-%m') as mes,
--   COUNT(*) as nuevos_suscriptores
-- FROM SUSCRIPTORES
-- GROUP BY DATE_FORMAT(FECHA, '%Y-%m')
-- ORDER BY mes DESC;

-- ============================================
-- Mantenimiento
-- ============================================

-- Eliminar suscriptores inactivos antiguos (más de 2 años)
-- DELETE FROM SUSCRIPTORES 
-- WHERE ACTIVO = 0 
--   AND UPDATED_AT < DATE_SUB(NOW(), INTERVAL 2 YEAR);

-- Limpiar emails duplicados (mantener el más reciente)
-- DELETE s1 FROM SUSCRIPTORES s1
-- INNER JOIN SUSCRIPTORES s2 
-- WHERE s1.ID < s2.ID 
--   AND s1.EMAIL = s2.EMAIL;

-- ============================================
-- Backup recomendado
-- ============================================

-- mysqldump -u usuario -p database SUSCRIPTORES > suscriptores_backup.sql

-- ============================================
-- Notas de implementación
-- ============================================

/*
1. Esta tabla soporta multiidioma (es, en, br)
2. El token permite desuscripción segura vía URL
3. La vista v_suscriptores_activos facilita consultas
4. Los procedimientos almacenados simplifican operaciones comunes
5. Los índices optimizan las búsquedas frecuentes

Seguridad:
- Email es único (no permite duplicados)
- Token generado automáticamente
- IP registrada para auditoría
- Timestamps automáticos

Performance:
- Índices en campos más consultados
- Vista materializada para estadísticas
- Engine InnoDB para transacciones

Mantenimiento:
- Soft delete (ACTIVO flag)
- Procedimientos para operaciones comunes
- Triggers para automatización
*/
