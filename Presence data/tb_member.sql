-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 16, 2026 at 04:28 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_presensi`
--

-- --------------------------------------------------------

--
-- Table structure for table `tb_member`
--

CREATE TABLE `tb_member` (
  `id_nim` text NOT NULL,
  `nama_mahasiswa` text NOT NULL,
  `Prodi` text NOT NULL,
  `Rombel` text NOT NULL,
  `Tanggal_Lahir` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_member`
--

INSERT INTO `tb_member` (`id_nim`, `nama_mahasiswa`, `Prodi`, `Rombel`, `Tanggal_Lahir`) VALUES
('23090620043', 'Muhammad Athaozih', 'Teknik Elektronika', 'V2', '2015-10-07 16:17:38'),
('23090620043', 'Muhammad Athaozih', 'Teknik Elektronika', 'V2', '2015-10-07 16:17:38'),
('23090620065', 'Ahmad Ilman Nadziron ', 'Teknik Elektronika', 'V2', '2015-12-10 16:18:40'),
('23090620065', 'Ahmad Ilman Nadziron ', 'Teknik Elektronika', 'V2', '2015-12-10 16:18:40'),
('23090620078', 'Zacky Allamsyah', 'Teknik Elektronika', 'V2', '2019-05-15 16:21:02'),
('23090620078', 'Zacky Allamsyah', 'Teknik Elektronika', 'V2', '2019-05-15 16:21:02'),
('23090620084', 'Anjani Nuria Arsyla', 'Teknik Elektronika', 'V2', '2018-12-17 16:22:14'),
('23090620084', 'Anjani Nuria Arsyla', 'Teknik Elektronika', 'V2', '2018-12-17 16:22:14');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
