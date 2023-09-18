-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 18, 2023 at 02:45 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `django_online_marketplace`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add category', 7, 'add_category'),
(26, 'Can change category', 7, 'change_category'),
(27, 'Can delete category', 7, 'delete_category'),
(28, 'Can view category', 7, 'view_category'),
(29, 'Can add item', 8, 'add_item'),
(30, 'Can change item', 8, 'change_item'),
(31, 'Can delete item', 8, 'delete_item'),
(32, 'Can view item', 8, 'view_item'),
(33, 'Can add conversation message', 9, 'add_conversationmessage'),
(34, 'Can change conversation message', 9, 'change_conversationmessage'),
(35, 'Can delete conversation message', 9, 'delete_conversationmessage'),
(36, 'Can view conversation message', 9, 'view_conversationmessage'),
(37, 'Can add conversation', 10, 'add_conversation'),
(38, 'Can change conversation', 10, 'change_conversation'),
(39, 'Can delete conversation', 10, 'delete_conversation'),
(40, 'Can view conversation', 10, 'view_conversation');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$BfX25WeeCRj3wwFLqr4gWy$IoNAC5r/KRKfZMwgQemc5Qi4pFq2G/+1gMllrziFK4Q=', '2023-09-14 12:51:34.937874', 1, 'ariston', '', '', 'aristoncatipay123@gmail.com', 1, 1, '2023-09-13 00:10:25.776458'),
(2, 'pbkdf2_sha256$600000$wYh5K9tVZbwTOZcIA3mAiF$rU4ZVv7DpL+fR/oMXb6fldmmv7rOTbf47i2fEKtzeuM=', '2023-09-14 13:44:47.158080', 0, 'Harvi', '', '', 'harvi.ramos123@gmail.com', 0, 1, '2023-09-14 03:48:13.492716');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `conversation_conversation`
--

