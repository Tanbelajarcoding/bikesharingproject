# Import library yang digunakan untuk analisis data dan visualisasi
import pandas as pd         # Untuk manipulasi dan analisis data
import numpy as np          # Untuk operasi numerik dan manipulasi data
import matplotlib.pyplot as plt  # Untuk visualisasi grafik
import seaborn as sns       # Untuk visualisasi statistik
import streamlit as st      # Untuk streamlit

# -------------------------------
# Load Data
# -------------------------------
hour = pd.read_csv("https://raw.githubusercontent.com/Tanbelajarcoding/bikesharingproject/refs/heads/main/Dashboard/hour_df.csv")
# -------------------------------
# Sidebar: Filter dan Pilihan Analisis
# -------------------------------
st.sidebar.header("Filter Data")
analysis_option = st.sidebar.radio("Pilih Analisis", ("Hubungan Humidity dan Jumlah Penyewaan Sepeda pada Musim Panas", "Perbandingan Jumlah Penyewaan Sepeda pada Hari Libur dan Hari Kerja", "pola penggunaan sepeda pada musim panas dan musim dingin"))

# -------------------------------
# Header
# -------------------------------
st.header('Dashboard Penyewaan Sepeda :sparkles:')
st.caption("Last updated: 1 January 2013")

# -------------------------------
# Overview Data
# -------------------------------
if analysis_option == "Hubungan Humidity dan Jumlah Penyewaan Sepeda pada Musim Panas":
    st.header("Hubungan Humidity dan Jumlah Penyewaan Sepeda pada Musim Panas")
    
    filtered_hour = hour[hour['season'].isin(['Summer'])]

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=filtered_hour, x='humidity', y='count', alpha=0.6, color='blue')
    plt.title('Hubungan antara Kelembapan (Humidity) dan Jumlah Penyewaan Sepeda pada Musim Panas', fontsize=14)
    plt.xlabel('Kelembapan (Humidity)', fontsize=12)
    plt.ylabel('Jumlah Penyewaan Sepeda (cnt)', fontsize=12)
    plt.grid(True)
    plt.show()
    

