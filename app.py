import streamlit as st
import streamlit.components.v1 as components
import os

# Konfigurasi halaman
st.set_page_config(
    page_title="Peta Angklung Indonesia",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Baca dan tampilkan HTML file
html_file_path = "peta_angklung_final.html"

if os.path.exists(html_file_path):
    try:
        # Baca file HTML
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Tampilkan HTML dalam Streamlit dengan tinggi penuh
        components.html(html_content, height=800, scrolling=True)
        
    except Exception as e:
        st.error(f"Error loading HTML file: {e}")
    
else:
    st.error("File peta_angklung_final.html tidak ditemukan!")
    st.info("Pastikan file HTML ada di folder yang sama dengan aplikasi ini.")