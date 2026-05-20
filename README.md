# Sistem Prediksi Risiko Stroke

Aplikasi web berbasis **Streamlit** untuk memprediksi risiko penyakit stroke pada pasien berdasarkan data kesehatan mereka.

---

## 📋 Daftar Isi
- [Persyaratan Sistem](#persyaratan-sistem)
- [Instalasi](#instalasi)
- [Cara Menjalankan](#cara-menjalankan)
- [Fitur Aplikasi](#fitur-aplikasi)
- [Data Input Pasien](#data-input-pasien)
- [Contoh Kasus](#contoh-kasus)

---

## 🖥️ Persyaratan Sistem

- **Python**: Versi 3.7 atau lebih baru
- **Sistem Operasi**: Windows, macOS, atau Linux
- **RAM**: Minimal 2 GB
- **Koneksi Internet**: Tidak diperlukan setelah instalasi

---

## 📦 Instalasi

### 1. Clone atau Download Repository
```bash
# Jika menggunakan Git
git clone <repository-url>
cd Stroke-Prediction

# Atau ekstrak file ZIP yang sudah didownload
```

### 2. Buat Virtual Environment (Opsional tapi Disarankan)

**Untuk Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Untuk macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

**Atau install secara manual:**
```bash
pip install streamlit pandas numpy joblib
```

---

## 🚀 Cara Menjalankan

### 1. Memastikan File Model Tersedia
Pastikan file berikut ada di direktori yang sama dengan `app.py`:
- `model_xgboost_stroke.pkl` (Model XGBoost)
- `scaler_stroke.pkl` (Scaler untuk normalisasi data)

### 2. Jalankan Aplikasi
Buka terminal/command prompt di folder project dan ketik:

```bash
streamlit run app.py
```

### 3. Akses Aplikasi
Setelah menjalankan perintah di atas, aplikasi akan membuka di browser secara otomatis pada:
```
http://localhost:8501
```

Jika tidak membuka otomatis, buka link di atas secara manual di browser Anda.

---

## ⚙️ Fitur Aplikasi

### Data Input yang Diperlukan:

#### **Data Demografi:**
- **Umur**: Rentang 0-120 tahun
- **Jenis Kelamin**: Male / Female
- **Pernah Menikah**: Yes / No
- **Tipe Pekerjaan**: Private, Self-employed, Govt_job, children, Never_worked
- **Tipe Tempat Tinggal**: Urban / Rural

#### **Data Kesehatan:**
- **BMI (Body Mass Index)**: Rentang 10-100
- **Rata-rata Level Glukosa**: Rentang 50-300 mg/dL
- **Hipertensi**: No / Yes
- **Penyakit Jantung**: No / Yes
- **Status Merokok**: never smoked, formerly smoked, smokes, Unknown

### Output:
- **Status Risiko**: Tinggi atau Rendah
- **Persentase Risiko**: Probabilitas pasien terkena stroke (%)
- **Visualisasi**: Progress bar untuk menampilkan tingkat risiko

---

## 📊 Data Input Pasien

### **Pasien dengan Risiko TINGGI Stroke (Positif)**

#### Contoh Kasus 1: Pria Tua dengan Hipertensi
```
Umur:                    65 tahun
Jenis Kelamin:           Male
Pernah Menikah:          Yes
Tipe Pekerjaan:          Private
Tipe Tempat Tinggal:     Urban
BMI:                     32.5
Rata-rata Level Glukosa: 145.3 mg/dL
Hipertensi:              Yes
Penyakit Jantung:        Yes
Status Merokok:          formerly smoked
```

#### Contoh Kasus 2: Wanita dengan Glukosa Tinggi
```
Umur:                    58 tahun
Jenis Kelamin:           Female
Pernah Menikah:          Yes
Tipe Pekerjaan:          Self-employed
Tipe Tempat Tinggal:     Rural
BMI:                     28.9
Rata-rata Level Glukosa: 178.5 mg/dL
Hipertensi:              Yes
Penyakit Jantung:        No
Status Merokok:          smokes
```

#### Contoh Kasus 3: Laki-laki Merokok Aktif
```
Umur:                    72 tahun
Jenis Kelamin:           Male
Pernah Menikah:          Yes
Tipe Pekerjaan:          Govt_job
Tipe Tempat Tinggal:     Urban
BMI:                     26.8
Rata-rata Level Glukosa: 155.0 mg/dL
Hipertensi:              Yes
Penyakit Jantung:        Yes
Status Merokok:          smokes
```

---

### **Pasien dengan Risiko RENDAH Stroke (Negatif)**

#### Contoh Kasus 1: Pria Muda Sehat
```
Umur:                    28 tahun
Jenis Kelamin:           Male
Pernah Menikah:          No
Tipe Pekerjaan:          Private
Tipe Tempat Tinggal:     Urban
BMI:                     22.1
Rata-rata Level Glukosa: 85.5 mg/dL
Hipertensi:              No
Penyakit Jantung:        No
Status Merokok:          never smoked
```

#### Contoh Kasus 2: Wanita dengan Kondisi Sehat
```
Umur:                    35 tahun
Jenis Kelamin:           Female
Pernah Menikah:          Yes
Tipe Pekerjaan:          Private
Tipe Tempat Tinggal:     Urban
BMI:                     24.3
Rata-rata Level Glukosa: 88.2 mg/dL
Hipertensi:              No
Penyakit Jantung:        No
Status Merokok:          never smoked
```

#### Contoh Kasus 3: Pria Dewasa Normal
```
Umur:                    45 tahun
Jenis Kelamin:           Male
Pernah Menikah:          Yes
Tipe Pekerjaan:          Self-employed
Tipe Tempat Tinggal:     Rural
BMI:                     25.7
Rata-rata Level Glukosa: 92.1 mg/dL
Hipertensi:              No
Penyakit Jantung:        No
Status Merokok:          formerly smoked
```

---

## 🎯 Contoh Kasus

### **Cara Menggunakan Aplikasi:**

1. **Buka aplikasi** di browser (http://localhost:8501)
2. **Isi formulir** dengan data pasien sesuai dengan contoh di atas
3. **Klik tombol** "Lakukan Analisis Prediksi"
4. **Lihat hasil** prediksi yang ditampilkan di bagian bawah

### **Interpretasi Hasil:**

- **Status TINGGI (Merah)**: Pasien terdeteksi memiliki risiko tinggi stroke, perlu segera konsultasi dengan dokter
- **Status RENDAH (Hijau)**: Pasien memiliki risiko rendah, namun tetap perlu menjaga kesehatan

---

## 📝 Catatan Penting

- Model ini dilatih pada dataset tertentu dan bersifat prediktif, bukan diagnosis medis yang definitif
- Selalu konsultasikan hasil prediksi dengan dokter profesional
- Jaga gaya hidup sehat dan lakukan pemeriksaan kesehatan berkala
- Data input harus valid dan sesuai dengan format yang ditentukan

---

## 🔧 Troubleshooting

### Aplikasi tidak berjalan?
```bash
# Pastikan semua dependencies terinstall
pip install --upgrade streamlit pandas numpy joblib

# Pastikan Anda di folder yang benar
cd path/to/Stroke-Prediction

# Jalankan kembali
streamlit run app.py
```

### Error: Model tidak ditemukan
- Pastikan file `model_xgboost_stroke.pkl` dan `scaler_stroke.pkl` ada di folder project
- Letakkan file tersebut di direktori yang sama dengan `app.py`

### Port 8501 sudah terpakai?
```bash
streamlit run app.py --server.port 8502
```

---
**Terakhir diperbarui:** 21 Mei 2026
