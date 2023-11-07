-- phpMyAdmin SQL Dump
-- version 5.1.4
-- https://www.phpmyadmin.net/
--
-- Host: mysql-ale.alwaysdata.net
-- Generation Time: Jul 23, 2023 at 10:50 PM
-- Server version: 10.6.13-MariaDB
-- PHP Version: 7.4.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ale_1`
--

-- --------------------------------------------------------

--
-- Table structure for table `admins`
--

CREATE TABLE `admins` (
  `id` int(11) NOT NULL,
  `user_id` bigint(20) UNSIGNED NOT NULL,
  `username` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admins`
--

INSERT INTO `admins` (`id`, `user_id`, `username`) VALUES
(1, 1924666696, 'Sarcehkr');
-- --------------------------------------------------------

--
-- ble structure for table `antispam`
--

CREATE TABLE `antispam` (
  `id` int(11) NOT NULL,
  `userid` varchar(50) NOT NULL,
  `last_checked_on` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `global_checker_stats`
--

CREATE TABLE `global_checker_stats` (
  `total_checked` varchar(100) NOT NULL,
  `total_ccn` varchar(100) NOT NULL,
  `total_cvv` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `global_checker_stats`
--

INSERT INTO `global_checker_stats` (`total_checked`, `total_ccn`, `total_cvv`) VALUES
('0', '0', '0');

-- --------------------------------------------------------

--
-- Table structure for table `groups`
--

CREATE TABLE `groups` (
  `id` varchar(50) DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  `fecha_vencimiento` date DEFAULT NULL,
  `status` varchar(20) NOT NULL DEFAULT 'free user'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `groups`
--

INSERT INTO `groups` (`id`, `name`, `fecha_vencimiento`, `status`) VALUES
('-1001736993290', 'AzunaCHKFree', '2023-07-14', 'premium'),
('-1001845103029', '', '2023-07-14', 'premium'),
('-1001795608283', 'BinsCEDex', '2023-07-25', 'premium'),
('-1001876504540', 'xexeee15', '2023-07-15', 'premium'),
('-1001757580332', 'anonymity_chat', '2023-07-16', 'premium');

-- --------------------------------------------------------

--
-- Table structure for table `keyuser`
--

CREATE TABLE `keyuser` (
  `id` varchar(255) NOT NULL,
  `clave` varchar(255) NOT NULL,
  `status` varchar(50) NOT NULL,
  `plan` varchar(50) NOT NULL,
  `planexpiry` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `keyuser`
--

INSERT INTO `keyuser` (`id`, `clave`, `status`, `plan`, `planexpiry`) VALUES
('', 'AzunaChkBot-z1wvV2OQW4Wu', 'ACTIVE', '30', '2023-07-27 13:42:41');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `user_id` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `status` varchar(255) NOT NULL,
  `expiration_date` date DEFAULT NULL,
  `creditos` int(11) NOT NULL DEFAULT 0,
  `warns` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `user_id`, `username`, `status`, `expiration_date`, `creditos`, `warns`) VALUES
(5, '1787128910', 'hackerismyname', 'free user', NULL, 0, NULL),
(6, '6060217058', 'harryszakf', 'free user', NULL, 0, NULL),
(7, '5777945924', 'TerrorVlP', 'free user', NULL, 0, NULL),
(8, '5330295177', 'JONYYMOPR0', 'free user', NULL, 0, NULL),
(9, '5544027604', 'Bryan_RG4', 'free user', NULL, 0, NULL),
(10, '5783018778', 'SynxCris', 'free user', NULL, 0, NULL),
(11, '5956861157', 'Josue_LDT', 'free user', NULL, 0, NULL),
(12, '6153034207', 'K1NG_OFFL1N3', 'free user', NULL, 0, NULL),
(13, '1124717677', 'VeigarAd', 'free user', NULL, 0, NULL),
(14, '5984693479', 'AxnlzxExp', 'free user', NULL, 0, NULL),
(15, '5455884750', 'Zenkaizq', 'free user', NULL, 0, NULL),
(16, '5694058445', 'Angel70k', 'premium', '2023-06-04', 10, 0),
(17, '1580254770', 'JPPROS3', 'free user', NULL, 0, NULL),
(18, '5397590940', 'juanbatzu', 'free user', NULL, 0, NULL),
(19, '5835996932', 'Nani_2811', 'premium', '2023-06-27', 0, NULL),
(20, '5552975574', 'mxguelidk', 'free user', NULL, 0, NULL),
(21, '5652055995', 'ntrxion', 'free user', NULL, 0, NULL),
(22, '1852985145', 'FERCABLLERO', 'free user', NULL, 0, NULL),
(23, '5060021759', 'AdonisGonzalez091618', 'free user', NULL, 0, NULL),
(24, '5203729864', 'yamorinight', 'free user', NULL, 0, NULL),
(25, '5123478457', 'Pelu420', 'free user', NULL, 0, NULL),
(26, '5509387090', 'LABINBADEL', 'free user', NULL, 0, NULL),
(27, '1739206386', 'AFN4NX', 'free user', NULL, 0, NULL),
(28, '5987397369', 'AzkeelOficial', 'free user', NULL, 0, NULL),
(29, '5090750610', 'DonMSI', 'premium', '2023-06-21', 20, 0),
(30, '5795024592', 'LOKITOA1', 'free user', NULL, 0, NULL),
(31, '5600021911', 'vZeenp', 'free user', NULL, 0, NULL),
(40, '5827678981', 'S4NT1RMX', 'Free User', NULL, 100, NULL),
(42, '1087968824', 'GroupAnonymousBot', 'Free User', NULL, 0, NULL),
(43, '5882192554', 'vipandres', 'Free User', NULL, 0, NULL),
(44, '6032721382', 'REDDIXX1', 'Free User', NULL, 0, NULL),
(45, '962912087', 'Thiare1965', 'Free User', NULL, 0, NULL),
(46, '6278310515', 'Kevin22012', 'Free User', NULL, 0, NULL),
(47, '1017417946', 'Uch4695', 'Free User', NULL, 0, NULL),
(48, '5114085968', 'mokka_capuchino', 'Free User', NULL, 0, NULL),
(49, '2010388048', 'Joseangel260612', 'Free User', NULL, 0, NULL),
(50, '1947540646', 'sagradS', 'Free User', NULL, 0, NULL),
(51, '1811449678', 'TheRenniel', 'Free User', NULL, 0, NULL),
(52, '5984596736', 'annymimichis', 'Free User', NULL, 0, NULL),
(53, '5190130978', 'patommx', 'Free User', NULL, 0, NULL),
(54, '1408466101', 'elmataperras0', 'Free User', NULL, 0, NULL),
(55, '1766274876', 'Srmadara1', 'Free User', NULL, 0, NULL),
(56, '6255366266', 'luemnezz', 'Free User', NULL, 0, NULL),
(57, '5446937342', 'UzumakiNaruton1', 'Free User', NULL, 0, NULL),
(58, '5575229765', 'rcsrenergy', 'Free User', NULL, 0, NULL),
(59, '1368236724', 'enrique_09sv', 'Free User', NULL, 0, NULL),
(60, '5106956473', 'anilvercruz', 'Free User', NULL, 0, NULL),
(61, '813980912', 'Enrique_S2', 'Free User', NULL, 0, NULL),
(63, '5818424966', 'alex20x2', 'premium', '2023-07-09', 0, 0),
(64, '1373453628', 'Londer45', 'Free User', NULL, 0, NULL),
(65, '6238759216', 'Eljixux', 'Free User', NULL, 0, 3),
(66, '6102879147', 'ByCraziestYT', 'Free User', NULL, 0, NULL),
(68, '6173403224', 'Gabo1015J', 'Free User', NULL, 0, NULL),
(69, '5963256646', 'sawling02', 'Free User', NULL, 0, NULL),
(70, '1106830117', 'IvanLautaxD', 'Free User', NULL, 0, NULL),
(71, '1500381272', 'httpsx16', 'Free User', NULL, 0, NULL),
(72, '6102645050', 'annyyyy9', 'Free User', NULL, 0, NULL),
(73, '6051815595', 'kqixxonigger', 'Free User', NULL, 0, NULL),
(74, '5225182250', 'Sxrxxxxx_binner', 'Free User', NULL, 0, NULL),
(75, '1864111245', 'Riasgremory00', 'Free User', NULL, 0, NULL),
(76, '6216101427', 'Brayan060', 'Free User', NULL, 0, NULL),
(78, '807928937', '', 'Free User', NULL, 0, NULL),
(79, '5408923336', 'Juliebosh1', 'premium', '2023-07-15', 10, 3),
(81, '5732745863', 'JEANN122', 'Free User', NULL, 0, NULL),
(82, '6196267028', 'DanielHernandez1l1', 'Free User', NULL, 0, NULL),
(84, '5017073559', 'Uriel_00', 'Free User', NULL, 0, NULL),
(85, '1984629373', 'PoisonsX', 'Free User', NULL, 0, NULL),
(86, '5305267913', 'erro_403', 'Free User', NULL, 0, 3),
(87, '2084488308', 'Sheltz01', 'Free User', NULL, 0, 1),
(88, '5202429424', 'a12374', 'Free User', NULL, 0, NULL),
(89, '1813620069', 'SPEEDY_GONZALEZ10', 'premium', '2023-07-15', 15, 0),
(90, '5592353777', 'B52OPB', 'Free User', NULL, 0, 1),
(91, '1708934665', 'BryanZR98', 'Free User', NULL, 0, 2),
(92, '5927745251', 'Victorxd14', 'Free User', NULL, 0, NULL),
(93, '6185696395', 'Luis220520', 'Free User', NULL, 0, 1),
(94, '2045212036', 'Julio_romero29', 'Free User', NULL, 0, NULL),
(95, '5025968388', 'stich00iceman00', 'Free User', NULL, 0, NULL),
(97, '5310678894', 'Kevinyryrt', 'Free User', NULL, 0, NULL),
(101, '5258227645', 'PainXenozZx', 'Free User', NULL, 0, NULL),
(102, '5032519946', 'Miguelo_0334', 'Free User', NULL, 0, NULL),
(103, '5660621998', 'natrann43', 'Free User', NULL, 0, NULL),
(104, '6154134499', 'Gu20242023', 'Free User', NULL, 0, NULL),
(105, '5343991569', 'lordasmodeo', 'premium', '2023-07-08', 40, 0),
(106, '5282484874', 'latin_vip', 'Free User', NULL, 0, NULL),
(107, '6054783627', 'Daddy12m', 'Free User', NULL, 0, NULL),
(108, '5635867152', 'Neitorrr', 'premium', '2023-07-08', 0, NULL),
(109, '5477569604', 'fuckingnyonxxx', 'premium', '2023-06-20', 35, 0),
(110, '1375549478', 'Mxstyk', 'Free User', NULL, 0, NULL),
(111, '5731246443', 'muertebl4nca', 'Free User', NULL, 0, NULL),
(112, '2077335030', '', 'Free User', NULL, 0, NULL),
(113, '5346773922', 'VasKizo', 'Free User', NULL, 0, NULL),
(114, '1189127583', 'miguelffh4x', 'Free User', NULL, 0, NULL),
(115, '5089052963', 'sebastian_GamerGG', 'Free User', NULL, 0, NULL),
(116, '5549674528', 'rubbns', 'Free User', NULL, 0, NULL),
(117, '6294769410', 'satan787', 'Free User', NULL, 0, 1),
(118, '1563979238', 'EZPana', 'Free User', NULL, 0, NULL),
(119, '5448204521', '', 'Free User', NULL, 0, NULL),
(120, '1675783726', 'Noel_131', 'Free User', NULL, 0, NULL),
(121, '848740209', 'OscarRojasG', 'Free User', NULL, 0, NULL),
(122, '6235973954', 'cesae899', 'Free User', NULL, -5, NULL),
(123, '1709552868', '', 'Free User', NULL, 0, NULL),
(124, '1530699495', 'AlexHyunSeok', 'Free User', NULL, 0, NULL),
(126, '5520736715', 'volvecredit', 'Free User', NULL, 0, NULL),
(127, '1109303626', 'yoing24', 'Free User', NULL, 0, NULL),
(128, '5617282869', 'TicoCR', 'Free User', NULL, 0, NULL),
(129, '6181014001', 'Aizen320', 'Free User', NULL, 0, NULL),
(130, '786193511', 'UltranetPeru', 'Free User', NULL, 0, NULL),
(131, '5651157254', '', 'Free User', NULL, 0, NULL),
(132, '2124301333', 'HailSatanReturn', 'premium', '2023-09-12', 2147483622, 0),
(133, '1409964150', 'zgamp', 'Free User', NULL, 0, 1),
(134, '5327678715', 'Skxshi', 'Free User', NULL, 0, 1),
(135, '1345152167', 'ElChabel', 'Free User', NULL, 0, 1),
(136, '5145401121', 'JustxnKBO', 'Free User', NULL, 0, NULL),
(137, '1422726620', 'Luisma_Do_not_disturb_04', 'premium', '2023-07-09', 20, 0),
(138, '613075126', 'Nandojerez', 'Free User', NULL, 0, NULL),
(139, '5734523059', 'AndresPKK', 'Free User', NULL, 0, NULL),
(140, '6251740621', 'nattiouj', 'Free User', NULL, 0, NULL),
(141, '5059816124', 'XerozSploitTae', 'Free User', NULL, 0, NULL),
(142, '5844463251', 'Uy_07', 'Free User', NULL, 0, NULL),
(143, '5119012216', 'ErlyTM', 'Free User', NULL, 0, NULL),
(144, '1205717709', 'SachioYT666', 'Free User', NULL, 0, NULL),
(145, '1167048396', 'AndnLyndoFuLL', 'Free User', NULL, 0, NULL),
(146, '1941748161', 'CapitanOozora', 'Free User', NULL, 0, NULL),
(148, '992564490', 'CarlReilly5295', 'Free User', NULL, 0, 1),
(149, '5625908235', 'MrGatox', 'Free User', NULL, 0, 3),
(150, '1290916846', 'hectormzt', 'Free User', NULL, 0, 2),
(151, '1837308594', 'Ismadinho', 'Free User', NULL, 0, 2),
(152, '1516668389', 'Maik_zz', 'Free User', NULL, 0, 1),
(153, '2136925178', 'bxbss', 'Free User', NULL, 0, 1),
(154, '1090427601', 'JACK_ARIAS_09', 'Free User', NULL, 0, 4),
(155, '6172566948', 'Jxrxmyyxray', 'Free User', NULL, 0, 4),
(156, '5556378146', 'jhonkt1', 'Free User', NULL, 0, 3),
(157, '6016441827', 'madre19', 'Free User', NULL, 0, 1),
(158, '5150554869', 'Raphielz', 'Free User', NULL, 0, 1),
(159, '6227006974', 'Papagoku12', 'Free User', NULL, 0, 1),
(160, '5030206556', 'veterano10', 'Free User', NULL, 0, 2),
(161, '1852255628', 'xMclovin01', 'Free User', NULL, 0, NULL),
(162, '686829882', 'Shinoby_01', 'Free User', NULL, 0, NULL),
(163, '1023162460', 'fred047dic', 'Free User', NULL, 0, NULL),
(164, '1988158599', 'iv4n_2218', 'premium', '2023-07-10', 0, 0),
(165, '5333788530', 'Pandaa158', 'Free User', NULL, 0, 3),
(166, '6153470959', 'Desp_on', 'Free User', NULL, 0, NULL),
(167, '5850715014', 'Al3xCodex', 'premium', '2023-07-10', 99999905, 1),
(168, '5207227366', 'Shishiwok', 'Free User', NULL, 0, 2),
(169, '5630011885', 'dimequestasorgullosochifu', 'premium', '2023-06-21', 10, 0),
(170, '5537026160', 'diegossj19', 'Free User', NULL, 0, 1),
(171, '5963388787', 'Andmeno5', 'Free User', NULL, 0, 1),
(172, '1930158570', 'ybn_Eduardo', 'Free User', NULL, 0, 2),
(173, '5556418472', 'MrLon3ly1', 'Free User', NULL, 0, NULL),
(174, '1364828437', 'SantiagoBejarano', 'Free User', NULL, 0, NULL),
(175, '5401158196', 'Annie766', 'premium', '2023-06-21', 0, 0),
(176, '5867822859', 'chovisin', 'premium', '2023-06-21', 15, 0),
(177, '1040718315', 'NepaliGuy', 'Free User', NULL, 0, NULL),
(178, '5478186161', 'JulioIwnl15', 'premium', '2023-07-15', 0, 0),
(179, '5821253667', 'JuliGlow', 'Free User', NULL, 0, NULL),
(180, '610783986', 'mmq145', 'Free User', NULL, 0, NULL),
(181, '5023948723', 'KevinDeBruyneJK', 'Free User', NULL, 0, 1),
(182, '1432255225', 'Pekoon', 'Free User', NULL, 0, NULL),
(183, '5848006844', 'XPanther_28', 'Free User', NULL, 0, NULL),
(184, '5753630363', 'xonlybamby', 'Free User', NULL, 0, NULL),
(185, '5734080537', 'JaxKit', 'Free User', NULL, 0, NULL),
(186, '1425540240', 'ElGatoVolador8', 'Free User', NULL, 0, NULL),
(187, '1451147548', 'CN_chyuloi', 'Free User', NULL, 0, NULL),
(188, '1572842024', 'MT17353', 'Free User', NULL, 0, NULL),
(189, '5641409335', 'Spinxs09', 'Free User', NULL, 0, NULL),
(190, '5673835413', 'Emmaxxl', 'Free User', NULL, 0, NULL),
(191, '6074698848', 'jalxsk', 'Free User', NULL, 0, NULL),
(192, '1436293638', 'Uncognizedx', 'premium', '2023-07-12', 0, NULL),
(193, '1448358405', 'STF275', 'Free User', NULL, 0, NULL),
(194, '2039881562', 'abduskanpng', 'premium', '2023-06-13', 20, 0),
(195, '5202840703', '', 'Free User', NULL, 0, NULL),
(196, '6277300072', 'Donvity10', 'Free User', NULL, 0, NULL),
(197, '5951688121', 'papufrezzerbasado777', 'Free User', NULL, 0, NULL),
(198, '5090465799', 'AlanGCP', 'Free User', NULL, 0, NULL),
(199, '5659389558', 'guanakho503c', 'premium', '2023-06-15', 20, 0),
(200, '6290053684', 'URi3L23', 'Free User', NULL, 0, NULL),
(201, '1101666678', 'MrXetwy21', 'Free User', NULL, 0, NULL),
(202, '999038962', 'PipaPaiAmaVoce', 'Free User', NULL, 0, NULL),
(203, '1605852833', 'TheDumxh', 'premium', '2023-07-15', 15, 0),
(204, '6268965683', 'Incog12m', 'Free User', NULL, 0, NULL),
(205, '6294740891', 'Lakritaz42', 'Free User', NULL, 0, NULL),
(206, '6121618381', 'Crissplay0405', 'Free User', NULL, 0, NULL),
(207, '5002799340', 'ElSemiDios', 'Free User', NULL, 0, NULL),
(208, '5943684374', '', 'Free User', NULL, 0, NULL),
(209, '5783761110', 'payasoxizix', 'Free User', NULL, 0, NULL),
(210, '1214659665', 'Rock_RQV', 'Free User', NULL, 0, NULL),
(211, '5974204823', '', 'Free User', NULL, 0, NULL),
(212, '5622648117', 'Culonadetwitch', 'Free User', NULL, 0, NULL),
(213, '6151223382', 'Michaelbenttt_13', 'Free User', NULL, 0, NULL),
(214, '5324354872', 'Sanchezk1ng', 'Free User', NULL, 0, NULL),
(215, '5139420063', 'EricDC200', 'Free User', NULL, 0, NULL),
(216, '760630040', 'MRSBLACK01', 'Free User', NULL, 0, NULL),
(217, '5625409827', 'idkluisx', 'Free User', NULL, 0, NULL),
(218, '5246369089', 'lualovespiderman', 'Free User', NULL, 0, NULL),
(219, '1210939112', 'Ariesvip_9580', 'Free User', NULL, 0, NULL),
(220, '5631696642', 'LitNight', 'Free User', NULL, 0, NULL),
(221, '1565413323', 'S4pakXrn', 'Free User', NULL, 0, NULL),
(222, '1443147489', 'nigthwingmaster', 'Free User', NULL, 0, NULL),
(223, '1043950894', 'johngc9', 'Free User', NULL, 0, NULL),
(224, '5367551532', 'BreyGar', 'premium', '2023-06-22', 30, 0),
(225, '5638302493', 'TheLord741', 'Free User', NULL, 0, NULL),
(226, '2046973886', 'OHara_Mat', 'premium', '2023-06-18', 15, 0),
(227, '2084519184', 'VodkWiskin', 'premium', '2023-06-18', 20, 0),
(228, '5024808744', 'Johxxn', 'Free User', NULL, 0, NULL),
(229, '1706901041', 'Kytcs', 'Free User', NULL, 0, NULL),
(230, '1556280566', 'el_mono2020', 'Free User', NULL, 0, NULL),
(231, '5790317115', 'Mike_W4zowski', 'Free User', NULL, 0, NULL),
(232, '2062897920', 'Ronymarhez', 'Free User', NULL, 0, NULL),
(233, '1939984147', 'ferna338', 'Free User', NULL, 0, NULL),
(234, '1645453121', 'michelqz', 'Free User', NULL, 0, NULL),
(235, '510002998', 'Machinazos', 'Free User', NULL, 0, NULL),
(236, '2009405324', 'AnthonyM97', 'Free User', NULL, 0, NULL),
(237, '6279984123', 'ranselsx', 'Free User', NULL, 0, NULL),
(238, '5081310186', 'MANUEL_O_O', 'Free User', NULL, 0, NULL),
(239, '1693459008', 'ccuorphe', 'Free User', NULL, 0, NULL),
(240, '1539406840', 'Espartanoroka', 'Free User', NULL, 0, NULL),
(241, '1161210665', 'Minecraft_pro_player', 'Free User', NULL, 0, NULL),
(242, '5797295185', 'Alexanderelcabron', 'Free User', NULL, 0, NULL),
(243, '1887467058', 'juan34222', 'Free User', NULL, 0, NULL),
(244, '1337561569', 'Nov0a', 'Free User', NULL, 0, NULL),
(245, '6231774595', 'SrEsqueleto', 'Free User', NULL, 0, NULL),
(246, '2109024299', 'Yhosneyll', 'Free User', NULL, 0, NULL),
(247, '1267717126', 'MajodeVil', 'Free User', NULL, 0, NULL),
(248, '5221226143', 'SINPIN999', 'Free User', NULL, 0, NULL),
(249, '1779754563', 'DavidGamer654', 'Free User', NULL, 0, NULL),
(250, '5073644696', 'NARUTO_1905', 'Free User', NULL, 0, NULL),
(251, '5523159559', 'Juan_EspitiaRk', 'Free User', NULL, 0, NULL),
(252, '5929878989', 'Abreguu22', 'Free User', NULL, 0, NULL),
(253, '5481863247', 'freddyssj', 'Free User', NULL, 0, NULL),
(254, '1630208457', 'Invincivol', 'Free User', NULL, 0, NULL),
(255, '2050536315', 'baypassLol', 'Free User', NULL, 0, NULL),
(256, '1836788273', 'Urieluwksb', 'Free User', NULL, 0, NULL),
(257, '5378113338', 'Andresikki', 'Free User', NULL, 0, NULL),
(258, '6182749785', 'FrankSanchezR', 'Free User', NULL, 0, NULL),
(259, '6283697551', 'Azarosolavuel', 'Free User', NULL, 0, NULL),
(260, '2062746383', 'Alucard555', 'Free User', NULL, 0, NULL),
(261, '5619927680', 'Manuari001', 'Free User', NULL, 0, NULL),
(262, '5959218838', 'elpaez02', 'Free User', NULL, 0, NULL),
(263, '5039537529', 'sol722', 'Free User', NULL, 0, NULL),
(264, '707583418', 'Nicol_Aylen', 'Free User', NULL, 0, NULL),
(265, '1838121529', '', 'Free User', NULL, 0, NULL),
(267, '5913332608', 'esquisobrrr', 'free user', NULL, 0, 1),
(268, '5453913597', 'ItsXadrxnVoAdmin', 'free user', NULL, 0, NULL),
(269, '5882657172', 'JackT69T', 'free user', NULL, 0, NULL),
(270, '5888708936', 'Jalzxk', 'free user', NULL, 0, NULL),
(271, '5938938509', 'AleecADN', 'free user', NULL, 0, NULL),
(272, '6177060164', 'Aleee989jj', 'Free User', NULL, 0, NULL),
(273, '6141671799', 'Ri0s97', 'Free User', NULL, 0, NULL),
(274, '1605631829', 'Ug_br', 'free user', NULL, 0, NULL),
(275, '5107148718', 'facu_17', 'free user', NULL, 0, NULL),
(276, '5243722063', 'Mathyproo', 'free user', NULL, 0, NULL),
(277, '5865823303', 'NatanaelD', 'free user', NULL, 0, NULL),
(278, '1402370393', 'DarwinOficial', 'free user', NULL, 0, NULL),
(279, '5128048634', 'Olympiaky', 'free user', NULL, 0, NULL),
(280, '6161020040', 'xjuanCOL', 'free user', NULL, 0, NULL),
(281, '5294813713', 'Robin494', 'free user', NULL, 0, NULL),
(282, '5596140059', 'Gab0x', 'free user', NULL, 0, NULL),
(283, '5538185359', 'A5ALiz', 'free user', NULL, 0, NULL),
(284, '5160716770', 'None', 'free user', NULL, 0, NULL),
(285, '5908423094', 'Gbtxo_exe', 'free user', NULL, 0, NULL),
(286, '6335845972', 'NixxGH', 'free user', NULL, 0, NULL),
(287, '5622899993', 'Eloniichan_Idk', 'free user', NULL, 0, NULL),
(288, '1400108091', 'AleSan4', 'free user', NULL, 0, NULL),
(289, '1225593145', 'Ironic_Hub', 'free user', NULL, 0, NULL),
(290, '1600363447', 'Gaxec_1', 'free user', NULL, 0, NULL),
(291, '5494896535', 'David197672', 'free user', NULL, 0, NULL),
(292, '6082776290', 'Nano_mry', 'free user', NULL, 0, NULL),
(293, '966993016', 'WilkinJoyBOY', 'free user', NULL, 0, NULL),
(294, '1848406611', 'Valdo_156', 'free user', NULL, 0, NULL),
(295, '5686987888', 'Catarx027', 'free user', NULL, 0, NULL),
(296, '2002129169', 'Azumi02', 'free user', NULL, 0, NULL),
(297, '1766523461', 'ReyTavo7', 'free user', NULL, 0, NULL),
(298, '5257099150', 'RandomeLand', 'free user', NULL, 0, NULL),
(299, '5831355771', 'Mariaps09', 'free user', NULL, 0, NULL),
(300, '636162978', 'TheRedR', 'free user', NULL, 0, NULL),
(301, '5889101154', 'penelope12377', 'free user', NULL, 0, NULL),
(302, '6217776577', 'ssjmI2023I', 'free user', NULL, 0, NULL),
(303, '6276676252', 'Peprlis', 'free user', NULL, 0, NULL),
(304, '6105560468', 'tatsudev', 'free user', NULL, 0, NULL),
(305, '5468481443', 'frsds_25', 'free user', NULL, 0, NULL),
(306, '2085015477', 'Carlitospro69', 'free user', NULL, 0, NULL),
(307, '5074474975', 'Jovodomi', 'free user', NULL, 0, NULL),
(308, '5575476789', 'Pokedexter', 'free user', NULL, 0, NULL),
(309, '5748970420', 'NeroDemon', 'free user', NULL, 0, NULL),
(310, '1542216260', 'None', 'free user', NULL, 0, NULL),
(311, '1972178618', 'Mati9z', 'free user', NULL, 0, NULL),
(312, '5807441301', 'juaquinhernanzea', 'free user', NULL, 0, NULL),
(313, '5732098310', 'alexsh09', 'free user', NULL, 0, NULL),
(314, '1098112118', 'chapincito26', 'free user', NULL, 0, NULL),
(315, '5972505031', 'Abdiel0121', 'free user', NULL, 0, NULL),
(316, '6092666836', 'perrocholo', 'free user', NULL, 0, NULL),
(317, '1039138371', 'Neu9008', 'free user', NULL, 0, NULL),
(318, '1477399944', 'Dorian_Artty', 'free user', NULL, 0, NULL),
(319, '5835092573', 'SSD_STIVEN', 'free user', NULL, 0, NULL),
(320, '1760358908', 'None', 'free user', NULL, 0, NULL),
(321, '5840125602', 'DiegoLs1', 'free user', NULL, 0, NULL),
(322, '5903847757', 'EveEzxc', 'free user', NULL, 0, NULL),
(323, '1953127343', 'andlxwrld', 'free user', NULL, 0, NULL),
(324, '1384935126', 'Killuminati99', 'free user', NULL, 0, NULL),
(325, '5226922587', 'Manuel22CM', 'free user', NULL, 0, NULL),
(326, '1499679586', 'JoaOfficial', 'free user', NULL, 0, NULL),
(327, '5951471646', 'XR_Darhzzz', 'free user', NULL, 0, NULL),
(328, '6308261913', 'Hanx4', 'free user', NULL, 0, NULL),
(329, '1716668511', 'Walyyx12', 'free user', NULL, 0, NULL),
(330, '6260691378', 'snxbr', 'free user', NULL, 0, NULL),
(331, '5675620317', 'AstxrismY', 'free user', NULL, 0, NULL),
(332, '5577527266', 'Knightthe', 'free user', NULL, 0, NULL),
(333, '5510355891', 'Tesla0303', 'free user', NULL, 0, NULL),
(334, '5653059831', 'zcgta17', 'free user', NULL, 0, NULL),
(335, '5337283579', 'e4zzyv', 'free user', NULL, 0, NULL),
(336, '1620447724', 'Perucho21', 'free user', NULL, 0, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `antispam`
--
ALTER TABLE `antispam`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `keyuser`
--
ALTER TABLE `keyuser`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admins`
--
ALTER TABLE `admins`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `antispam`
--
ALTER TABLE `antispam`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=337;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
