import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import os

# Konfigurasi halaman
st.set_page_config(
    page_title="Peta Angklung Indonesia",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header aplikasi
st.title("🎵 Peta Angklung Indonesia")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("🎋 Tentang Angklung")
    st.markdown("""
    **Angklung** adalah alat musik tradisional Indonesia yang terbuat dari bambu. 
    Alat musik ini berasal dari Jawa Barat dan telah diakui oleh UNESCO sebagai 
    Warisan Budaya Takbenda Manusia.
    
    ### Fitur Peta:
    - 📍 Lokasi-lokasi angklung di Indonesia
    - 🗺️ Peta interaktif dengan Leaflet
    - 📊 Data dalam format CSV
    """)
    
    # Tombol untuk download data
    if os.path.exists("angklung.csv"):
        df = pd.read_csv("angklung.csv")
        st.subheader("📊 Data Angklung")
        st.write(f"Total lokasi: {len(df)}")
        
        # Download button
        csv = df.to_csv(index=False)
        st.download_button(
            label="📥 Download Data CSV",
            data=csv,
            file_name="angklung_data.csv",
            mime="text/csv"
        )

# Main content
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("🗺️ Peta Interaktif Angklung Indonesia")
    
    # Baca dan tampilkan HTML file
    html_file_path = "peta_angklung_final.html"
    
    if os.path.exists(html_file_path):
        # Baca file HTML
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Tampilkan HTML dalam Streamlit
        components.html(html_content, height=600, scrolling=True)
        
        st.success("✅ Peta berhasil dimuat!")
        
    else:
        st.error("❌ File peta_angklung_final.html tidak ditemukan!")
        st.info("📁 Pastikan file HTML ada di folder yang sama dengan aplikasi ini.")

with col2:
    st.subheader("📋 Informasi")
    
    if os.path.exists("angklung.csv"):
        df = pd.read_csv("angklung.csv")
        
        st.metric("Total Lokasi", len(df))
        
        # Tampilkan preview data
        st.subheader("👀 Preview Data")
        st.dataframe(df.head(), use_container_width=True)
        
        # Statistik sederhana
        if 'provinsi' in df.columns or 'province' in df.columns:
            prov_col = 'provinsi' if 'provinsi' in df.columns else 'province'
            st.subheader("📊 Per Provinsi")
            prov_count = df[prov_col].value_counts()
            st.bar_chart(prov_count.head(10))
    
    else:
        st.warning("⚠️ File angklung.csv tidak ditemukan!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>🇮🇩 <b>Dibuat untuk melestarikan budaya Indonesia</b> 🇮🇩</p>
    <p>Data angklung dari berbagai sumber | Peta menggunakan Leaflet.js</p>
</div>
""", unsafe_allow_html=True)