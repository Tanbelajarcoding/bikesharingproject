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
    tab1, tab2, tab3, tab4 = st.tabs(["Spring", "Summer", "Fall", "Winter"])
    with tab1:
        filtered_hour = hour[hour['season'].isin(['Spring'])]
    
        fig = plt.figure(figsize=(10, 6))
        sns.scatterplot(data=filtered_hour, x='humidity', y='count', alpha=0.6, color='blue')
        plt.title('Hubungan antara Kelembapan (Humidity) dan Jumlah Penyewaan Sepeda pada Musim Semi', fontsize=14)
        plt.xlabel('Kelembapan (Humidity)', fontsize=12)
        plt.ylabel('Jumlah Penyewaan Sepeda (cnt)', fontsize=12)
        plt.grid(True)
        st.pyplot(fig)    
    with tab2:
        filtered_hour = hour[hour['season'].isin(['Summer'])]
    
        fig = plt.figure(figsize=(10, 6))
        sns.scatterplot(data=filtered_hour, x='humidity', y='count', alpha=0.6, color='blue')
        plt.title('Hubungan antara Kelembapan (Humidity) dan Jumlah Penyewaan Sepeda pada Musim Panas', fontsize=14)
        plt.xlabel('Kelembapan (Humidity)', fontsize=12)
        plt.ylabel('Jumlah Penyewaan Sepeda (cnt)', fontsize=12)
        plt.grid(True)
        st.pyplot(fig) 
    with tab3:
        filtered_hour = hour[hour['season'].isin(['Fall'])]
    
        fig = plt.figure(figsize=(10, 6))
        sns.scatterplot(data=filtered_hour, x='humidity', y='count', alpha=0.6, color='blue')
        plt.title('Hubungan antara Kelembapan (Humidity) dan Jumlah Penyewaan Sepeda pada Musim Gugur', fontsize=14)
        plt.xlabel('Kelembapan (Humidity)', fontsize=12)
        plt.ylabel('Jumlah Penyewaan Sepeda (cnt)', fontsize=12)
        plt.grid(True)
        st.pyplot(fig) 
    with tab4:
        filtered_hour = hour[hour['season'].isin(['Winter'])]
    
        fig = plt.figure(figsize=(10, 6))
        sns.scatterplot(data=filtered_hour, x='humidity', y='count', alpha=0.6, color='blue')
        plt.title('Hubungan antara Kelembapan (Humidity) dan Jumlah Penyewaan Sepeda pada Musim Dingin', fontsize=14)
        plt.xlabel('Kelembapan (Humidity)', fontsize=12)
        plt.ylabel('Jumlah Penyewaan Sepeda (cnt)', fontsize=12)
        plt.grid(True)
        st.pyplot(fig) 

if analysis_option == "Perbandingan Jumlah Penyewaan Sepeda pada Hari Libur dan Hari Kerja":
    st.header("Perbandingan Jumlah Penyewaan Sepeda pada Hari Libur dan Hari Kerja")
   
    holiday_data = hour.groupby('holiday')['count'].mean()
    
    fig = plt.figure(figsize=(8, 6))
    sns.barplot(x=holiday_data.index, y=holiday_data.values, palette="Blues_d")
    plt.title('Perbandingan Jumlah Penyewaan Sepeda pada Hari Libur dan Hari Kerja', fontsize=14)
    plt.xlabel('Hari Libur (0: Bukan Libur, 1: Libur)', fontsize=12)
    plt.ylabel('Rata-rata Jumlah Penyewaan Sepeda (cnt)', fontsize=12)
    plt.xticks([0, 1], ['Bukan Libur', 'Libur'])
    plt.grid(True)
    st.pyplot(fig)

if analysis_option == "pola penggunaan sepeda pada musim panas dan musim dingin":
    st.header("pola penggunaan sepeda pada musim panas dan musim dingin")
    tab1, tab2, tab3 = st.tabs(["Summer & Winter", "Summer", "Winter"])
    with tab1:
        fig = plt.figure(figsize=(10, 6))
        
        filtered_hour = hour[hour['season'].isin(['Summer', 'Winter'])]
        
        sns.scatterplot(
            x='atemp',
            y='count',
            data=filtered_hour,
            hue='season',
            alpha=0.5
        )
        
        plt.title('Distribusi Penjualan Berdasarkan Musim Panas & Dingin')
        plt.xlabel('Suhu yang dirasakan')
        plt.ylabel('Jumlah Penjualan')
        
        st.pyplot(fig)
        
    with tab2:
        fig = plt.figure(figsize=(10, 6))
        
        filtered_hour = hour[hour['season'].isin(['Summer'])]
        
        sns.scatterplot(
            x='atemp',
            y='count',
            data=filtered_hour,
            hue='season',
            alpha=0.5
        )
        
        plt.title('Distribusi Penjualan Berdasarkan Musim Panas')
        plt.xlabel('Suhu yang dirasakan')
        plt.ylabel('Jumlah Penjualan')
        
        st.pyplot(fig)
           
        with tab3:
        fig = plt.figure(figsize=(10, 6))
        
        filtered_hour = hour[hour['season'].isin(['Winter'])]
        
        sns.scatterplot(
            x='atemp',
            y='count',
            data=filtered_hour,
            hue='season',
            alpha=0.5
        )
        
        plt.title('Distribusi Penjualan Berdasarkan Musim Dingin')
        plt.xlabel('Suhu yang dirasakan')
        plt.ylabel('Jumlah Penjualan')
        
        st.pyplot(fig)
