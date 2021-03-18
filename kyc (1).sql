-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 18, 2021 at 06:32 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kyc`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact_information`
--

CREATE TABLE `contact_information` (
  `NIC` varchar(20) NOT NULL,
  `House No` varchar(10) NOT NULL,
  `Street` varchar(25) NOT NULL,
  `City` varchar(50) NOT NULL,
  `Postal Code` int(10) NOT NULL,
  `Country` varchar(50) NOT NULL,
  `Phone No..` tinyint(20) NOT NULL,
  `Mobile No.` varchar(20) NOT NULL,
  `E-mail` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `employment_information`
--

CREATE TABLE `employment_information` (
  `NIC` varchar(15) NOT NULL,
  `Employment Status` varchar(15) NOT NULL,
  `Occupation` varchar(25) NOT NULL,
  `Job Title` varchar(25) NOT NULL,
  `Industry` varchar(25) NOT NULL,
  `Length of Services` int(5) NOT NULL,
  `Source of Income` text NOT NULL,
  `Average Income` text NOT NULL,
  `Transaction Mode` varchar(15) NOT NULL,
  `Operating Authority` varchar(15) NOT NULL,
  `Banking Products` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `identity_information`
--

CREATE TABLE `identity_information` (
  `Serial No` int(50) NOT NULL,
  `Identification Code` text NOT NULL,
  `Name with Initials` varchar(50) NOT NULL,
  `Name in Full` text NOT NULL,
  `Identity Recognition` varchar(15) NOT NULL,
  `Expiration Date` date NOT NULL,
  `Nationality` varchar(25) NOT NULL,
  `DOB` date NOT NULL,
  `Face Recognition` text NOT NULL,
  `Finger Print 01` varchar(10) NOT NULL,
  `Finger Print 02` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `office_use`
--

CREATE TABLE `office_use` (
  `NIC` varchar(20) NOT NULL,
  `Date (form fill)` date NOT NULL,
  `Account No.` varchar(50) NOT NULL,
  `Branch No.` varchar(20) NOT NULL,
  `Officer's S/No.` varchar(25) NOT NULL,
  `Manager's INTL` varchar(25) NOT NULL,
  `Risk Category` varchar(20) NOT NULL,
  `Name of the Officer` varchar(100) NOT NULL,
  `Signature of the Officer` text NOT NULL,
  `Date (sign by the officer)` date NOT NULL,
  `Name of the Manager` varchar(100) NOT NULL,
  `Signature of the Manager` varchar(50) NOT NULL,
  `Date (sign by the Manager)` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact_information`
--
ALTER TABLE `contact_information`
  ADD PRIMARY KEY (`NIC`);

--
-- Indexes for table `employment_information`
--
ALTER TABLE `employment_information`
  ADD PRIMARY KEY (`NIC`);

--
-- Indexes for table `identity_information`
--
ALTER TABLE `identity_information`
  ADD PRIMARY KEY (`Serial No`);

--
-- Indexes for table `office_use`
--
ALTER TABLE `office_use`
  ADD PRIMARY KEY (`NIC`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `identity_information`
--
ALTER TABLE `identity_information`
  MODIFY `Serial No` int(50) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
