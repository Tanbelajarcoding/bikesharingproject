# Import library yang digunakan untuk analisis data dan visualisasi
import pandas as pd         # Untuk manipulasi dan analisis data
import numpy as np          # Untuk operasi numerik dan manipulasi data
import matplotlib.pyplot as plt  # Untuk visualisasi grafik
import seaborn as sns       # Untuk visualisasi statistik
import streamlit as st      # Untuk streamlit

# -------------------------------
# Load Data
# -------------------------------
hour = pd.read_csv("https://raw.githubusercontent.com/Tanbelajarcoding/bikesharingproject/refs/heads/main/Data/hour.csv")
# -------------------------------
# Sidebar: Filter dan Pilihan Analisis
# -------------------------------
st.sidebar.header("Filter Data")
analysis_option = st.sidebar.radio("Pilih Analisis", ("Overview Data", "Analisis per Jam", "Tren Bulanan", "Peak Season"))

# -------------------------------
# Header
# -------------------------------
st.header('Dashboard Penyewaan Sepeda :sparkles:')
st.caption("Last updated: 1 January 2013")

# -------------------------------
# Overview Data
# -------------------------------
if analysis_option == "Overview Data":
    st.header("Overview Data")
    st.subheader('Total Penyewaan')

