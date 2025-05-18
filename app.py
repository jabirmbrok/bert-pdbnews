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

# Load data
data = pd.read_csv("dataset.csv")

# Mapping label prediksi
data['pdb_label'] = data['pdb_label'].map({1: 'Naik', -1: 'Turun'}).fillna('Tidak diketahui')

# Filter pilihan kategori GDP
gdp_category = st.selectbox("Pilih Kategori GDP:", ["Not Specified", "Year-on-Year", "Quarter-to-Quarter", "Cumulative"])
if gdp_category == "Not Specified":
    filtered_gdp = data.copy()
else:
    filtered_gdp = data[data['category'] == gdp_category]

# Filter pilihan sektor berdasarkan hasil filter kategori GDP
sector_label = st.selectbox("Pilih Sektor Industri:", options=filtered_gdp['sector_label'].dropna().unique())
filtered_data = filtered_gdp[filtered_gdp['sector_label'] == sector_label]

st.write(f"Menampilkan berita dengan kategori GDP: **{gdp_category}** dan sektor industri: **{sector_label}**")

cols_to_show = ['title', 'publish_date', 'sector_label', 'pdb_label']

# Setup AgGrid
gb = GridOptionsBuilder.from_dataframe(filtered_data[cols_to_show])
gb.configure_default_column(editable=False, groupable=False)

# Atur kolom dan lebar
gb.configure_column("title", width=300, header_name="Judul Berita")
gb.configure_column("publish_date", width=150, header_name="Tanggal")
gb.configure_column("sector_label", width=150, header_name="Kategori")
gb.configure_column("pdb_label", width=100, header_name="Prediksi")

# Styling untuk kolom prediksi
cellsytle_jscode = """
function(params) {
    if (params.value == 'Naik') {
        return {'color': 'white', 'backgroundColor': 'green'};
    } else if (params.value == 'Turun') {
        return {'color': 'white', 'backgroundColor': 'red'};
    } else {
        return {'color': 'black'};
    }
};
"""
gb.configure_column("pdb_label", cellStyle=cellsytle_jscode)

grid_options = gb.build()

# Tampilkan tabel interaktif
AgGrid(filtered_data[cols_to_show], gridOptions=grid_options, height=400)

# Statistik klasifikasi
st.subheader("Hasil Klasifikasi")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Akurasi", "88%")
col2.metric("Precision", "85%")
col3.metric("Recall", "80%")
col4.metric("F1-Score", "82%")
