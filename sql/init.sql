#
CREATE DATABASE IF NOT EXISTS `mysql` DEFAULT CHARACTER SET = utf8mb4;
Use `mysql`;

#
# Structure for table "tpoint"
#

DROP TABLE IF EXISTS `tpoint`;
CREATE TABLE `tpoint` (
  `row_id` int(10) NOT NULL AUTO_INCREMENT,
  `location_id` varchar(20) NOT NULL,
  `province_name` varchar(30) NOT NULL,
  `city_name` varchar(30) NOT NULL,
  `district_name` varchar(30) DEFAULT NULL,
  `town_name` varchar(30) DEFAULT NULL,
  `location_name` varchar(300) NOT NULL,
  `address` varchar(300) NOT NULL,
  `longitude` double(9,6) NOT NULL,
  `latitude` double(9,6) NOT NULL,
  PRIMARY KEY (`row_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

