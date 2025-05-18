import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

# Judul
st.title("Dashboard Klasifikasi Berita Pergerakan GDP Indonesia")

# Load data
data = pd.read_csv("dataset.csv")
data['pdb_label'] = data['pdb_label'].map({1: 'Naik', -1: 'Turun'}).fillna('Tidak diketahui')

# Filter sektor
sector_label = st.selectbox("Pilih Sektor Industri:", options=data['sector_label'].dropna().unique())
filtered_data = data[data['sector_label'] == sector_label].copy()

cols_to_show = ['title', 'publish_date', 'sector_label', 'pdb_label']
data1 = filtered_data[cols_to_show].copy()
data1.reset_index(drop=True, inplace=True)

gb = GridOptionsBuilder.from_dataframe(data1)
gb.configure_default_column(editable=False, groupable=False)

gb.configure_column("title", width=300, header_name="Judul Berita")
gb.configure_column("publish_date", width=150, header_name="Tanggal Terbit")
gb.configure_column("sector_label", width=150, header_name="Sektor Industri")
gb.configure_column("pdb_label", width=100, header_name="Prediksi")

# Gunakan cellClassRules untuk styling berdasarkan nilai sel
cell_class_rules = {
    "cell-green": "x == 'Naik'",
    "cell-red": "x == 'Turun'"
}
gb.configure_column("pdb_label", cellClassRules=cell_class_rules)

grid_options = gb.build()

# Tambahkan CSS custom untuk cell-green dan cell-red
st.markdown(
    """
    <style>
    .ag-theme-streamlit .cell-green {
        background-color: green !important;
        color: white !important;
    }
    .ag-theme-streamlit .cell-red {
        background-color: red !important;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

AgGrid(data1, gridOptions=grid_options, height=400)

# Statistik klasifikasi
st.subheader("Hasil Klasifikasi")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Akurasi", "88%")
col2.metric("Precision", "85%")
col3.metric("Recall", "80%")
col4.metric("F1-Score", "82%")
