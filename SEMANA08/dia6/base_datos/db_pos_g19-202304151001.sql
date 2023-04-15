-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: db_pos_g19
-- ------------------------------------------------------
-- Server version	5.7.24

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tbl_categoria`
--

DROP TABLE IF EXISTS `tbl_categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_categoria` (
  `categoria_id` int(11) NOT NULL AUTO_INCREMENT,
  `categoria_nom` varchar(100) NOT NULL,
  PRIMARY KEY (`categoria_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_categoria`
--

LOCK TABLES `tbl_categoria` WRITE;
/*!40000 ALTER TABLE `tbl_categoria` DISABLE KEYS */;
INSERT INTO `tbl_categoria` VALUES (1,'ENTRADAS'),(2,'PLATOS DE FONDO'),(3,'BEBIDAS');
/*!40000 ALTER TABLE `tbl_categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_pedido`
--

DROP TABLE IF EXISTS `tbl_pedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_pedido` (
  `pedido_id` int(11) NOT NULL AUTO_INCREMENT,
  `pedido_fech` datetime(6) DEFAULT NULL,
  `pedido_nro` varchar(100) NOT NULL,
  `pedido_est` varchar(100) NOT NULL,
  `mesa_id` int(11) NOT NULL,
  `usu_id` int(11) NOT NULL,
  PRIMARY KEY (`pedido_id`),
  KEY `tbl_pedido_mesa_id_111d7a6b_fk_tbl_mesa_mesa_id` (`mesa_id`),
  KEY `tbl_pedido_usu_id_d14c6130_fk_auth_user_id` (`usu_id`),
  CONSTRAINT `tbl_pedido_mesa_id_111d7a6b_fk_tbl_mesa_mesa_id` FOREIGN KEY (`mesa_id`) REFERENCES `tbl_mesa` (`mesa_id`),
  CONSTRAINT `tbl_pedido_usu_id_d14c6130_fk_auth_user_id` FOREIGN KEY (`usu_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_pedido`
--

LOCK TABLES `tbl_pedido` WRITE;
/*!40000 ALTER TABLE `tbl_pedido` DISABLE KEYS */;
INSERT INTO `tbl_pedido` VALUES (1,NULL,'P001','solicitado',1,1),(2,'2023-04-04 08:28:04.000000','5c242048-2e9d-4482-8740-ed28f7e88a0c','solicitado',1,1),(3,'2023-04-04 08:29:36.000000','3eca9fb6-1743-4d21-8954-9806bb7a7976','solicitado',3,1),(4,'2023-04-04 08:31:15.000000','2eb7e728-ab5a-48a0-b83e-14ef73121ce1','solicitado',5,1);
/*!40000 ALTER TABLE `tbl_pedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_plato`
--

DROP TABLE IF EXISTS `tbl_plato`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_plato` (
  `plato_id` int(11) NOT NULL AUTO_INCREMENT,
  `plato_nom` varchar(200) NOT NULL,
  `plato_img` varchar(255) NOT NULL,
  `plato_pre` decimal(10,2) NOT NULL,
  `categoria_id` int(11) NOT NULL,
  PRIMARY KEY (`plato_id`),
  KEY `tbl_plato_categoria_id_cc821925_fk_tbl_categoria_categoria_id` (`categoria_id`),
  CONSTRAINT `tbl_plato_categoria_id_cc821925_fk_tbl_categoria_categoria_id` FOREIGN KEY (`categoria_id`) REFERENCES `tbl_categoria` (`categoria_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_plato`
--

LOCK TABLES `tbl_plato` WRITE;
/*!40000 ALTER TABLE `tbl_plato` DISABLE KEYS */;
INSERT INTO `tbl_plato` VALUES (1,'TEQUEÑOS','image/upload/v1680576581/kdtce78kl51tce4ddvhz.jpg',15.00,1),(2,'CEVICHOP','image/upload/v1680576623/xd255hsqqgx8uqgmcpfw.jpg',20.00,1),(3,'CAUSA','image/upload/v1680576638/gflt8p9iounn3qaozuho.jpg',25.00,1),(4,'LOMO SALTADO','image/upload/v1680576651/fy5hrqnlwpwvespdhpii.jpg',30.00,2),(5,'ARROZ CON PATO','image/upload/v1680576667/qf5agxutqs9tvfhkcszr.jpg',40.00,2),(6,'TACU TACU','image/upload/v1680576683/zhe7db0ddahavnvhol29.jpg',35.00,2),(7,'CUSQUEÑA TRIGO','image/upload/v1680576700/pwg1jequjwemxknhfrro.jpg',10.00,3),(8,'INKA KOLA','image/upload/v1680576714/pb9s33w6s1dbc3idetsc.webp',9.00,3),(9,'PISCO SOUR','image/upload/v1680576726/drfqcv0wv3rh7bzoj8qx.jpg',15.00,3);
/*!40000 ALTER TABLE `tbl_plato` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_mesa`
--

DROP TABLE IF EXISTS `tbl_mesa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_mesa` (
  `mesa_id` int(11) NOT NULL AUTO_INCREMENT,
  `mesa_nro` varchar(10) NOT NULL,
  `mesa_cap` int(11) NOT NULL,
  PRIMARY KEY (`mesa_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_mesa`
--

LOCK TABLES `tbl_mesa` WRITE;
/*!40000 ALTER TABLE `tbl_mesa` DISABLE KEYS */;
INSERT INTO `tbl_mesa` VALUES (1,'1',10),(2,'2',10),(3,'3',10),(4,'4',10),(5,'5',10),(6,'6',5),(7,'7',15);
/*!40000 ALTER TABLE `tbl_mesa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_pedido_plato`
--

DROP TABLE IF EXISTS `tbl_pedido_plato`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_pedido_plato` (
  `pedidoplato_id` int(11) NOT NULL AUTO_INCREMENT,
  `pedidoplato_cant` int(11) NOT NULL,
  `pedido_id` int(11) NOT NULL,
  `plato_id` int(11) NOT NULL,
  PRIMARY KEY (`pedidoplato_id`),
  KEY `tbl_pedido_plato_pedido_id_03e70b3a_fk_tbl_pedido_pedido_id` (`pedido_id`),
  KEY `tbl_pedido_plato_plato_id_245e2de6_fk_tbl_plato_plato_id` (`plato_id`),
  CONSTRAINT `tbl_pedido_plato_pedido_id_03e70b3a_fk_tbl_pedido_pedido_id` FOREIGN KEY (`pedido_id`) REFERENCES `tbl_pedido` (`pedido_id`),
  CONSTRAINT `tbl_pedido_plato_plato_id_245e2de6_fk_tbl_plato_plato_id` FOREIGN KEY (`plato_id`) REFERENCES `tbl_plato` (`plato_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_pedido_plato`
--

LOCK TABLES `tbl_pedido_plato` WRITE;
/*!40000 ALTER TABLE `tbl_pedido_plato` DISABLE KEYS */;
INSERT INTO `tbl_pedido_plato` VALUES (1,1,1,1),(2,1,2,1),(3,1,2,2),(4,1,2,4),(5,1,2,8),(6,1,3,3),(7,1,3,6),(8,1,3,7),(9,1,4,2),(10,1,4,4),(11,1,4,9);
/*!40000 ALTER TABLE `tbl_pedido_plato` ENABLE KEYS */;
UNLOCK TABLES;
