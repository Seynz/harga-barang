import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Daftar Harga Toko",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 Daftar Harga")

# =========================
# DATA BARANG
# =========================

data = [
    # BERAS
    ["Beras", "Beras Curah", "1 Liter", 14000],
    ["Beras", "Beras BMW", "1 Karung (5 Kg)", 80000],
    ["Beras", "Beras Pokea", "1 Karung (5 Kg)", 85000],
    ["Beras", "Beras SPHP", "1 Karung (5 Kg)", 65000],
    ["Beras", "Beras Karung Bening", "25kg", 405000],
    

    # MINYAK
    ["Minyak Goreng", "Minyak Bimoli", "1 Liter", 28000],
    ["Minyak Goreng", "Minyak Sabrina", "900 ml", 25000],
    ["Minyak Goreng", "Minyak Fortune", "1 Liter", 28000],
    

    # GULA
    ["Gula", "Gula Aren", "1 Pasang", 20000],
    ["Gula", "Gula Aren", "1/2 Pasang", 10000],
    
    # TELUR
    ["Telur", "Telur Ayam", "1 Biji", 2000],
    ["Telur", "Telur Ayam", "1 Rak", 60000],

    # Tissue
    ["Tissue", "Larrist", "1 Bungkus", 10000],
    

    # Amplop
    ["Amplop", "Amplop Besar", "1 Lembar", 1000],
    ["Amplop", "Amplop Kecil", "1 Lembar", 500],

    #Gas
    ["Gas", "Gas 5 Kg", "1 Tabung", 32000],
    
]

df = pd.DataFrame(
    data,
    columns=["Kategori", "Nama Barang", "Ukuran", "Harga"]
)

# =========================
# FILTER
# =========================

col1, col2 = st.columns([1, 2])

with col1:
    kategori = st.selectbox(
        "Kategori",
        ["Semua"] + sorted(df["Kategori"].unique())
    )

with col2:
    cari = st.text_input(
        "Cari Barang",
        placeholder="Contoh: Beras, Minyak..."
    )

hasil = df.copy()

if kategori != "Semua":
    hasil = hasil[hasil["Kategori"] == kategori]

if cari:
    hasil = hasil[
        hasil["Nama Barang"].str.contains(cari, case=False)
    ]

hasil = hasil.sort_values(
    by=["Kategori", "Nama Barang", "Ukuran"]
).reset_index(drop=True)

st.markdown(f"### Ditemukan **{len(hasil)}** barang")

st.divider()

if len(hasil) == 0:
    st.warning("Barang tidak ditemukan.")
else:
    for _, row in hasil.iterrows():

        harga = f"Rp {row['Harga']:,}".replace(",", ".")

        with st.container(border=True):

            col1, col2 = st.columns([4,1])

            with col1:
                st.markdown(f"### {row['Nama Barang']}")
                st.caption(row["Kategori"])

                st.write(f"📦 **Ukuran:** {row['Ukuran']}")

            with col2:
                st.markdown("### 💰")
                st.markdown(f"**{harga}**")

st.caption("Terakhir diperbarui: 28 Juni 2026")
