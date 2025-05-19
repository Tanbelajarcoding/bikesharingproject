import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
hour = pd.read_csv("bikedataset.csv")

# Preprocess data
hour['tanggal'] = pd.to_datetime(hour['tanggal'])
hour['musim'] = hour['musim'].replace({
    1: 'Musim Semi', 2: 'Musim Panas', 3: 'Musim Gugur', 4: 'Musim Dingin'
})
hour['bulan'] = hour['bulan'].replace({
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'Mei', 6: 'Jun',
    7: 'Jul', 8: 'Agu', 9: 'Sep', 10: 'Okt', 11: 'Nov', 12: 'Des'
})

# -------------------------------
# Function to display Question 3: Impact of weather variables on rentals
# -------------------------------
def question_3_plot():
    st.header("Pengaruh Cuaca terhadap Penyewa Sepeda")

    # Sidebar Filters
    weather_filter = st.sidebar.selectbox("Pilih Cuaca", ["Cerah/Berawan Sebagian", "Berkabut/Berawan", "Hujan/Salju Ringan", "Cuaca Ekstrem"], index=0)

    # Date Range Filter
    min_date = hour['tanggal'].min()
    max_date = hour['tanggal'].max()
    start_date, end_date = st.sidebar.date_input("Pilih Rentang Tanggal", [min_date, max_date])

    # Filter data based on selected date range and other filters
    filtered_data = hour[
        (hour['tanggal'] >= pd.to_datetime(start_date)) &
        (hour['tanggal'] <= pd.to_datetime(end_date)) &
        (hour['situasi_cuaca'] == weather_filter)
    ]

    # Handle empty data
    if filtered_data.empty:
        st.warning("Tidak ada data yang sesuai dengan filter yang dipilih.")
        return

    # --- Create the plots ---
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # --- Windspeed vs. Rentals ---
    sns.scatterplot(x='kecepatan_angin', y='jumlah', data=filtered_data, alpha=0.5, color="tomato", ax=axes[0])
    sns.regplot(x='kecepatan_angin', y='jumlah', data=filtered_data, scatter=False, color="black", order=2, ax=axes[0])
    axes[0].set_title('Dampak Kecepatan Angin terhadap Penyewaan Sepeda')
    axes[0].set_xlabel('Kecepatan Angin')
    axes[0].set_ylabel('Jumlah Penyewaan')

    # --- Temperature vs. Rentals ---
    sns.scatterplot(x='suhu_terasa', y='jumlah', data=filtered_data, alpha=0.5, color="royalblue", ax=axes[1])
    sns.regplot(x='suhu_terasa', y='jumlah', data=filtered_data, scatter=False, color="blue", lowess=True, ax=axes[1])
    axes[1].set_title('Dampak Suhu terhadap Penyewaan Sepeda')
    axes[1].set_xlabel('Suhu Terasa')
    axes[1].set_ylabel('Jumlah Penyewaan')

    # --- Humidity vs. Rentals ---
    sns.scatterplot(x='kelembaban', y='jumlah', data=filtered_data, alpha=0.5, color="seagreen", ax=axes[2])
    sns.regplot(x='kelembaban', y='jumlah', data=filtered_data, scatter=False, color="green", lowess=True, ax=axes[2])
    axes[2].set_title('Dampak Kelembaban terhadap Penyewaan Sepeda')
    axes[2].set_xlabel('Kelembaban')
    axes[2].set_ylabel('Jumlah Penyewaan')

    plt.tight_layout()
    st.pyplot(fig)


# -------------------------------
# Function to display Question 1: Weather and working day influence
# -------------------------------
def question_1_plot():
    st.header("Pengaruh Cuaca dan Hari Kerja terhadap Penyewa Sepeda")

    # Sidebar Filters
    season_filter = st.sidebar.multiselect("Pilih Musim", ["Musim Semi", "Musim Panas", "Musim Gugur", "Musim Dingin"], default=["Musim Semi", "Musim Panas", "Musim Gugur", "Musim Dingin"])
    weather_filter = st.sidebar.multiselect("Pilih Situasi Cuaca", ["Cerah/Berawan Sebagian", "Berkabut/Berawan", "Hujan/Salju Ringan", "Cuaca Ekstrem"], default=["Cerah/Berawan Sebagian", "Berkabut/Berawan", "Hujan/Salju Ringan", "Cuaca Ekstrem"])

    # Date Range Filter
    min_date = hour['tanggal'].min()
    max_date = hour['tanggal'].max()
    start_date, end_date = st.sidebar.date_input("Pilih Rentang Tanggal", [min_date, max_date])

    # Filter data based on selected date range and other filters
    filtered_data = hour[
        (hour['tanggal'] >= pd.to_datetime(start_date)) &
        (hour['tanggal'] <= pd.to_datetime(end_date)) &
        hour['musim'].isin(season_filter) &
        hour['situasi_cuaca'].isin(weather_filter)
    ]

    # Create plot for working day vs user preference
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    sns.boxplot(data=filtered_data, x='hari_kerja', y='penyewa_casual', ax=axes[0, 0], palette="coolwarm")
    axes[0, 0].set_title("Pengaruh Hari Kerja terhadap Penyewa Casual")
    sns.boxplot(data=filtered_data, x='hari_kerja', y='penyewa_terdaftar', ax=axes[0, 1], palette="coolwarm")
    axes[0, 1].set_title("Pengaruh Hari Kerja terhadap Penyewa Terdaftar")
    sns.boxplot(data=filtered_data, x='situasi_cuaca', y='penyewa_casual', ax=axes[1, 0], palette="Blues")
    axes[1, 0].set_title("Pengaruh Cuaca terhadap Penyewa Casual")
    sns.boxplot(data=filtered_data, x='situasi_cuaca', y='penyewa_terdaftar', ax=axes[1, 1], palette="Blues")
    axes[1, 1].set_title("Pengaruh Cuaca terhadap Penyewa Terdaftar")

    plt.tight_layout()
    st.pyplot(fig)

