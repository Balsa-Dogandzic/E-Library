-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 16, 2023 at 08:23 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `biblioteka`
--

-- --------------------------------------------------------

--
-- Table structure for table `autor`
--

CREATE TABLE `autor` (
  `id` int(11) NOT NULL,
  `autor` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `autor`
--

INSERT INTO `autor` (`id`, `autor`) VALUES
(1, 'Steven King'),
(2, 'Ivo Andric'),
(3, 'Mesa Selimovic'),
(4, 'Vasko Popa'),
(5, 'J. K. Rowling'),
(6, 'Lav Tolstoj'),
(7, 'Vilijam Sekspir'),
(8, 'Dzordz Orvel');

-- --------------------------------------------------------

--
-- Table structure for table `knjiga`
--

CREATE TABLE `knjiga` (
  `id` int(11) NOT NULL,
  `naslov` varchar(255) NOT NULL,
  `zanr` varchar(255) NOT NULL,
  `autor_id` int(11) NOT NULL,
  `povez` enum('Tvrdi povez','Meki povez','','') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `knjiga`
--

INSERT INTO `knjiga` (`id`, `naslov`, `zanr`, `autor_id`, `povez`) VALUES
(1, 'IT', 'Horror', 1, 'Tvrdi povez'),
(2, 'Shining', 'Horror', 1, 'Tvrdi povez'),
(4, 'Na Drini cuprija', 'Roman', 2, 'Tvrdi povez'),
(5, 'Dervis i smrt', 'Roman', 3, 'Meki povez'),
(8, 'Prokleta avlija', 'Roman', 2, 'Meki povez'),
(9, 'Tvrdjava', 'Roman', 3, 'Tvrdi povez'),
(10, 'Zivotinjska farma', 'Roman', 8, 'Meki povez'),
(11, 'Ana Karenjina', 'Roman', 6, 'Tvrdi povez'),
(12, 'Hari Poter i kamen mudrosti', 'Fantazija', 5, 'Tvrdi povez');

-- --------------------------------------------------------

--
-- Table structure for table `korisnik`
--

CREATE TABLE `korisnik` (
  `id` int(11) NOT NULL,
  `korisnicko_ime` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `lozinka` varchar(255) NOT NULL,
  `ime` varchar(255) NOT NULL,
  `prezime` varchar(255) NOT NULL,
  `tip_korisnika` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `korisnik`
--

INSERT INTO `korisnik` (`id`, `korisnicko_ime`, `email`, `lozinka`, `ime`, `prezime`, `tip_korisnika`) VALUES
(2, 'admin', 'admin@gmail.com', 'admin123', 'Admin', 'Adminovic', 2),
(3, 'Marko', 'marko@gmail.com', 'marko123', 'Marko', 'Markovic', 1),
(5, 'ana', 'ana123@gmail.com', 'ana123', 'Ana', 'Aleksic', 1),
(6, 'pera', 'peric@gmail.com', 'pera123', 'Pera', 'Peric', 1);

-- --------------------------------------------------------

--
-- Table structure for table `rezervacije`
--

CREATE TABLE `rezervacije` (
  `id` int(11) NOT NULL,
  `knjiga_id` int(11) NOT NULL,
  `korisnik_id` int(11) NOT NULL,
  `datum_preuzimanja` date NOT NULL,
  `datum_vracanja` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rezervacije`
--

INSERT INTO `rezervacije` (`id`, `knjiga_id`, `korisnik_id`, `datum_preuzimanja`, `datum_vracanja`) VALUES
(1, 1, 3, '2023-06-01', '2023-06-30'),
(3, 5, 2, '2023-06-01', '2023-06-30'),
(9, 8, 2, '2023-06-16', '2023-07-16'),
(10, 9, 5, '2023-06-06', '2023-07-16'),
(11, 11, 5, '2023-06-13', '2023-07-13'),
(12, 12, 5, '2023-06-10', '2023-07-10'),
(13, 10, 6, '2023-06-07', '2023-08-07');

-- --------------------------------------------------------

--
-- Table structure for table `tipovi_korisnika`
--

CREATE TABLE `tipovi_korisnika` (
  `id` int(11) NOT NULL,
  `tip` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tipovi_korisnika`
--

INSERT INTO `tipovi_korisnika` (`id`, `tip`) VALUES
(1, 'korisnik'),
(2, 'admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `autor`
--
ALTER TABLE `autor`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `knjiga`
--
ALTER TABLE `knjiga`
  ADD PRIMARY KEY (`id`),
  ADD KEY `autor_id` (`autor_id`);

--
-- Indexes for table `korisnik`
--
ALTER TABLE `korisnik`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`korisnicko_ime`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `tip_korisnika` (`tip_korisnika`);

--
-- Indexes for table `rezervacije`
--
ALTER TABLE `rezervacije`
  ADD PRIMARY KEY (`id`),
  ADD KEY `knjiga_id` (`knjiga_id`),
  ADD KEY `korisnik_id` (`korisnik_id`);

--
-- Indexes for table `tipovi_korisnika`
--
ALTER TABLE `tipovi_korisnika`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `autor`
--
ALTER TABLE `autor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `knjiga`
--
ALTER TABLE `knjiga`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `korisnik`
--
ALTER TABLE `korisnik`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `rezervacije`
--
ALTER TABLE `rezervacije`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `tipovi_korisnika`
--
ALTER TABLE `tipovi_korisnika`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `knjiga`
--
ALTER TABLE `knjiga`
  ADD CONSTRAINT `knjiga_ibfk_1` FOREIGN KEY (`autor_id`) REFERENCES `autor` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `korisnik`
--
ALTER TABLE `korisnik`
  ADD CONSTRAINT `korisnik_ibfk_1` FOREIGN KEY (`tip_korisnika`) REFERENCES `tipovi_korisnika` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `rezervacije`
--
ALTER TABLE `rezervacije`
  ADD CONSTRAINT `rezervacije_ibfk_1` FOREIGN KEY (`korisnik_id`) REFERENCES `korisnik` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `rezervacije_ibfk_2` FOREIGN KEY (`knjiga_id`) REFERENCES `knjiga` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
