-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 16, 2026 at 04:30 AM
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
-- Table structure for table `tb_presensi`
--

CREATE TABLE `tb_presensi` (
  `id_user` text NOT NULL,
  `hari_kedatangan` text NOT NULL,
  `tanggal_kedatangan` text NOT NULL,
  `waktu_kedatangan` text NOT NULL,
  `image` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_presensi`
--

INSERT INTO `tb_presensi` (`id_user`, `hari_kedatangan`, `tanggal_kedatangan`, `waktu_kedatangan`, `image`) VALUES
('23090620043', 'Tuesday', '2024-11-26', '06:27:41', 'file_20241126062741.png'),
('23090620065', 'Tuesday', '2024-11-26', '06:34:43', 'file_20241126063443.png'),
('23090620043', 'Tuesday', '2024-11-26', '06:47:50', 'file_20241126064750.png'),
('23090620043', 'Tuesday', '2024-11-26', '06:47:59', 'file_20241126064759.png'),
('23090620043', 'Tuesday', '2024-11-26', '06:48:19', 'file_20241126064819.png'),
('23090620043', 'Tuesday', '2024-11-26', '06:50:00', 'file_20241126065000.png'),
('23090620065', 'Tuesday', '2024-11-26', '06:50:09', 'file_20241126065009.png'),
('23090620043', 'Tuesday', '2024-11-26', '06:53:25', 'file_20241126065325.png'),
('23090620043', 'Tuesday', '2024-11-26', '06:56:34', 'file_20241126065634.png'),
('23090620043', 'Tuesday', '2024-11-26', '06:57:29', 'file_20241126065729.png'),
('23090620043', 'Tuesday', '2024-11-26', '06:58:30', 'file_20241126065830.png'),
('23090620043', 'Tuesday', '2024-11-26', '06:59:09', 'file_20241126065909.png'),
('23090620043', 'Tuesday', '2024-11-26', '06:59:46', 'file_20241126065946.png'),
('23090620065', 'Tuesday', '2024-11-26', '08:08:42', 'file_20241126080842.png'),
('23090620065', 'Tuesday', '2024-11-26', '08:32:46', 'file_20241126083246.png'),
('23090620065', 'Tuesday', '2024-11-26', '08:32:51', 'file_20241126083251.png'),
('23090620065', 'Tuesday', '2024-11-26', '08:33:19', 'file_20241126083319.png'),
('23090620078', 'Tuesday', '2024-11-26', '08:34:58', 'file_20241126083458.png'),
('23090620078', 'Tuesday', '2024-11-26', '08:34:58', 'file_20241126083458.png'),
('23090620043', 'Tuesday', '2024-11-26', '08:48:38', 'file_20241126084838.png'),
('23090620043', 'Tuesday', '2024-11-26', '08:52:14', 'file_20241126085214.png'),
('23090620043', 'Tuesday', '2024-11-26', '08:57:40', 'file_20241126085740.png'),
('23090620065', 'Tuesday', '2024-11-26', '09:05:16', 'file_20241126090516.png'),
('23090620043', 'Saturday', '2024-12-14', '14:30:27', 'file_20241214143027.png'),
('23090620043', 'Saturday', '2024-12-14', '14:30:56', 'file_20241214143056.png'),
('23090620043', 'Saturday', '2024-12-14', '14:38:29', 'file_20241214143829.png'),
('23090620043', 'Saturday', '2024-12-14', '14:51:23', 'file_20241214145123.png'),
('23090620043', 'Saturday', '2024-12-14', '15:15:54', 'file_20241214151554.png'),
('23090620065', 'Saturday', '2024-12-14', '15:21:46', 'file_20241214152146.png'),
('23090620065', 'Saturday', '2024-12-14', '15:21:58', 'file_20241214152158.png'),
('23090620043', 'Saturday', '2024-12-14', '15:54:06', 'file_20241214155406.png'),
('23090620043', 'Saturday', '2024-12-14', '16:02:19', 'file_20241214160219.png'),
('23090620043', 'Saturday', '2024-12-14', '16:24:37', 'file_20241214162437.png'),
('23090620043', 'Saturday', '2024-12-14', '16:25:02', 'file_20241214162502.png'),
('23090620043', 'Saturday', '2024-12-14', '16:36:43', 'file_20241214163643.png'),
('23090620065', 'Saturday', '2024-12-14', '16:37:09', 'file_20241214163709.png'),
('23090620043', 'Saturday', '2024-12-14', '17:04:31', 'file_20241214170431.png'),
('23090620043', 'Saturday', '2024-12-14', '17:04:40', 'file_20241214170440.png'),
('23090620043', 'Saturday', '2024-12-14', '17:04:44', 'file_20241214170444.png'),
('23090620043', 'Saturday', '2024-12-14', '17:04:47', 'file_20241214170447.png'),
('23090620043', 'Saturday', '2024-12-14', '17:04:52', 'file_20241214170452.png'),
('23090620043', 'Saturday', '2024-12-14', '17:15:27', 'file_20241214171527.png'),
('23090620043', 'Saturday', '2024-12-14', '17:23:33', 'file_20241214172333.png'),
('23090620078', 'Saturday', '2024-12-14', '17:34:23', 'file_20241214173423.png'),
('23090620078', 'Saturday', '2024-12-14', '17:34:34', 'file_20241214173434.png'),
('23090620065', 'Saturday', '2024-12-14', '17:44:14', 'file_20241214174414.png'),
('23090620065', 'Saturday', '2024-12-14', '17:44:24', 'file_20241214174424.png');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
