-- --------------------------------------------------------
-- Host:                         localhost
-- Versión del servidor:         5.7.24 - MySQL Community Server (GPL)
-- SO del servidor:              Win32
-- HeidiSQL Versión:             10.2.0.5599
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para db_factura
DROP DATABASE IF EXISTS `db_factura_g19`;
CREATE DATABASE IF NOT EXISTS `db_factura_g19` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
USE `db_factura_g19`;

-- Volcando estructura para tabla db_factura.tbl_cliente
DROP TABLE IF EXISTS `tbl_cliente`;
CREATE TABLE IF NOT EXISTS `tbl_cliente` (
  `cliente_id` int(11) NOT NULL AUTO_INCREMENT,
  `cliente_rsocial` varchar(255) COLLATE utf8_bin NOT NULL,
  `cliente_ruc` varchar(20) COLLATE utf8_bin NOT NULL,
  `cliente_direccion` longtext COLLATE utf8_bin NOT NULL,
  `cliente_estado` char(1) COLLATE utf8_bin NOT NULL DEFAULT '1',
  `cliente_fecha_log` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `cliente_usuario_log` varchar(255) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`cliente_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla db_factura.tbl_factura_cab
DROP TABLE IF EXISTS `tbl_factura_cab`;
CREATE TABLE IF NOT EXISTS `tbl_factura_cab` (
  `factura_cab_id` int(11) NOT NULL AUTO_INCREMENT,
  `factura_cab_serie` varchar(20) COLLATE utf8_bin NOT NULL,
  `factura_cab_nro` varchar(255) COLLATE utf8_bin NOT NULL,
  `factura_cab_fvencimiento` date NOT NULL,
  `factura_cab_femision` date NOT NULL,
  `factura_cab_tipo_moneda` varchar(45) COLLATE utf8_bin NOT NULL DEFAULT 'SOLES',
  `factura_cab_observacion` longtext COLLATE utf8_bin,
  `factura_cab_valorventa` double NOT NULL,
  `factura_cab_valorigv` double NOT NULL,
  `factura_cab_valortotal` double NOT NULL,
  `factura_cab_estado` char(1) COLLATE utf8_bin NOT NULL DEFAULT '1',
  `factura_cab_fecha_log` timestamp NOT NULL,
  `factura_cab_usuario_log` varchar(255) COLLATE utf8_bin NOT NULL,
  `cliente_id` int(11) NOT NULL,
  PRIMARY KEY (`factura_cab_id`),
  KEY `fk_tbl_factura_cab_tbl_cliente` (`cliente_id`),
  CONSTRAINT `fk_tbl_factura_cab_tbl_cliente` FOREIGN KEY (`cliente_id`) REFERENCES `tbl_cliente` (`cliente_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla db_factura.tbl_factura_det
DROP TABLE IF EXISTS `tbl_factura_det`;
CREATE TABLE IF NOT EXISTS `tbl_factura_det` (
  `factura_det_id` int(11) NOT NULL AUTO_INCREMENT,
  `factura_det_precio` double NOT NULL,
  `factura_det_cantidad` double NOT NULL,
  `factura_det_subtotal` double NOT NULL,
  `factura_det_fecha_log` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `factura_det_usuario_log` varchar(255) COLLATE utf8_bin NOT NULL,
  `producto_id` int(11) NOT NULL,
  `factura_cab_id` int(11) NOT NULL,
  PRIMARY KEY (`factura_det_id`),
  KEY `fk_tbl_factura_det_tbl_producto1` (`producto_id`),
  KEY `fk_tbl_factura_det_tbl_factura_cab1` (`factura_cab_id`),
  CONSTRAINT `fk_tbl_factura_det_tbl_factura_cab1` FOREIGN KEY (`factura_cab_id`) REFERENCES `tbl_factura_cab` (`factura_cab_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_tbl_factura_det_tbl_producto1` FOREIGN KEY (`producto_id`) REFERENCES `tbl_producto` (`producto_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla db_factura.tbl_producto
DROP TABLE IF EXISTS `tbl_producto`;
CREATE TABLE IF NOT EXISTS `tbl_producto` (
  `producto_id` int(11) NOT NULL AUTO_INCREMENT,
  `producto_codigo` varchar(255) COLLATE utf8_bin NOT NULL,
  `producto_precio` double NOT NULL,
  `producto_estado` char(1) COLLATE utf8_bin NOT NULL DEFAULT '1',
  `producto_fecha_log` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `producto_usuario_log` varchar(255) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`producto_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- La exportación de datos fue deseleccionada.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
