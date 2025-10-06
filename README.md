# 🎵 Peta Angklung Indonesia - Streamlit App

Aplikasi web interaktif yang menampilkan peta lokasi-lokasi angklung di Indonesia menggunakan Streamlit.

## 📋 Fitur

- 🗺️ **Peta Interaktif**: Menampilkan lokasi angklung menggunakan Leaflet.js
- 📊 **Visualisasi Data**: Grafik dan statistik lokasi angklung
- 📥 **Download Data**: Export data dalam format CSV
- 📱 **Responsive**: Dapat diakses di desktop dan mobile

## 🚀 Cara Menjalankan

### Lokal

1. **Install Python** (3.8 atau lebih baru)
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Jalankan aplikasi**:
   ```bash
   streamlit run app.py
   ```

### Deploy ke Streamlit Cloud

1. **Upload ke GitHub repository**
2. **Buka [share.streamlit.io](https://share.streamlit.io)**
3. **Connect dengan GitHub repository**
4. **Deploy aplikasi**

## 📁 Struktur File

```
streamlit-angklung/
├── app.py                      # Aplikasi utama Streamlit
├── peta_angklung_final.html    # File HTML peta interaktif
├── angklung.csv                # Data lokasi angklung
├── requirements.txt            # Dependencies Python
└── README.md                   # Dokumentasi
```

## 🛠️ Teknologi

- **Streamlit**: Framework aplikasi web Python
- **Pandas**: Manipulasi dan analisis data
- **Leaflet.js**: Library peta interaktif
- **HTML/CSS/JavaScript**: Frontend untuk peta

## 📊 Data

Data angklung berisi informasi:
- Lokasi geografis (latitude, longitude)
- Nama tempat/daerah
- Informasi tambahan terkait angklung

## 🌐 Deploy ke Streamlit Cloud

1. **Push ke GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Streamlit Angklung App"
   git remote add origin https://github.com/[username]/streamlit-angklung
   git push -u origin main
   ```

2. **Deploy di Streamlit Cloud**:
   - Buka https://share.streamlit.io
   - Klik "New app"
   - Pilih repository GitHub
   - Set file utama: `app.py`
   - Klik "Deploy"

## 📝 Catatan

- Pastikan file `peta_angklung_final.html` dan `angklung.csv` ada di folder yang sama
- Aplikasi akan otomatis membaca dan menampilkan data
- Untuk modifikasi, edit file `app.py`

## 🤝 Kontribusi

Aplikasi ini dibuat untuk melestarikan budaya Indonesia. Kontribusi dan saran sangat diterima!

---

🇮🇩 **Dibuat dengan ❤️ untuk Indonesia** 🇮🇩