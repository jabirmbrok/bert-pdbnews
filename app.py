import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

st.title("Dashboard Klasifikasi Berita Pergerakan GDP Indonesia")

st.write("""
    Sistem ini mengklasifikasikan berita ekonomi untuk mendeteksi pergerakan GDP Indonesia. 
    Pengguna dapat melihat hasil klasifikasi pergerakan GDP berdasarkan sektor industri.
""")

data = pd.read_csv("dataset.csv")

# Pilih sektor industri
sector_label = st.selectbox("Pilih Sektor Industri:", options=data['sector_label'].dropna().unique())
filtered_data = data[data['sector_label'] == sector_label].copy()

# Mapping prediksi sebelum subset kolom dan AgGrid
filtered_data['pdb_label'] = filtered_data['pdb_label'].map({1: 'Naik', -1: 'Turun'}).fillna('Tidak diketahui')

cols_to_show = ['title', 'publish_date', 'sector_label', 'pdb_label']
data1 = filtered_data[cols_to_show].reset_index(drop=True)

gb = GridOptionsBuilder.from_dataframe(data1)
gb.configure_default_column(editable=False, groupable=False)

# Atur lebar kolom yang realistis
gb.configure_column("title", width=300, header_name="Judul Berita")
gb.configure_column("publish_date", width=150, header_name="Tanggal")
gb.configure_column("sector_label", width=150, header_name="Kategori")
gb.configure_column("pdb_label", width=100, header_name="Prediksi")

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

AgGrid(data1, gridOptions=grid_options, height=400)

# Statistik klasifikasi
st.subheader("Hasil Klasifikasi")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Akurasi", "88%")
col2.metric("Precision", "85%")
col3.metric("Recall", "80%")
col4.metric("F1-Score", "82%")
