import streamlit as st
import pandas as pd

st.title("Dashboard Klasifikasi Berita Pergerakan GDP Indonesia")

# Load data
data = pd.read_csv("dataset.csv")
data['pdb_label'] = data['pdb_label'].map({1: 'Naik', -1: 'Turun'}).fillna('Tidak diketahui')

sector_label = st.selectbox("Pilih Sektor Industri:", options=data['sector_label'].dropna().unique())
filtered_data = data[data['sector_label'] == sector_label].copy()

cols_to_show = ['title', 'publish_date', 'sector_label', 'pdb_label']
data1 = filtered_data[cols_to_show].copy()

# Fungsi untuk highlight warna baris berdasarkan nilai kolom pdb_label
def highlight_pdb_label(row):
    color = ''
    if row['pdb_label'] == 'Naik':
        color = 'background-color: green; color: white;'
    elif row['pdb_label'] == 'Turun':
        color = 'background-color: red; color: white;'
    else:
        color = ''
    return [color] * len(row)

styled_df = data1.style.apply(highlight_pdb_label, axis=1)

st.dataframe(styled_df, height=400)

st.subheader("Hasil Klasifikasi")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Akurasi", "88%")
col2.metric("Precision", "85%")
col3.metric("Recall", "80%")
col4.metric("F1-Score", "82%")
