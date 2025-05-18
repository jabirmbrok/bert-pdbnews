import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

st.title("Dashboard Klasifikasi Berita Pergerakan GDP Indonesia")

data = pd.read_csv("dataset.csv")
data['pdb_label'] = data['pdb_label'].map({1: 'Naik', -1: 'Turun'}).fillna('Tidak diketahui')

sector_label = st.selectbox("Pilih Sektor Industri:", options=data['sector_label'].dropna().unique())
filtered_data = data[data['sector_label'] == sector_label].copy()

def label_with_color(x):
    if x == 'Naik':
        return "🟢 Naik"
    elif x == 'Turun':
        return "🔴 Turun"
    else:
        return x

filtered_data['pdb_label_color'] = filtered_data['pdb_label'].apply(label_with_color)

cols_to_show = ['title', 'publish_date', 'sector_label', 'pdb_label_color']
data1 = filtered_data[cols_to_show].copy()
data1.reset_index(drop=True, inplace=True)

gb = GridOptionsBuilder.from_dataframe(data1)
gb.configure_default_column(editable=False, groupable=False)
gb.configure_column("title", width=300, header_name="Judul Berita")
gb.configure_column("publish_date", width=150, header_name="Tanggal Terbit")
gb.configure_column("sector_label", width=150, header_name="Sektor Industri")
gb.configure_column("pdb_label_color", width=120, header_name="Prediksi")

grid_options = gb.build()

AgGrid(data1, gridOptions=grid_options, height=400)

st.subheader("Hasil Klasifikasi")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Akurasi", "88%")
col2.metric("Precision", "85%")
col3.metric("Recall", "80%")
col4.metric("F1-Score", "82%")
