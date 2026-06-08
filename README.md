Proyek ini adalah simulasi proses ETL (Extract, Transform, Load) menggunakan Python. Fokus utamanya adalah mengambil data mentah transaksi pesanan dari layanan delivery, membersihkan data yang bermasalah, lalu memasukkannya ke dalam database agar siap dianalisis.

Tech Stack
Python - Pandas (untuk manipulasi dan cleaning data)
SQLite (sebagai database lokal untuk menyimpan hasil akhir)

Alur Kerja (ETL Process)
1. Extract
Membaca data mentah dari file transaksi_pesanan.csv. Data ini sengaja memuat beberapa error untuk mensimulasikan masalah yang sering terjadi di lapangan, seperti data kosong, typo, atau perbedaan format.

2. Transform
Di tahap ini, data diproses dan dibersihkan menggunakan Pandas. Beberapa hal yang ditangani antara lain:
- Missing Values: Menghapus baris transaksi yang tidak memiliki nama barang atau jumlah beli.
- Standarisasi Teks: Merapikan penulisan huruf kapital pada nama barang dan status pengiriman agar seragam.
- Koreksi Typo: Memperbaiki kesalahan ketik pada data, misalnya mengubah status "Dikrim" menjadi "Dikirim".
- Koreksi Anomali Angka: Mengubah nilai minus pada total belanja menjadi angka positif untuk mengatasi kemungkinan salah input kasir.
- Standarisasi Tanggal: Mengonversi berbagai macam format tanggal yang berantakan menjadi satu standar baku YYYY-MM-DD.

3. Load
Data yang sudah melewati tahap cleaning kemudian di-load ke dalam database relasional SQLite. Skrip otomatis membuat file db_anterin.db dan menyimpan data tersebut di dalam tabel transaksi_bersih.

Cara Menjalankan
Pastikan Python sudah ter-install di perangkat.
Install library Pandas dengan menjalankan perintah:

Bash
pip install pandas
Buka terminal di folder repository ini, lalu jalankan skrip utama:

Bash
python main.py
Jika proses berhasil, file db_anterin.db akan muncul di folder yang sama dan siap dibuka melalui SQLite Viewer.
