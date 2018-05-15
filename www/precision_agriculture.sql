-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 23, 2018 at 08:53 AM
-- Server version: 5.7.14
-- PHP Version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `precision_agriculture`
--

-- --------------------------------------------------------

--
-- Table structure for table `data`
--

CREATE TABLE `data` (
  `Sub_Id` varchar(10) CHARACTER SET utf8 NOT NULL,
  `Sensor_Id` varchar(10) CHARACTER SET utf8 NOT NULL,
  `Date` datetime NOT NULL,
  `Value` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `farms`
--

CREATE TABLE `farms` (
  `RegionName` varchar(100) NOT NULL,
  `Description` varchar(100) NOT NULL,
  `NorhtWestLat` varchar(100) NOT NULL,
  `NorhtWestLong` varchar(100) NOT NULL,
  `SouthEastLat` varchar(100) NOT NULL,
  `SouthEastLong` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `farms`
--

INSERT INTO `farms` (`RegionName`, `Description`, `NorhtWestLat`, `NorhtWestLong`, `SouthEastLat`, `SouthEastLong`) VALUES
('budapest', 'wine', '47.520138515251546', '19.32419043416462', '47.47977997138057', '19.441606816000558'),
('Budapest1', 'oil', '37.5591611710287', '22.180012359619127', '37.54432695824025', '22.22035278320311');

-- --------------------------------------------------------

--
-- Table structure for table `markers`
--

CREATE TABLE `markers` (
  `RegionName` varchar(100) NOT NULL,
  `Sub_Name` varchar(100) NOT NULL,
  `markerLatitude` varchar(100) NOT NULL,
  `markerLongtitude` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `sensors`
--

CREATE TABLE `sensors` (
  `Sensor_Id` varchar(10) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Min` int(10) NOT NULL,
  `Max` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `sensors`
--

INSERT INTO `sensors` (`Sensor_Id`, `Name`, `Min`, `Max`) VALUES
('Soil_Hum', 'Soil Humidity', 0, 1023),
('Soil_Temp', 'Soil Temperature', -5, 40);

-- --------------------------------------------------------

--
-- Table structure for table `subwithsensors`
--

CREATE TABLE `subwithsensors` (
  `Sub_Id` varchar(10) NOT NULL,
  `Sensor_Id` varchar(10) NOT NULL,
  `Port` varchar(10) CHARACTER SET utf8mb4 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `sub_node`
--

CREATE TABLE `sub_node` (
  `Sub_Name` varchar(100) NOT NULL,
  `Sub_Id` varchar(10) NOT NULL,
  `Protocol` varchar(10) NOT NULL,
  `IP` varchar(15) DEFAULT NULL,
  `MAC` varchar(10) DEFAULT NULL,
  `Status` tinyint(1) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `Name` varchar(15) NOT NULL,
  `LastName` varchar(20) NOT NULL,
  `Password` varchar(15) NOT NULL,
  `Email` varchar(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`Name`, `LastName`, `Password`, `Email`) VALUES
('chris', 'chris', 'cdelis1994', 'deli@ceid.upatras.gr'),
('dimitris', 'dimitriou', 'cdelis1994', 'deliww@gmail.com'),
('deli', 'deli', 'cdelis1994', 'deli2957@gmail.com'),
('chris', 'd', 'cdelis1994', 'de@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `data`
--
ALTER TABLE `data`
  ADD KEY `Id_Sub` (`Sub_Id`),
  ADD KEY `Id_Sensor` (`Sensor_Id`),
  ADD KEY `Value` (`Value`);

--
-- Indexes for table `farms`
--
ALTER TABLE `farms`
  ADD PRIMARY KEY (`RegionName`);

--
-- Indexes for table `markers`
--
ALTER TABLE `markers`
  ADD PRIMARY KEY (`RegionName`,`Sub_Name`);

--
-- Indexes for table `sensors`
--
ALTER TABLE `sensors`
  ADD PRIMARY KEY (`Sensor_Id`),
  ADD KEY `Id_Sensor` (`Sensor_Id`);

--
-- Indexes for table `subwithsensors`
--
ALTER TABLE `subwithsensors`
  ADD PRIMARY KEY (`Sub_Id`,`Sensor_Id`),
  ADD UNIQUE KEY `sub_id` (`Sub_Id`,`Port`),
  ADD KEY `sub_id_2` (`Sub_Id`),
  ADD KEY `sens_id` (`Sensor_Id`);

--
-- Indexes for table `sub_node`
--
ALTER TABLE `sub_node`
  ADD PRIMARY KEY (`Sub_Id`),
  ADD UNIQUE KEY `Sub_Name` (`Sub_Name`),
  ADD UNIQUE KEY `MAC` (`MAC`),
  ADD UNIQUE KEY `IP` (`IP`),
  ADD KEY `Id_Sub` (`Sub_Id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`Name`,`LastName`),
  ADD UNIQUE KEY `Email` (`Email`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `data`
--
ALTER TABLE `data`
  ADD CONSTRAINT `data_ibfk_1` FOREIGN KEY (`Sub_Id`) REFERENCES `sub_node` (`Sub_Id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `data_ibfk_2` FOREIGN KEY (`Sensor_Id`) REFERENCES `sensors` (`Sensor_Id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `markers`
--
ALTER TABLE `markers`
  ADD CONSTRAINT `markers_ibfk_1` FOREIGN KEY (`RegionName`) REFERENCES `farms` (`RegionName`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `subwithsensors`
--
ALTER TABLE `subwithsensors`
  ADD CONSTRAINT `subwithsensors_ibfk_1` FOREIGN KEY (`Sub_Id`) REFERENCES `sub_node` (`Sub_Id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `subwithsensors_ibfk_2` FOREIGN KEY (`Sensor_Id`) REFERENCES `sensors` (`Sensor_Id`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
