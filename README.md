# 🚴‍♂️ Bike Sharing Analysis Dashboard

## 📌 Deskripsi Proyek
Proyek ini adalah dashboard interaktif yang dibuat menggunakan Streamlit untuk menganalisis penggunaan sepeda berdasarkan berbagai faktor, seperti cuaca, hari kerja, dan waktu dalam sehari. Data yang digunakan berasal dari dataset **Bike Sharing Dataset** yang berisi informasi peminjaman sepeda berdasarkan hari dan jam.

## 🔧 Fitur Dashboard
- **📅 Filter Waktu**: Memungkinkan pengguna memilih bulan, tahun, dan rentang jam.
- **🌤 Analisis Pengaruh Cuaca**: Menunjukkan bagaimana kondisi cuaca memengaruhi jumlah pengguna sepeda.
- **📆 Pola Penggunaan Harian**: Membandingkan jumlah pengguna sepeda antara hari kerja dan akhir pekan.
- **🕒 Pola Penggunaan Jam**: Menganalisis pola penggunaan sepeda berdasarkan jam dalam sehari.

## 🏗️ Instalasi & Menjalankan Aplikasi
1. **Clone Repository**
   ```bash
   git clone https://github.com/suryaagus9/Proyek-Analisis-Data.git
   cd bike-sharing-dashboard
   ```

2. **Buat Virtual Environment** (Opsional, tetapi disarankan)
   ```bash
   python -m venv env
   source env/bin/activate  # MacOS/Linux
   env\Scripts\activate    # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan Aplikasi Streamlit**
   ```bash
   streamlit run dashboard/dashboard.py
   ```

## 📂 Struktur Direktori
```
├── dashboard/		
│   ├── dashboard.py
│   ├── main_data.csv
├── data/	
│   ├── day.csv
│   ├── hour.csv
├── notebook.py		
├── requirements.txt	
├── README.md
├── url.txt		
```

## 📊 Insight Utama dari Analisis
- **Pengaruh Cuaca**: Jumlah pengguna sepeda menurun pada kondisi cuaca buruk.
- **Pola Harian**: Penggunaan sepeda lebih tinggi pada hari kerja dibandingkan akhir pekan.
- **Pola Jam**: Lonjakan pengguna terjadi pada jam sibuk (pagi & sore).

## 🤝 Kontribusi
Kontribusi sangat dihargai! Silakan fork repository ini dan buat pull request untuk perbaikan atau fitur baru.

