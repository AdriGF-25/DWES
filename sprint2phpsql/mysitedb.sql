/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-11.8.3-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: mysitedb
-- ------------------------------------------------------
-- Server version	11.8.3-MariaDB-0+deb13u1 from Debian

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Table structure for table `comentarios`
--

DROP TABLE IF EXISTS `comentarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `comentarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comentario` varchar(2000) DEFAULT NULL,
  `libro_id` int(11) NOT NULL,
  `usuario_id` int(11) DEFAULT NULL,
  `fecha` timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `libro_id` (`libro_id`),
  CONSTRAINT `comentarios_ibfk_1` FOREIGN KEY (`libro_id`) REFERENCES `libros` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comentarios`
--

LOCK TABLES `comentarios` WRITE;
/*!40000 ALTER TABLE `comentarios` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `comentarios` VALUES
(1,'una lectura fascinante sobre estrategia y liderazgo.',1,NULL,'2025-10-28 11:02:53'),
(2,'un homenaje a la cultura pop y los años 80.',2,NULL,'2025-10-28 11:02:53'),
(3,'una historia envolvente en la barcelona gótica.',3,NULL,'2025-10-28 11:02:53'),
(4,'pionero del cyberpunk con una visión futurista.',4,NULL,'2025-10-28 11:02:53'),
(5,'una reflexión profunda sobre la historia de la humanidad.',5,NULL,'2025-10-28 11:02:53'),
(6,'asd',1,NULL,'2025-10-28 11:02:53'),
(7,'dsfgadsfvfd',1,NULL,'2025-10-28 11:02:53'),
(8,'prueba 911',1,NULL,'2025-10-28 11:02:53'),
(9,'asdf',1,NULL,'2025-10-28 11:02:53'),
(10,'comentario prueba',2,NULL,'2025-10-28 11:02:53'),
(11,'polno ¿? pofi',1,NULL,'2025-10-28 11:02:53'),
(12,'por fin va',1,NULL,'2025-10-28 11:02:53'),
(13,'polno yes ',2,NULL,'2025-10-28 11:08:43');
/*!40000 ALTER TABLE `comentarios` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `juegos`
--

DROP TABLE IF EXISTS `juegos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `juegos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `url_imagen` varchar(200) DEFAULT NULL,
  `plataforma` varchar(50) DEFAULT NULL,
  `fecha_lanzamiento` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `juegos`
--

LOCK TABLES `juegos` WRITE;
/*!40000 ALTER TABLE `juegos` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `juegos` VALUES
(1,'dredge','https://image.api.playstation.com/vulcan/ap/rnd/202302/0216/519d1449f3f87943aa0789b9a9e133b4d517c993f8e0b226.jpg','pc, consolas','2023-03-23'),
(2,'horizon forbidden west','https://www.xtrafondos.com/wallpapers/vertical/horizon-ii-forbidden-west-9737.jpg','playstation 4, playstation 5','2022-02-18'),
(3,'dragon ball sparking zero','https://image.api.playstation.com/vulcan/ap/rnd/202405/2216/6dbecd42a82245c34688d6ac2d16bf403c7c8b9249183232.png','PlayStation 5','2023-11-13'),
(4,'minecraft','https://upload.wikimedia.org/wikipedia/commons/f/fb/Minecraft-creeper-face.jpg','multi-plataforma','2011-11-18'),
(5,'ghost of tsushima','https://mir-s3-cdn-cf.behance.net/project_modules/hd_webp/29a8e4102363089.5f35f6dc29e5f.png','playstation 4','2020-07-17');
/*!40000 ALTER TABLE `juegos` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `libros`
--

DROP TABLE IF EXISTS `libros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `libros` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `url_imagen` varchar(200) DEFAULT NULL,
  `autor` varchar(100) DEFAULT NULL,
  `año_publicacion` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libros`
--

LOCK TABLES `libros` WRITE;
/*!40000 ALTER TABLE `libros` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `libros` VALUES
(1,'el juego de ender','https://images.cdn3.buscalibre.com/fit-in/360x360/b0/59/b059dceef929daf43f42be5d29ec5443.jpg','orson scott card',1985),
(2,'ready player one','https://m.media-amazon.com/images/I/714qeTmyeyL._AC_UF1000,1000_QL80_.jpg','ernest cline',2011),
(3,'la sombra del viento','https://m.media-amazon.com/images/I/61ZSuWFzQRL.jpg','carlos ruiz zafón',2001),
(4,'neuromante','https://www.ccyberdark.net/wp-content/uploads/2021/05/Neuromancer.jpeg','william gibson',1984),
(5,'sapiens','https://m.media-amazon.com/images/I/811PTyrckTL.jpg','yuval noah harari',2011);
/*!40000 ALTER TABLE `libros` ENABLE KEYS */;
UNLOCK TABLES;
commit;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2025-10-28 12:10:45
