-- MySQL dump 10.16  Distrib 10.1.32-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: 21cnjy
-- ------------------------------------------------------
-- Server version	10.1.32-MariaDB

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
-- Table structure for table `document3`
--

DROP TABLE IF EXISTS `document3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `document3` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `document_classify` int(1) NOT NULL COMMENT '资源的分类：1，同步资源；2，专区资源。如果一个资源属于多个分类，则用逗号分割存储。',
  `subject_id` int(11) DEFAULT NULL COMMENT '备课学科id',
  `teachingmaterial_id` int(11) DEFAULT NULL COMMENT '备课教材id',
  `grade_id` int(11) DEFAULT NULL COMMENT '备课年级id',
  `chapter_id` int(11) DEFAULT NULL COMMENT '备课章节id',
  `document_name` varchar(225) COLLATE utf8mb4_bin NOT NULL,
  `document_explain` text COLLATE utf8mb4_bin,
  `url` varchar(500) COLLATE utf8mb4_bin NOT NULL COMMENT '文档下载地址',
  `file_type` varchar(20) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '文档的类型(.ppt/.word)',
  `used_count` int(11) DEFAULT NULL COMMENT '使用次数',
  `prepare_lesson_type` int(11) NOT NULL COMMENT '备课资源类型，对应字典表',
  `prepare_lesson_importance` int(11) NOT NULL COMMENT '备课资源的重要性，精品/普通，对应字典表',
  `prepare_lesson_area` int(11) NOT NULL COMMENT '备课资源所属地区，对应字典表',
  `prepare_lesson_level` int(11) NOT NULL COMMENT '备课资源星级，对应字典表',
  `teacher_id` int(11) DEFAULT NULL COMMENT '上传文档老师id',
  `document_source` int(1) DEFAULT '1' COMMENT '文档来源，1：系统和教师，2：21教育网',
  `show_sort` int(1) DEFAULT NULL COMMENT '资源的显示排序，从1开始，1表示最先显示',
  `show_time` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '此文档上传的时间，yyyy-MM-dd',
  `document_id` int(11) NOT NULL COMMENT '21网站的文档id',
  `username` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `document3`
--

LOCK TABLES `document3` WRITE;
/*!40000 ALTER TABLE `document3` DISABLE KEYS */;
/*!40000 ALTER TABLE `document3` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-21 20:29:21
