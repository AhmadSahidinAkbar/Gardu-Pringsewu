import streamlit as st
import streamlit.components.v1 as components
import os
import csv

# Konfigurasi halaman
st.set_page_config(
    page_title="Peta Angklung Indonesia",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header aplikasi
st.title("Peta Angklung Indonesia")
st.markdown("---")

# Fungsi untuk membaca CSV
def read_csv_data(filename):
    data = []
    if os.path.exists(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                data = list(csv_reader)
        except Exception as e:
            st.error(f"Error reading CSV: {e}")
    return data

# Sidebar
with st.sidebar:
    st.header("Tentang Angklung")
    st.markdown("""
    **Angklung** adalah alat musik tradisional Indonesia yang terbuat dari bambu. 
    Alat musik ini berasal dari Jawa Barat dan telah diakui oleh UNESCO sebagai 
    Warisan Budaya Takbenda Manusia.
    
    ### Fitur Peta:
    - Lokasi-lokasi angklung di Indonesia
    - Peta interaktif dengan Leaflet
    - Data dalam format CSV
    """)
    
    # Load dan tampilkan info data
    data = read_csv_data("angklung.csv")
    if data:
        st.subheader("Data Angklung")
        st.write(f"Total lokasi: {len(data)}")
        
        # Download button
        try:
            with open("angklung.csv", 'r', encoding='utf-8') as file:
                csv_content = file.read()
                st.download_button(
                    label="Download Data CSV",
                    data=csv_content,
                    file_name="angklung_data.csv",
                    mime="text/csv"
                )
        except Exception as e:
            st.error(f"Error preparing download: {e}")

# Main content
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("Peta Interaktif Angklung Indonesia")
    
    # Baca dan tampilkan HTML file
    html_file_path = "peta_angklung_final.html"
    
    if os.path.exists(html_file_path):
        try:
            # Baca file HTML
            with open(html_file_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            # Tampilkan HTML dalam Streamlit
            components.html(html_content, height=600, scrolling=True)
            
            st.success("Peta berhasil dimuat!")
            
        except Exception as e:
            st.error(f"Error loading HTML file: {e}")
        
    else:
        st.error("File peta_angklung_final.html tidak ditemukan!")
        st.info("Pastikan file HTML ada di folder yang sama dengan aplikasi ini.")

with col2:
    st.subheader("Informasi")
    
    data = read_csv_data("angklung.csv")
    
    if data:
        st.metric("Total Lokasi", len(data))
        
        # Tampilkan preview data
        st.subheader("Preview Data")
        
        # Tampilkan 5 data pertama
        preview_data = data[:5] if len(data) > 5 else data
        for i, row in enumerate(preview_data, 1):
            with st.expander(f"Lokasi {i}"):
                for key, value in row.items():
                    st.write(f"**{key}**: {value}")
        
        # Statistik sederhana
        if data:
            st.subheader("Statistik")
            
            # Hitung provinsi jika ada kolom provinsi
            provinces = {}
            for row in data:
                # Coba beberapa nama kolom yang mungkin untuk provinsi
                prov_value = None
                for prov_key in ['provinsi', 'province', 'Provinsi', 'Province']:
                    if prov_key in row:
                        prov_value = row[prov_key]
                        break
                
                if prov_value:
                    provinces[prov_value] = provinces.get(prov_value, 0) + 1
            
            if provinces:
                st.write("**Distribusi per Provinsi:**")
                # Tampilkan top 10 provinsi
                sorted_provinces = sorted(provinces.items(), key=lambda x: x[1], reverse=True)[:10]
                for prov, count in sorted_provinces:
                    st.write(f"• {prov}: {count} lokasi")
    
    else:
        st.warning("File angklung.csv tidak ditemukan atau kosong!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p><b>Dibuat untuk melestarikan budaya Indonesia</b></p>
    <p>Data angklung dari berbagai sumber | Peta menggunakan Leaflet.js</p>
</div>
""", unsafe_allow_html=True)
