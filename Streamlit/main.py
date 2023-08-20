import streamlit as st
import math
from streamlit_option_menu import option_menu

# Navigasi Sidebar
with st.sidebar:
    selected = option_menu('Hitung Luas Bangun', ['Hitung Luas & Keliling Persegi Panjang', 'Hitung Luas & Keliling Persegi', 'Hitung Luas & Keliling Segitiga', 'Hitung Luas & Keliling Jajar Genjang', 'Hitung Luas & Keliling Trapesium', 'Hitung Luas & Keliling Layang-Layang', 'Hitung Luas & Keliling Belah Ketupat', 'Hitung Luas & Keliling Lingkaran'], default_index=0)

# Halaman Persegi Panjang
if (selected == 'Hitung Luas & Keliling Persegi Panjang'):
    st.title("Hitung Luas & Keliling Persegi Panjang")

    panjang = st.number_input("Panjang", 0.0)
    lebar = st.number_input("Lebar", 0.0)
    HitungPersegiPanjang = st.button("Hitung Luas")
    HitungPersegiPanjang2 = st.button("Hitung Keliling")

    if HitungPersegiPanjang:
        luas = panjang * lebar
        st.success(f"Luas Persegi Panjang Adalah = {luas}")

    if HitungPersegiPanjang2:
        keliing = 2 * (panjang + lebar)
        st.success(f"Keliling Persegi Panjang Adalah = {keliing}")

# Halaman Persegi
elif (selected == 'Hitung Luas & Keliling Persegi'):
    st.title("Hitung Luas & Keliling Persegi")

    sisi = st.number_input("Sisi", 0.0)
    HitungPersegi = st.button("Hitung Luas")
    HitungPersegi2 = st.button("Hitung Keliling")

    if HitungPersegi:
        luas = sisi * sisi
        st.success(f"Luas Persegi Adalah = {luas}")

    if HitungPersegi2:
        keliling = 4 * sisi
        st.success(f"Keliling Persegi Adalah = {keliling}")

# Halaman Segitiga
elif (selected == 'Hitung Luas & Keliling Segitiga'):
    st.title("Hitung Luas & Keliling Segitiga")

    alas = st.number_input("Alas", 0.0)
    tinggi = st.number_input("Tinggi", 0.0)
    HitungSegitiga = st.button("Hitung Luas")
    HitungSegitiga2 = st.button("Hitung Keliling")

    if HitungSegitiga:
        luas = 0.5 * alas * tinggi
        st.success(f"Luas Segitiga Adalah = {luas}")

    if HitungSegitiga2:
        keliling = 3 * alas  # Menggunakan formula sisi * sisi * sisi, tetapi Anda perlu memasukkan panjang sisi pada variabel alas
        st.success(f"Keliling Segitiga Adalah = {keliling}")

# Halaman Jajar Genjang
elif (selected == 'Hitung Luas & Keliling Jajar Genjang'):
    st.title("Hitung Luas & Keliling Jajar Genjang")

    alas = st.number_input("Alas", 0.0)
    tinggi = st.number_input("Tinggi", 0.0)
    sisi_miring = st.number_input("Sisi Miring", 0.0)
    HitungJajarGenjang = st.button("Hitung Luas")
    HitungJajarGenjang2 = st.button("Hitung Keliling")

    if HitungJajarGenjang:
        luas = alas * tinggi
        st.success(f"Luas Jajar Genjang Adalah = {luas}")

    if HitungJajarGenjang2:
        keliling = 2 * (alas + sisi_miring)
        st.success(f"Keliling Jajar Genjang Adalah = {keliling}")

# Halaman Trapesium
elif (selected == 'Hitung Luas & Keliling Trapesium'):
    st.title("Hitung Luas & Keliling Trapesium")

    alas1 = st.number_input("Alas Sejajar 1", 0.0)
    alas2 = st.number_input("Alas Sejajar 2", 0.0)
    tinggi = st.number_input("Tinggi", 0.0)
    sisi_miring = st.number_input("Sisi Miring (Jika Ada)", 0.0)
    HitungTrapesium = st.button("Hitung Luas")
    HitungTrapesium2 = st.button("Hitung Keliling")

    if HitungTrapesium:
        luas = 0.5 * (alas1 + alas2) * tinggi
        st.success(f"Luas Trapesium Adalah = {luas}")

    if HitungTrapesium2:
        keliling = alas1 + alas2 + 2 * sisi_miring  # Anda perlu menambahkan sisi_miring ke formula keliling
        st.success(f"Keliling Trapesium Adalah = {keliling}")

# Halaman Layang-Layang
elif (selected == 'Hitung Luas & Keliling Layang-Layang'):
    st.title("Hitung Luas & Keliling Layang-Layang")

    diagonal1 = st.number_input("Diagonal 1", 0.0)
    diagonal2 = st.number_input("Diagonal 2", 0.0)
    sisi1 = st.number_input("Sisi 1", 0.0)
    sisi2 = st.number_input("Sisi 2", 0.0)
    HitungLayangLayang = st.button("Hitung Luas")
    HitungLayangLayang2 = st.button("Hitung Keliling")

    if HitungLayangLayang:
        luas = 0.5 * diagonal1 * diagonal2
        st.success(f"Luas Layang-Layang Adalah = {luas}")

    if HitungLayangLayang2:
        keliling = 2 * (sisi1 + sisi2)
        st.success(f"Keliling Layang-Layang Adalah = {keliling}")

# Halaman Belah Ketupat
elif (selected == 'Hitung Luas & Keliling Belah Ketupat'):
    st.title("Hitung Luas & Keliling Belah Ketupat")

    diagonal1 = st.number_input("Diagonal 1", 0.0)
    diagonal2 = st.number_input("Diagonal 2", 0.0)
    sisi = st.number_input("Sisi", 0.0)
    HitungBelahKetupat = st.button("Hitung Luas")
    HitungBelahKetupat2 = st.button("Hitung Keliling")

    if HitungBelahKetupat:
        luas = 0.5 * diagonal1 * diagonal2
        st.success(f"Luas Belah Ketupat Adalah = {luas}")

    if HitungBelahKetupat2:
        keliling = 4 * sisi
        st.success(f"Keliling Belah Ketupat Adalah = {keliling}")

# Halaman Lingkaran
elif (selected == 'Hitung Luas & Keliling Lingkaran'):
    st.title("Hitung Luas & Keliling Lingkaran")

    jari_jari = st.number_input("Jari-Jari", 0.0)
    HitungLingkaran = st.button("Hitung Luas")
    HitungLingkaran2 = st.button("Hitung Keliling")

    if HitungLingkaran:
        luas = math.pi * jari_jari * jari_jari  # Ingat untuk mengimpor modul math di awal kode
        st.success(f"Luas Lingkaran Adalah = {luas}")

    if HitungLingkaran2:
        keliling = 2 * math.pi * jari_jari  # Ingat untuk mengimpor modul math di awal kode
        st.success(f"Keliling Lingkaran Adalah = {keliling}")
