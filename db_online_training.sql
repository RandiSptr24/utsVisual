-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 10 Nov 2025 pada 13.45
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_online_training`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `jabatan`
--

CREATE TABLE `jabatan` (
  `jabatan_id` int(11) NOT NULL,
  `nama_jabatan` varchar(100) NOT NULL,
  `deskripsi` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `jabatan`
--

INSERT INTO `jabatan` (`jabatan_id`, `nama_jabatan`, `deskripsi`, `created_at`) VALUES
(1, 'HR Manager', 'Mengelola sumber daya manusia', '2025-11-10 03:12:40'),
(2, 'Supervisor Tambang', 'Mengawasi operasional tambang', '2025-11-10 03:12:40'),
(3, 'Operator Alat Berat', 'Mengoperasikan alat berat tambang', '2025-11-10 03:12:40'),
(4, 'Safety Officer', 'Bertanggung jawab atas keselamatan kerja', '2025-11-10 03:12:40'),
(5, 'Geologist', 'Ahli geologi pertambangan', '2025-11-10 03:12:40');

-- --------------------------------------------------------

--
-- Struktur dari tabel `questions`
--

CREATE TABLE `questions` (
  `question_id` int(11) NOT NULL,
  `task_id` int(11) NOT NULL,
  `pertanyaan` text NOT NULL,
  `opsi_a` varchar(255) NOT NULL,
  `opsi_b` varchar(255) NOT NULL,
  `opsi_c` varchar(255) NOT NULL,
  `opsi_d` varchar(255) DEFAULT NULL,
  `jawaban_benar` enum('A','B','C','D') NOT NULL,
  `bobot_nilai` int(11) DEFAULT 10,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `questions`
--

INSERT INTO `questions` (`question_id`, `task_id`, `pertanyaan`, `opsi_a`, `opsi_b`, `opsi_c`, `opsi_d`, `jawaban_benar`, `bobot_nilai`, `created_at`) VALUES
(1, 1, 'Apa yang harus dilakukan pertama kali sebelum memasuki area tambang?', 'Langsung masuk', 'Memakai APD lengkap', 'Membawa makanan', 'Menelepon keluarga', 'B', 10, '2025-11-10 03:12:41'),
(2, 1, 'Alat Pelindung Diri (APD) yang wajib digunakan di tambang adalah?', 'Topi biasa', 'Helm safety, sepatu boots, rompi', 'Sandal jepit', 'Topi baseball', 'B', 10, '2025-11-10 03:12:41'),
(3, 1, 'Jika terjadi kecelakaan kerja, apa yang harus dilakukan?', 'Pulang ke rumah', 'Lapor ke supervisor dan safety officer', 'Diam saja', 'Foto untuk media sosial', 'B', 10, '2025-11-10 03:12:41'),
(4, 2, 'Sebelum mengoperasikan excavator, hal pertama yang harus diperiksa adalah?', 'Warna cat', 'Kondisi mesin dan sistem hidrolik', 'Radio', 'AC cabin', 'B', 10, '2025-11-10 03:12:41'),
(5, 2, 'Jarak aman antar alat berat saat beroperasi minimal berapa meter?', '1 meter', '3 meter', '5 meter', '10 meter', 'C', 10, '2025-11-10 03:12:41');

-- --------------------------------------------------------

--
-- Struktur dari tabel `tasks`
--

CREATE TABLE `tasks` (
  `task_id` int(11) NOT NULL,
  `judul` varchar(200) NOT NULL,
  `deskripsi` text DEFAULT NULL,
  `jabatan_id` int(11) DEFAULT NULL,
  `dibuat_oleh` int(11) DEFAULT NULL,
  `tanggal_mulai` date DEFAULT NULL,
  `tanggal_selesai` date DEFAULT NULL,
  `durasi_menit` int(11) DEFAULT 60,
  `status` enum('Aktif','Nonaktif') DEFAULT 'Aktif',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `tasks`
--

INSERT INTO `tasks` (`task_id`, `judul`, `deskripsi`, `jabatan_id`, `dibuat_oleh`, `tanggal_mulai`, `tanggal_selesai`, `durasi_menit`, `status`, `created_at`) VALUES
(1, 'Keselamatan Kerja Tambang', 'Ujian pengetahuan keselamatan kerja di area tambang', 3, 1, '2025-01-01', '2025-12-31', 30, 'Aktif', '2025-11-10 03:12:41'),
(2, 'Prosedur Operasional Alat Berat', 'Evaluasi pemahaman prosedur operasional', 3, 1, '2025-01-01', '2025-12-31', 45, 'Aktif', '2025-11-10 03:12:41');

-- --------------------------------------------------------

--
-- Struktur dari tabel `task_results`
--

CREATE TABLE `task_results` (
  `result_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `task_id` int(11) NOT NULL,
  `nilai` decimal(5,2) DEFAULT 0.00,
  `total_benar` int(11) DEFAULT 0,
  `total_salah` int(11) DEFAULT 0,
  `status` enum('Lulus','Tidak Lulus') DEFAULT 'Tidak Lulus',
  `tanggal_selesai` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` enum('HR','Trainer','Peserta') NOT NULL,
  `jabatan_id` int(11) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `users`
--

INSERT INTO `users` (`user_id`, `name`, `email`, `password`, `role`, `jabatan_id`, `created_at`, `updated_at`) VALUES
(1, 'Admin HR', 'admin@msm.com', 'admin123', 'HR', 1, '2025-11-10 03:12:41', '2025-11-10 03:12:41'),
(2, 'Trainer Mining', 'trainer@msm.com', 'trainer123', 'Trainer', 2, '2025-11-10 03:12:41', '2025-11-10 03:12:41'),
(3, 'John Doe', 'john@msm.com', 'user123', 'Peserta', 3, '2025-11-10 03:12:41', '2025-11-10 03:12:41'),
(4, 'Jane Smith', 'jane@msm.com', 'user123', 'Peserta', 4, '2025-11-10 03:12:41', '2025-11-10 03:12:41');

-- --------------------------------------------------------

--
-- Struktur dari tabel `user_answers`
--

CREATE TABLE `user_answers` (
  `answer_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  `jawaban_user` enum('A','B','C','D') NOT NULL,
  `is_correct` tinyint(1) DEFAULT 0,
  `answered_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `jabatan`
--
ALTER TABLE `jabatan`
  ADD PRIMARY KEY (`jabatan_id`);

--
-- Indeks untuk tabel `questions`
--
ALTER TABLE `questions`
  ADD PRIMARY KEY (`question_id`),
  ADD KEY `task_id` (`task_id`);

--
-- Indeks untuk tabel `tasks`
--
ALTER TABLE `tasks`
  ADD PRIMARY KEY (`task_id`),
  ADD KEY `jabatan_id` (`jabatan_id`),
  ADD KEY `dibuat_oleh` (`dibuat_oleh`);

--
-- Indeks untuk tabel `task_results`
--
ALTER TABLE `task_results`
  ADD PRIMARY KEY (`result_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `task_id` (`task_id`);

