import streamlit as st
import pandas as pd

# Judul
st.title("Dashboard Klasifikasi Berita Pergerakan GDP Indonesia")

# Deskripsi
st.write("""
    Sistem ini mengklasifikasikan berita ekonomi untuk mendeteksi pergerakan GDP Indonesia. 
    Pengguna dapat melihat hasil klasifikasi pergerakan GDP berdasarkan sektor industri.
""")

# Memuat dan menampilkan data berita yang sudah diproses
data = pd.read_csv("dataset.csv")

# Menampilkan data berita
st.subheader("Data Berita Terkini")
st.dataframe(data)

# Pilihan untuk memilih kategori pergerakan GDP
gdp_category = st.selectbox("Pilih Kategori GDP:", ["Not Specified", "Year-on-Year", "Quarter-to-Quarter", "Cumulative"])

# Filter data berdasarkan kategori
filtered_data = data[data["Category"] == sector_label]
st.write(f"Menampilkan berita dengan kategori: {sector_label}")
st.dataframe(filtered_data)

# Menampilkan statistik klasifikasi
st.subheader("Hasil Klasifikasi")
accuracy = 0.88  # Angka contoh, Anda bisa mengganti ini dengan nilai aktual
precision = 0.85
recall = 0.80
f1_score = 0.82

st.write(f"Akurasinya: {accuracy}")
st.write(f"Precision: {precision}")
st.write(f"Recall: {recall}")
st.write(f"F1-Score: {f1_score}")
