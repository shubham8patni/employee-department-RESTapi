-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 23, 2022 at 11:58 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pythonsql`
--

-- --------------------------------------------------------

--
-- Table structure for table `employees`
--

CREATE TABLE `employees` (
  `emp_id` varchar(6) DEFAULT NULL,
  `emp_name` varchar(8) DEFAULT NULL,
  `job_name` varchar(9) DEFAULT NULL,
  `manager_id` varchar(10) DEFAULT NULL,
  `hire_date` varchar(10) DEFAULT NULL,
  `salary` varchar(6) DEFAULT NULL,
  `commission` varchar(10) DEFAULT NULL,
  `dep_id` varchar(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `employees`
--

INSERT INTO `employees` (`emp_id`, `emp_name`, `job_name`, `manager_id`, `hire_date`, `salary`, `commission`, `dep_id`) VALUES
('68319', 'KAYLING', 'PRESIDENT', '', '18-11-1991', '6000', '', '1001'),
('66928', 'BLAZE', 'MANAGER', '68319', '01-05-1991', '2750', '', '3001'),
('67832', 'CLARE', 'MANAGER', '68319', '09-06-1991', '2550', '', '1001'),
('65646', 'JONAS', 'MANAGER', '68319', '02-04-1991', '2957', '', '2001'),
('64989', 'ADELYN', 'SALESMAN', '66928', '20-02-1991', '1700', '400', '3001'),
('65271', 'WADE', 'SALESMAN', '66928', '22-02-1991', '1350', '600', '3001'),
('66564', 'MADDEN', 'SALESMAN', '66928', '28-09-1991', '1350', '1500', '3001'),
('68454', 'TUCKER', 'SALESMAN', '66928', '08-09-1991', '1600', '0', '3001'),
('68736', 'ADNRES', 'CLERK', '67858', '23-05-1997', '1200', '', '2001'),
('69000', 'JULIUS', 'CLERK', '66928', '03-12-1991', '1050', '', '3001'),
('69324', 'MARKER', 'CLERK', '67832', '23-01-1992', '1400', '', '1001'),
('67858', 'SCARLET', 'ANALYST', '65646', '19-04-1997', '3100', '', '2001'),
('69062', 'FRANK', 'ANALYST', '65646', '03-12-1991', '3100', '', '2001'),
('63679', 'SANDRINE', 'CLERK', '69062', '18-12-1990', '900', '', '2001');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