--
-- Indeks untuk tabel `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `jabatan_id` (`jabatan_id`);

--
-- Indeks untuk tabel `user_answers`
--
ALTER TABLE `user_answers`
  ADD PRIMARY KEY (`answer_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `question_id` (`question_id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `jabatan`
--
ALTER TABLE `jabatan`
  MODIFY `jabatan_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT untuk tabel `questions`
--
ALTER TABLE `questions`
  MODIFY `question_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT untuk tabel `tasks`
--
ALTER TABLE `tasks`
  MODIFY `task_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT untuk tabel `task_results`
--
ALTER TABLE `task_results`
  MODIFY `result_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `user_answers`
--
ALTER TABLE `user_answers`
  MODIFY `answer_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `questions`
--
ALTER TABLE `questions`
  ADD CONSTRAINT `questions_ibfk_1` FOREIGN KEY (`task_id`) REFERENCES `tasks` (`task_id`) ON DELETE CASCADE;

--
-- Ketidakleluasaan untuk tabel `tasks`
--
ALTER TABLE `tasks`
  ADD CONSTRAINT `tasks_ibfk_1` FOREIGN KEY (`jabatan_id`) REFERENCES `jabatan` (`jabatan_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `tasks_ibfk_2` FOREIGN KEY (`dibuat_oleh`) REFERENCES `users` (`user_id`) ON DELETE SET NULL;

--
-- Ketidakleluasaan untuk tabel `task_results`
--
ALTER TABLE `task_results`
  ADD CONSTRAINT `task_results_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `task_results_ibfk_2` FOREIGN KEY (`task_id`) REFERENCES `tasks` (`task_id`) ON DELETE CASCADE;

--
-- Ketidakleluasaan untuk tabel `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`jabatan_id`) REFERENCES `jabatan` (`jabatan_id`) ON DELETE SET NULL;

--
-- Ketidakleluasaan untuk tabel `user_answers`
--
ALTER TABLE `user_answers`
  ADD CONSTRAINT `user_answers_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `user_answers_ibfk_2` FOREIGN KEY (`question_id`) REFERENCES `questions` (`question_id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
