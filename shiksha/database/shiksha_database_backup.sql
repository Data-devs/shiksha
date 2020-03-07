-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: localhost    Database: shiksha
-- ------------------------------------------------------
-- Server version	5.7.29-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `university_info`
--

DROP TABLE IF EXISTS `university_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `university_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(300) DEFAULT NULL,
  `link` varchar(400) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `university_info`
--

LOCK TABLES `university_info` WRITE;
/*!40000 ALTER TABLE `university_info` DISABLE KEYS */;
INSERT INTO `university_info` VALUES (32,'University of Alberta','https://studyabroad.shiksha.com/canada/universities/university-of-alberta'),(33,'The University of British Columbia','https://studyabroad.shiksha.com/canada/universities/university-of-british-columbia'),(34,'University of Toronto','https://studyabroad.shiksha.com/canada/universities/university-of-toronto'),(35,'Humber College','https://studyabroad.shiksha.com/canada/universities/humber-college'),(36,'McGill University','https://studyabroad.shiksha.com/canada/universities/mcgill-university'),(37,'Centennial College','https://studyabroad.shiksha.com/canada/universities/centennial-college'),(38,'University of Waterloo','https://studyabroad.shiksha.com/canada/universities/university-of-waterloo'),(39,'University of Windsor','https://studyabroad.shiksha.com/canada/universities/university-of-windsor'),(40,'University of Calgary','https://studyabroad.shiksha.com/canada/universities/university-of-calgary'),(41,'St. Clair College','https://studyabroad.shiksha.com/canada/universities/st-clair-college-of-applied-arts-technology'),(42,'University of Saskatchewan','https://studyabroad.shiksha.com/canada/universities/university-of-saskatchewan'),(43,'Fanshawe College','https://studyabroad.shiksha.com/canada/universities/fanshawe-college-of-applied-arts-and-technology'),(44,'Conestoga College','https://studyabroad.shiksha.com/canada/universities/conestoga-college'),(45,'York University','https://studyabroad.shiksha.com/canada/universities/york-university'),(46,'University of Ottawa','https://studyabroad.shiksha.com/canada/universities/university-of-ottawa'),(47,'Sheridan College ','https://studyabroad.shiksha.com/canada/universities/sheridan-college-institute-of-technology-advanced-learning'),(48,'Memorial University of Newfoundland','https://studyabroad.shiksha.com/canada/universities/memorial-university-of-newfoundland'),(49,'Concordia University','https://studyabroad.shiksha.com/canada/universities/concordia-university'),(50,'University of Regina','https://studyabroad.shiksha.com/canada/universities/university-of-regina'),(51,'Dalhousie University','https://studyabroad.shiksha.com/canada/universities/dalhousie-university'),(52,'heool',NULL);
/*!40000 ALTER TABLE `university_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `university_page_data`
--

DROP TABLE IF EXISTS `university_page_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `university_page_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `course_name` varchar(1000) DEFAULT NULL,
  `duration` varchar(1000) DEFAULT NULL,
  `level` varchar(1000) DEFAULT NULL,
  `course_description` varchar(1000) DEFAULT NULL,
  `qs` varchar(1000) DEFAULT NULL,
  `shanghai` varchar(1000) DEFAULT NULL,
  `times_higher` varchar(1000) DEFAULT NULL,
  `us_news` varchar(1000) DEFAULT NULL,
  `1st_year_tuition_fees` varchar(1000) DEFAULT NULL,
  `hostel_and_meals` varchar(1000) DEFAULT NULL,
  `non_instructional_fees` varchar(1000) DEFAULT NULL,
  `utilities` varchar(1000) DEFAULT NULL,
  `internet_and_mobile_phone` varchar(1000) DEFAULT NULL,
  `clothing` varchar(1000) DEFAULT NULL,
  `educational_supplies` varchar(1000) DEFAULT NULL,
  `recreation` varchar(1000) DEFAULT NULL,
  `total` varchar(1000) DEFAULT NULL,
  `class_12th` varchar(1000) DEFAULT NULL,
  `bachelors` varchar(1000) DEFAULT NULL,
  `exams` varchar(1000) DEFAULT NULL,
  `about_this_ course` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `university_page_data`
--

LOCK TABLES `university_page_data` WRITE;
/*!40000 ALTER TABLE `university_page_data` DISABLE KEYS */;
/*!40000 ALTER TABLE `university_page_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-08  2:03:36
