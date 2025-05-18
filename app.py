import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

# Judul
st.title("Dashboard Klasifikasi Berita Pergerakan GDP Indonesia")

# Deskripsi
st.write("""
    Sistem ini mengklasifikasikan berita ekonomi untuk mendeteksi pergerakan GDP Indonesia. 
    Pengguna dapat melihat hasil klasifikasi pergerakan GDP berdasarkan sektor industri.
""")

# Load data
data = pd.read_csv("dataset.csv")

# Map label prediksi
data['pdb_label'] = data['pdb_label'].map({1: 'Naik', -1: 'Turun'}).fillna('Tidak diketahui')

# Filter kategori GDP
gdp_category = st.selectbox("Pilih Kategori GDP:", ["Not Specified", "Year-on-Year", "Quarter-to-Quarter", "Cumulative"])
if gdp_category == "Not Specified":
    filtered_gdp = data.copy()
else:
    filtered_gdp = data[data['category'] == gdp_category]

# Filter sektor berdasarkan hasil filter kategori GDP
sector_label = st.selectbox("Pilih Sektor Industri:", options=filtered_gdp['sector_label'].dropna().unique())
filtered_data = filtered_gdp[filtered_gdp['sector_label'] == sector_label]

cols_to_show = ['title', 'publish_date', 'sector_label', 'pdb_label']
df_to_show = filtered_data[cols_to_show].copy()
df_to_show = df_to_show.reset_index(drop=True)

# Tampilkan AgGrid tanpa konfigurasi styling kompleks dulu
AgGrid(df_to_show, height=400)

# Statistik klasifikasi (contoh nilai)
st.subheader("Hasil Klasifikasi")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Akurasi", "88%")
col2.metric("Precision", "85%")
col3.metric("Recall", "80%")
col4.metric("F1-Score", "82%")
