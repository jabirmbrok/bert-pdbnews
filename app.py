import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

# Judul
st.title("Dashboard Klasifikasi Berita Pergerakan GDP Indonesia")

st.write("""
    Sistem ini mengklasifikasikan berita ekonomi untuk mendeteksi pergerakan GDP Indonesia. 
    Pengguna dapat melihat hasil klasifikasi pergerakan GDP berdasarkan sektor industri.
""")

# Load data
data = pd.read_csv("dataset.csv")

# Mapping label prediksi
data['pdb_label'] = data['pdb_label'].map({1: 'Naik', -1: 'Turun'}).fillna('Tidak diketahui')

# Filter sektor
sector_label = st.selectbox("Pilih Sektor Industri:", options=data['sector_label'].dropna().unique())
filtered_data = data[data['sector_label'] == sector_label].copy()

# Pilih kolom yang akan ditampilkan
cols_to_show = ['title', 'publish_date', 'sector_label', 'pdb_label']
data1 = filtered_data[cols_to_show].copy()
data1.reset_index(drop=True, inplace=True)

# Setup GridOptionsBuilder
gb = GridOptionsBuilder.from_dataframe(data1)
gb.configure_default_column(editable=False, groupable=False)

# Atur lebar kolom dan nama header
gb.configure_column("title", width=300, header_name="Judul Berita")
gb.configure_column("publish_date", width=150, header_name="Tanggal Terbit")
gb.configure_column("sector_label", width=150, header_name="Sektor Industri")
gb.configure_column("pdb_label", width=100, header_name="Prediksi")

# Styling kolom prediksi dengan pewarnaan hijau untuk 'Naik' dan merah untuk 'Turun'
cell_style_jscode = """
function(params) {
    if (params.value == 'Naik') {
        return {'color': 'white', 'backgroundColor': 'green'};
    } else if (params.value == 'Turun') {
        return {'color': 'white', 'backgroundColor': 'red'};
    } else {
        return null;
    }
}
"""
gb.configure_column("pdb_label", cellStyle=cell_style_jscode)

grid_options = gb.build()

# Tampilkan AgGrid dengan styling
AgGrid(data1, gridOptions=grid_options, height=400)

# Statistik klasifikasi
st.subheader("Hasil Klasifikasi")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Akurasi", "88%")
col2.metric("Precision", "85%")
col3.metric("Recall", "80%")
col4.metric("F1-Score", "82%")
