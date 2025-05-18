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
cols_to_show = ['title', 'publish_date', 'sector_label', 'composite_label']

def set_col_width(df, widths):
    styles = []
    for i, col in enumerate(df.columns):
        width = widths.get(col, 150)  # default 150px jika kolom tidak dispesifikkan
        styles.append({
            'selector': f'th.col{i}',
            'props': [('min-width', f'{width}px'), ('max-width', f'{width}px')]
        })
        styles.append({
            'selector': f'td.col{i}',
            'props': [('min-width', f'{width}px'), ('max-width', f'{width}px')]
        })
    return df.style.set_table_styles(styles)

widths = {
    'title': 20,
    'publish_date': 12,
    'sector_label': 15,
    'composite_label': 12,
}

styled_df = set_col_width(data[cols_to_show], widths)
st.dataframe(styled_df)



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
