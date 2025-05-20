# Dashboard Penyewaan Sepeda ✨

Proyek ini adalah aplikasi interaktif yang memungkinkan pengguna untuk menganalisis data penyewaan sepeda menggunakan Streamlit. Aplikasi ini memberikan insight tentang berbagai faktor yang mempengaruhi pola penyewaan sepeda, termasuk kondisi cuaca, musim, dan hari kerja. Dashboard ini menyajikan visualisasi yang menarik untuk memahami hubungan antara cuaca, suhu, kelembaban, kecepatan angin, dan faktor lainnya terhadap penyewaan sepeda.

## Setup Environment

Untuk menjalankan proyek ini, Anda perlu mengatur lingkungan pengembangan sesuai dengan instruksi berikut.

### Setup Environment - Anaconda
Jika Anda menggunakan Anaconda, ikuti langkah-langkah berikut untuk membuat lingkungan baru:

1. Buat lingkungan virtual baru dengan Python 3.9:
    ```bash
    conda create --name main-ds python=3.9
    ```

2. Aktivasi lingkungan:
    ```bash
    conda activate main-ds
    ```

3. Instal semua dependensi dari berkas `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

### Setup Environment - Shell/Terminal
Jika Anda menggunakan terminal atau shell biasa, lakukan langkah-langkah berikut:

1. Buat direktori proyek dan masuk ke dalamnya:
    ```bash
    mkdir Bike-Sharing-Project
    cd Bike-Sharing-Project
    ```

2. Instal `pipenv` untuk manajemen virtual environment:
    ```bash
    pipenv install
    pipenv shell
    ```

3. Instal dependensi yang dibutuhkan:
    ```bash
    pip install -r requirements.txt
    ```

## Menjalankan Aplikasi Streamlit

Setelah semua dependensi terinstal, Anda bisa menjalankan aplikasi Streamlit dengan perintah berikut:

```bash
streamlit run dashboard.py
