import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

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
#cols_to_show = ['title', 'publish_date', 'sector_label', 'composite_label']
#st.dataframe(data[cols_to_show])


# Buat grid options untuk atur lebar kolom
gb = GridOptionsBuilder.from_dataframe(data[cols_to_show])
gb.configure_default_column(editable=False, groupable=False)

# Contoh atur lebar kolom spesifik (dalam pixel)
gb.configure_column("title", width=30)
gb.configure_column("publish_date", width=15)
gb.configure_column("sector_label", width=15)
gb.configure_column("composite_label", width=12)
grid_options = gb.build()

# Tampilkan AgGrid
AgGrid(data, gridOptions=grid_options, height=400)

# Pilihan untuk memilih kategori pergerakan GDP
gdp_category = st.selectbox("Pilih Kategori GDP:", ["Not Specified", "Year-on-Year", "Quarter-to-Quarter", "Cumulative"])

# Filter data berdasarkan kategori
sector_label = st.selectbox("Pilih Sektor Industri:", options=data['sector_label'].dropna().unique())
filtered_data = data[data['sector_label'] == sector_label]

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
