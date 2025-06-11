# Pemodelan dan Peramalan Volatilitas Harga Minyak Mentah Menggunakan Model ARIMA dan GARCH
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/release/python-3130/)
[![On Progress](https://img.shields.io/badge/Status-On%20Progress-yellow.svg)](https://github.com/zakizulham/proyek-peramalan-global-comodity-price-september-2024/graphs/commit-activity)
[![License: MIT](https://img.shields.io/badge/License-MIT-darkgreen.svg)](https://opensource.org/licenses/MIT)

Repositori ini berisi kode dan data untuk proyek akhir mata kuliah Metode Peramalan, yang mengimplementasikan model ARIMA dan GARCH untuk menganalisis dan memprediksi harga minyak mentah (Crude Oil) WTI.

**[Deskripsi](#Deskripsi)** | **[Struktur Repository](#Struktur)** | **[Reproduksi Hasil](#Reproduksi)** | **[Ringkasan Proyek](#Ringkasan)** | **[Lisensi](#Lisensi)** 

## Deskripsi Proyek <a id='Deskripsi'></a>

Proyek ini bertujuan untuk membangun model peramalan deret waktu untuk memprediksi volatilitas harga minyak mentah WTI, salah satu komoditas paling strategis dalam perekonomian global. Harga minyak mentah dikenal sangat fluktuatif akibat pengaruh faktor geopolitik, kebijakan OPEC, dan krisis ekonomi global. Mengingat karakteristik tersebut, data harga minyak mentah seringkali menunjukkan sifat non-stasioner dan heteroskedastisitas (varians yang tidak konstan).

Untuk mengatasi tantangan ini, proyek ini mengimplementasikan pendekatan pemodelan ganda:
1. **Model ARIMA (Autoregressive Integrated Moving Average)**: Digunakan untuk memodelkan komponen rata-rata (mean) dari deret waktu harga setelah melalui proses diferensiasi untuk mencapai stasioneritas.
2. **Model GARCH (Generalized Autoregressive Conditional Heteroskedasticity)**: Diterapkan pada residual dari model ARIMA untuk memodelkan volatilitas atau varians yang berubah seiring waktu.

Tujuan utama dari proyek ini adalah:

- Menerapkan model forecasting time series gabungan (ARIMA-GARCH) untuk memodelkan dan memprediksi harga Crude Oil berdasarkan data historis univariat.
- Menganalisis dan memodelkan struktur tren, stasioneritas, dan volatilitas yang terdapat dalam data harga Crude Oil.
- Mengevaluasi performa model menggunakan berbagai metrik seperti MAE, MSE, RMSE, dan MAPE untuk menentukan pendekatan peramalan terbaik.

## Struktur Repository <a id='Struktur'></a>

```
proyek-peramalan-global-comodity-price-september-2024/
├── data/
│   ├── Arkavidiaa/                     # Data mentah dari kompetisi
│   │   ├── Global_Commodity_Price/
│   │   ├── Google_Trend/
│   │   │   ├── bawang/
│   │   │   │   ├── Aceh.csv
│   │   │   │   └── (... 32 file CSV lainnya per provinsi ...)
│   │   │   ├── beras/
│   │   │   │   └── (... data per provinsi ...)
│   │   │   └── (... 12 folder komoditas lainnya ...)
│   │   ├── Harga_Bahan_Pangan/
│   │   └── Mata_Uang/
│   └── Arkavidiaa_Processed/             # Data yang sudah dibersihkan dan diproses
│       ├── Global_Commodity_Price/
│       ├── Google_Trend/
│       ├── Harga_Bahan_Pangan/
│       └── Mata_Uang/
├── notebooks/
│   ├── 0_data_wrangling.ipynb
│   ├── 1_EDA.ipynb
│   ├── 2_ARIMA_Model.ipynb
│   ├── 3_Beyond_ARIMA_Model.ipynb
│   └── 4_Machine_Learning.ipynb
├── outputs/
│   ├── models/
│   │   └── arima_crude_oil_model.pkl
│   └── plots/                          # (Folder untuk menyimpan gambar/plot)
├── reports/
│   ├── main.tex
│   ├── proyek_akhir_metpar.pdf
│   └── references.bib
├── .gitignore
├── LICENSE
├── README.md
└── structure.md                      # Struktur direktori lengkap
```

**Catatan**: Struktur di atas adalah versi ringkas. Untuk melihat daftar file yang lengkap dan detail, silakan merujuk ke file `structure.md`.

## Cara Reproduksi Hasil <a id='Reproduksi'></a>

Untuk menjalankan analisis ini di mesin lokal Anda, ikuti langkah-langkah berikut:

1.  **Clone repositori ini:**
    ```bash
    git clone https://github.com/zakizulham/proyek-peramalan-global-comodity-price-september-2024.git && cd proyek-peramalan-global-comodity-price-september-2024
    ```

2.  **Buat dan aktifkan Virtual Environment (Direkomendasikan):**
    ```bash
    # Membuat environment
    python -m venv venv

    # Mengaktifkan di Windows
    .\venv\Scripts\activate

    # Mengaktifkan di MacOS/Linux
    source venv/bin/activate
    ```

3.  **Instal pustaka yang dibutuhkan:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Jalankan Jupyter Notebook:**
    Jalankan notebook secara berurutan, dimulai dari `1_Data_Exploration.ipynb`, `2_ARIMA_Modelling.ipynb`, dan `3_ARIMA-GARCH_Modelling`.ipynb.
    ```bash
    jupyter notebook notebooks/analisis_churn.ipynb
    ```

## Ringkasan Proyek <a id='Ringkasan'></a>

Proyek ini dimulai dengan analisis eksplorasi data pada dataset Crude Oil WTI Futures Historical Data periode 1 Oktober 2022 hingga 30 September 2024. Hasil analisis menunjukkan bahwa data harga bersifat non-stasioner dan menunjukkan adanya volatility clustering, di mana periode fluktuasi tinggi diikuti oleh periode fluktuasi tinggi lainnya.

1. Pemodelan ARIMA:

    - Uji Augmented Dickey-Fuller (ADF) mengonfirmasi data tidak stasioner. Setelah dilakukan diferensiasi pertama (d=1), data menjadi stasioner.
    - Berdasarkan analisis plot ACF dan PACF serta perbandingan kriteria AIC dan BIC, model ARIMA(1,1,2) terpilih sebagai model terbaik untuk memodelkan komponen rata-rata.
    - Meskipun model ini mampu menangkap korelasi data, diagnostik residual menunjukkan adanya heteroskedastisitas, yang mengindikasikan perlunya pemodelan volatilitas.

2. Pemodelan ARIMA-GARCH:

    - Untuk menstabilkan varians, transformasi logaritmik diterapkan pada data sebelum pemodelan.
    - Residual dari model ARIMA(1,1,2) pada data logaritmik dimodelkan menggunakan GARCH untuk menangkap volatilitas. Model GARCH(1,1) terpilih sebagai yang terbaik karena signifikansi parameter dan kriteria informasi yang paling optimal.
    - Parameter GARCH ( $ \alpha + \beta \approx 0.9258 $ ) menunjukkan bahwa volatilitas pada harga minyak mentah memiliki sifat persisten (bertahan lama).

3. Hasil dan Evaluasi:
Model gabungan **ARIMA(1,1,2)-GARCH(1,1)** dievaluasi performanya pada data uji. Beberapa metode peramalan diuji, dan hasilnya dibandingkan dengan model ARIMA standalone.

| **Model Peramalan**                   | **MAE** | **RMSE** | **MAPE** |
|---------------------------------------|---------|----------|----------|
| ARIMA(1,1,2)                          | 5.49    | 6.46     | 6.94%    |
| ARIMA(1,1,2)-GARCH(1,1) + Monte Carlo | 4.82    | 5.73     | 6.18%    |

Kesimpulannya, model gabungan **ARIMA(1,1,2)-GARCH(1,1) yang diimplementasikan dengan simulasi Monte Carlo** memberikan hasil peramalan yang paling akurat. Pendekatan ini tidak hanya mampu memodelkan tren harga tetapi juga berhasil menangkap dinamika volatilitas yang kompleks, menghasilkan kesalahan prediksi (MAPE) terendah sebesar **6.18%**.


## Lisensi <a id='Lisensi'></a>

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file `LICENSE` untuk detail lebih lanjut.