# -------------------------------
# Function to display Question 2: Rental percentage patterns
# -------------------------------
def question_2_plot():
    st.header("Pola Persentase Penyewaan Sepeda")

    # Sidebar Filters
    season_filter = st.sidebar.multiselect("Pilih Musim", ["Musim Semi", "Musim Panas", "Musim Gugur", "Musim Dingin"], default=["Musim Semi", "Musim Panas", "Musim Gugur", "Musim Dingin"])

    # Date Range Filter
    min_date = hour['tanggal'].min()
    max_date = hour['tanggal'].max()
    start_date, end_date = st.sidebar.date_input("Pilih Rentang Tanggal", [min_date, max_date])

    # Filter data based on selected date range and other filters
    filtered_data = hour[
        (hour['tanggal'] >= pd.to_datetime(start_date)) &
        (hour['tanggal'] <= pd.to_datetime(end_date)) &
        hour['musim'].isin(season_filter)
    ]

    # Group data by month and year for rental percentage
    filtered_data['tahun_bulan'] = filtered_data['tanggal'].dt.strftime('%b %Y')
    date_df = filtered_data.groupby("tahun_bulan").agg({
        "penyewa_casual": "sum",
        "penyewa_terdaftar": "sum",
        "jumlah": "sum"
    }).reset_index()
    date_df['persentase_casual'] = (date_df['penyewa_casual'] / date_df['jumlah']) * 100
    date_df['persentase_terdaftar'] = (date_df['penyewa_terdaftar'] / date_df['jumlah']) * 100

    # Plot rental percentage over time
    plt.figure(figsize=(12, 8))
    plt.barh(date_df['tahun_bulan'], date_df['persentase_casual'], label="Casual", color="lightblue", alpha=0.8)
    plt.barh(date_df['tahun_bulan'], date_df['persentase_terdaftar'], left=date_df['persentase_casual'], label="Terdaftar", color="salmon", alpha=0.8)
    plt.title("Proporsi Penyewaan Sepeda: Casual vs Terdaftar")
    plt.xlabel("Persentase Penyewaan (%)")
    plt.ylabel("Bulan dan Tahun")
    plt.legend()
    plt.grid(axis='x', linestyle="dashed", alpha=0.7)
    st.pyplot()

# -------------------------------
# New Additional Analysis: Summer vs Winter Rentals and Temperature Impact
# -------------------------------
def summer_winter_analysis():
    st.header("Analisis Lanjutan: Penggunaan Sepeda di Musim Panas dan Musim Dingin")

    # Sidebar Filters
    season_filter = st.sidebar.selectbox("Pilih Musim", ["Musim Panas", "Musim Dingin", "Gabungan Musim Panas dan Dingin"], index=0)

    # Filter data based on selected season
    if season_filter == "Gabungan Musim Panas dan Dingin":
        filtered_data = hour[hour['musim'].isin(['Musim Panas', 'Musim Dingin'])]
    else:
        filtered_data = hour[hour['musim'] == season_filter]

    # Scatter plot: Temperature vs Bike Rentals by Season (Summer and Winter)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        x='suhu_terasa',
        y='jumlah',
        data=filtered_data,
        hue='musim',
        alpha=0.5,
        palette={"Musim Panas": "red", "Musim Dingin": "blue"}
    )

    plt.title('Distribusi Penyewaan Berdasarkan Musim (Musim Panas & Musim Dingin)', fontsize=14)
    plt.xlabel('Suhu yang Dirasakan (°C)', fontsize=12)
    plt.ylabel('Jumlah Penyewaan Sepeda', fontsize=12)
    plt.grid(True, linestyle="dashed", alpha=0.6)
    st.pyplot()

# -------------------------------
# Sidebar Configuration
# -------------------------------
st.sidebar.title("Dashboard Penyewaan Sepeda")

# Moved analysis selection to the sidebar
tabs = st.sidebar.radio("Pilih Analisis", ["Analisis 1: Pengaruh Cuaca & Hari Kerja", "Analisis 2: Persentase Penyewaan", "Analisis 3: Cuaca dan Penyewaan", "Analisis Lanjutan: Musim Panas vs Musim Dingin"])

# -------------------------------
# Main Layout with Content Based on Sidebar Analysis
# -------------------------------
if tabs == "Analisis 1: Pengaruh Cuaca & Hari Kerja":
    question_1_plot()
elif tabs == "Analisis 2: Persentase Penyewaan":
    question_2_plot()
elif tabs == "Analisis 3: Cuaca dan Penyewaan":
    question_3_plot()
elif tabs == "Analisis Lanjutan: Musim Panas vs Musim Dingin":
    summer_winter_analysis()

# Footer with developer info
st.markdown("---")
st.caption("**Developed by Sulthan Muhammad Rafif Ilham | Contact: sulthanrafif@student.ub.ac.id | GitHub: (https://github.com/Tanbelajarcoding)**")
