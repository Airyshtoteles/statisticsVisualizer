# 📊 Statistik Visualizer (GUI Python)

**Statistik Visualizer** adalah aplikasi GUI berbasis Python yang dibuat menggunakan **Tkinter**. Aplikasi ini memungkinkan kamu untuk memasukkan data angka, lalu menampilkan statistik deskriptif, membuat grafik histogram dan boxplot, serta mengekspor hasil analisis ke file `.txt`.

Cocok untuk pelajar, mahasiswa, guru, atau siapa pun yang ingin memahami data dengan cara yang simpel dan visual.

---

## ✨ Fitur Utama

- 🧮 Menghitung statistik dasar: mean, median, modus, standar deviasi, varian, dll.
- 📊 Menampilkan visualisasi data (histogram & boxplot)
- 📝 Mengekspor hasil analisis ke file teks (`.txt`)
- 🖱️ Antarmuka visual interaktif menggunakan Tkinter

---

## 🖼️ Tampilan Aplikasi

*(Tambahkan gambar di sini kalau sudah punya)*

---

## 📦 Struktur Proyek

statisticsVisualizer/
├── main.py # GUI utama dengan Tkinter
├── data_handler.py # Pengelolaan dan analisis data
├── visualizer.py # Modul visualisasi dengan matplotlib
├── export_tools.py # Fitur ekspor hasil analisis
├── requirements.txt # Daftar dependensi
└── README.md # Dokumentasi (file ini)

yaml
Copy
Edit

---

## 🔧 Instalasi & Menjalankan

### 1. Clone repositori:

```bash
git clone https://github.com/Airyshtoteles/statisticsVisualizer.git
cd statisticsVisualizer
2. Buat dan aktifkan virtual environment (opsional tapi disarankan):
bash

python -m venv venv
venv\Scripts\activate        # Untuk Windows
# source venv/bin/activate  # Untuk Mac/Linux
3. Install dependensi:
bash

pip install matplotlib tkinter numpy pandas seaborn
4. Jalankan aplikasinya:
bash
python main.py
📘 Cara Menggunakan
Masukkan data angka yang dipisahkan dengan koma, misalnya:

10, 15, 12, 8, 20, 15
Klik tombol "Proses Data" untuk menghitung statistik.

Lihat hasil statistik seperti Mean, Median, Modus, dll. akan muncul di kolom bawah.

Gunakan tombol:

"Tampilkan Histogram" → untuk menampilkan grafik distribusi

"Tampilkan Boxplot" → untuk melihat distribusi data secara visual

"Ekspor Laporan ke TXT" → untuk menyimpan hasil statistik ke file teks