CREATE TABLE `conversation_conversation` (
  `id` bigint(20) NOT NULL,
  `created_at` date NOT NULL,
  `modified_at` datetime(6) NOT NULL,
  `item_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `conversation_conversation`
--

INSERT INTO `conversation_conversation` (`id`, `created_at`, `modified_at`, `item_id`) VALUES
(1, '2023-09-15', '2023-09-15 12:25:04.542834', 3),
(2, '2023-09-15', '2023-09-15 12:26:14.378214', 3),
(3, '2023-09-15', '2023-09-15 12:26:18.372465', 3),
(4, '2023-09-15', '2023-09-15 12:33:29.985668', 3),
(5, '2023-09-15', '2023-09-15 13:43:19.641686', 3);

-- --------------------------------------------------------

--
-- Table structure for table `conversation_conversationmessage`
--

CREATE TABLE `conversation_conversationmessage` (
  `id` bigint(20) NOT NULL,
  `content` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `conversation_id` bigint(20) NOT NULL,
  `created_by_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `conversation_conversationmessage`
--

INSERT INTO `conversation_conversationmessage` (`id`, `content`, `created_at`, `conversation_id`, `created_by_id`) VALUES
(1, 'Hello Ariston. I\'m interested with the Shoe. Is it still available?', '2023-09-15 12:25:04.545887', 1, 2),
(2, 'Hello Ariston. I\'m interested with the Shoe. Is it still available?', '2023-09-15 12:26:14.378214', 2, 2),
(3, 'Hello Ariston. I\'m interested with the Shoe. Is it still available?', '2023-09-15 12:26:18.375051', 3, 2),
(4, 'Hello Ariston. I\'m interested with the Shoe. Is it still available?', '2023-09-15 12:33:29.985668', 4, 2),
(5, 'Hello Ariston, My name is Harvi. I am very interested in the shoes you are selling. Is it still available?', '2023-09-15 12:39:15.146438', 5, 2),
(6, 'Also, if you don\'t mind me asking what is the shoe size?', '2023-09-15 13:41:24.500039', 5, 2),
(7, 'Also, if you don\'t mind me asking what is the shoe size?', '2023-09-15 13:42:02.549715', 5, 2),
(8, 'Also, if you don\'t mind me asking what is the shoe size?', '2023-09-15 13:42:04.497967', 5, 2),
(9, 'Also, if you don\'t mind me asking what is the shoe size?', '2023-09-15 13:42:47.284975', 5, 2),
(10, 'Also, if you don\'t mind me asking what is the shoe size?', '2023-09-15 13:43:19.629601', 5, 2);

-- --------------------------------------------------------

--
-- Table structure for table `conversation_conversation_members`
--

CREATE TABLE `conversation_conversation_members` (
  `id` bigint(20) NOT NULL,
  `conversation_id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `conversation_conversation_members`
--

INSERT INTO `conversation_conversation_members` (`id`, `conversation_id`, `user_id`) VALUES
(2, 1, 1),
(1, 1, 2),
(4, 2, 1),
(3, 2, 2),
(6, 3, 1),
(5, 3, 2),
(8, 4, 1),
(7, 4, 2),
(10, 5, 1),
(9, 5, 2);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-09-13 00:31:39.069748', '1', 'Clothes', 1, '[{\"added\": {}}]', 7, 1),
(2, '2023-09-13 00:34:20.828381', '2', 'Furniture', 1, '[{\"added\": {}}]', 7, 1),
(3, '2023-09-13 00:34:31.279821', '3', 'Toys', 1, '[{\"added\": {}}]', 7, 1),
(4, '2023-09-13 06:47:41.838198', '1', 'Red Shoes', 1, '[{\"added\": {}}]', 8, 1),
(5, '2023-09-13 06:59:23.444337', '2', 'Brown Shoes', 1, '[{\"added\": {}}]', 8, 1),
(6, '2023-09-13 07:21:39.154515', '2', 'Brown Shoes', 3, '', 8, 1),
(7, '2023-09-13 07:23:20.859470', '3', 'Brown Shoes', 1, '[{\"added\": {}}]', 8, 1),
(8, '2023-09-14 12:51:50.005535', '6', 'Table Set', 3, '', 8, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(10, 'conversation', 'conversation'),
(9, 'conversation', 'conversationmessage'),
(7, 'item', 'category'),
(8, 'item', 'item'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-09-12 23:57:08.859145'),
(2, 'auth', '0001_initial', '2023-09-12 23:57:09.323327'),
(3, 'admin', '0001_initial', '2023-09-12 23:57:09.436287'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-09-12 23:57:09.446261'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-09-12 23:57:09.455470'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-09-12 23:57:09.523649'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-09-12 23:57:09.572490'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-09-12 23:57:09.592640'),
(9, 'auth', '0004_alter_user_username_opts', '2023-09-12 23:57:09.603612'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-09-12 23:57:09.661434'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-09-12 23:57:09.664428'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-09-12 23:57:09.673517'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-09-12 23:57:09.692107'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-09-12 23:57:09.712049'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-09-12 23:57:09.734470'),
(16, 'auth', '0011_update_proxy_permissions', '2023-09-12 23:57:09.744422'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-09-12 23:57:09.766562'),
(18, 'sessions', '0001_initial', '2023-09-12 23:57:09.808650'),
(19, 'item', '0001_initial', '2023-09-12 23:59:27.084225'),
(20, 'item', '0002_alter_category_options_item', '2023-09-13 01:37:37.802398'),
(21, 'conversation', '0001_initial', '2023-09-15 11:37:23.422873');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('dwrvnnlt8yw6z484v2rd1gmp7n40ek40', '.eJxVjDsOwjAQBe_iGlnxNzYlPWew1t5dHECOFCcV4u4QKQW0b2beSyTY1pq2TkuaUJyFFqffLUN5UNsB3qHdZlnmti5TlrsiD9rldUZ6Xg7376BCr9-axuhM5OACGsWqhGzVkLXyYQSHg0X22pHJHg17Y9kxxGg0F4Ks0JF4fwDTkTgS:1qgmeF:tpwBXuRKp-VQmqo9IwR3nKlBsIHg23ItbhduESQKU1s', '2023-09-28 13:44:47.160635');

-- --------------------------------------------------------

--
-- Table structure for table `item_category`
--

CREATE TABLE `item_category` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `item_category`
--

INSERT INTO `item_category` (`id`, `name`) VALUES
(1, 'Clothes'),
(2, 'Furniture'),
(3, 'Toys');

-- --------------------------------------------------------

--
-- Table structure for table `item_item`
--

CREATE TABLE `item_item` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` longtext DEFAULT NULL,
  `price` double NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `is_sold` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `category_id` bigint(20) NOT NULL,
  `created_by_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `item_item`
--

INSERT INTO `item_item` (`id`, `name`, `description`, `price`, `image`, `is_sold`, `created_at`, `category_id`, `created_by_id`) VALUES
(1, 'Red Shoes', 'Used but not abused. Kindly message me if you are interested.', 5000, 'item_images/Red_Shoes.jpg', 0, '2023-09-13 06:47:41.836455', 1, 1),
(3, 'Brown Shoes', 'Used but not abused. Kindly message me if you are interested.', 4000, 'item_images/Brown_Shoes.jpg', 0, '2023-09-13 07:23:20.858474', 1, 1),
(5, 'Table Set', 'A white table set with two chairs. Kindly message me if you are interested.', 10000, 'item_images/Table_Set.jpg', 0, '2023-09-14 12:45:54.154261', 2, 2),
(7, 'White Vase', 'Imported from Japan. In very presentable condition. Kindly message me if you are interested. Edited Description.', 2000, 'item_images/Vase.jpg', 0, '2023-09-15 03:27:00.172871', 2, 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `conversation_conversation`
--
ALTER TABLE `conversation_conversation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `conversation_conversation_item_id_228c4088_fk_item_item_id` (`item_id`);

--
-- Indexes for table `conversation_conversationmessage`
--
ALTER TABLE `conversation_conversationmessage`
  ADD PRIMARY KEY (`id`),
  ADD KEY `conversation_convers_conversation_id_fdd084d4_fk_conversat` (`conversation_id`),
  ADD KEY `conversation_convers_created_by_id_aa6cea66_fk_auth_user` (`created_by_id`);

--
-- Indexes for table `conversation_conversation_members`
--
ALTER TABLE `conversation_conversation_members`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `conversation_conversatio_conversation_id_user_id_8676b40f_uniq` (`conversation_id`,`user_id`),
  ADD KEY `conversation_convers_user_id_226f9afc_fk_auth_user` (`user_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `item_category`
--
ALTER TABLE `item_category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `item_item`
--
ALTER TABLE `item_item`
  ADD PRIMARY KEY (`id`),
  ADD KEY `item_item_category_id_7971a411_fk_item_category_id` (`category_id`),
  ADD KEY `item_item_created_by_id_abf41b7a_fk_auth_user_id` (`created_by_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `conversation_conversation`
--
ALTER TABLE `conversation_conversation`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `conversation_conversationmessage`
--
ALTER TABLE `conversation_conversationmessage`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `conversation_conversation_members`
--
ALTER TABLE `conversation_conversation_members`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `item_category`
--
ALTER TABLE `item_category`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `item_item`
--
ALTER TABLE `item_item`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `conversation_conversation`
--
ALTER TABLE `conversation_conversation`
  ADD CONSTRAINT `conversation_conversation_item_id_228c4088_fk_item_item_id` FOREIGN KEY (`item_id`) REFERENCES `item_item` (`id`);

--
-- Constraints for table `conversation_conversationmessage`
--
ALTER TABLE `conversation_conversationmessage`
  ADD CONSTRAINT `conversation_convers_conversation_id_fdd084d4_fk_conversat` FOREIGN KEY (`conversation_id`) REFERENCES `conversation_conversation` (`id`),
  ADD CONSTRAINT `conversation_convers_created_by_id_aa6cea66_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `conversation_conversation_members`
--
ALTER TABLE `conversation_conversation_members`
  ADD CONSTRAINT `conversation_convers_conversation_id_c146fce9_fk_conversat` FOREIGN KEY (`conversation_id`) REFERENCES `conversation_conversation` (`id`),
  ADD CONSTRAINT `conversation_convers_user_id_226f9afc_fk_auth_user` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `item_item`
--
ALTER TABLE `item_item`
  ADD CONSTRAINT `item_item_category_id_7971a411_fk_item_category_id` FOREIGN KEY (`category_id`) REFERENCES `item_category` (`id`),
  ADD CONSTRAINT `item_item_created_by_id_abf41b7a_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
