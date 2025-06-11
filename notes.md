## 

## apa itu granularitas?

### Granularitas dalam Data dan Time Series

Dalam konteks data dan time series, **granularitas** mengacu pada tingkat detail atau frekuensi data tersebut direkam atau dikumpulkan. Ini menentukan seberapa halus (atau kasar) data Anda.

Bayangkan Anda memiliki data suhu udara:

- **Granularitas Tinggi**: Data suhu dicatat setiap menit. Ini sangat detail, memberikan banyak titik data dalam periode waktu tertentu.
- **Granularitas Rendah**: Data suhu dicatat setiap bulan. Ini kurang detail, hanya memberikan satu titik data per bulan.

#### Contoh pada Dataset

- **Global Commodity Price**: Data harian. Ini adalah granularitas yang relatif tinggi untuk data harga.
- **Google Trends**: Data mingguan. Ini adalah granularitas yang sedikit lebih rendah dibandingkan harian.

---

### Mengapa Granularitas Penting dalam Forecasting?

- **Pilihan Model**:  
  Beberapa model forecasting bekerja lebih baik dengan granularitas tertentu.  
  Misalnya:
  - Model yang menangkap **pola musiman harian** (seperti pola penggunaan listrik yang berubah setiap jam) membutuhkan data dengan granularitas **jam**.
  - Model yang menangkap **pola musiman tahunan** mungkin cukup dengan data **bulanan**.

- **Pola yang Terlihat**:  
  Granularitas yang berbeda dapat menyoroti pola yang berbeda.
  - Data **harian** mungkin menunjukkan fluktuasi harga yang cepat dalam seminggu.
  - Data **bulanan** mungkin hanya menunjukkan tren jangka panjang.

- **Integrasi Data**:  
  Jika Anda ingin menggabungkan dataset dengan granularitas yang berbeda (misalnya, harga harian dan Google Trends mingguan), Anda perlu melakukan **resampling**.
  - Anda mungkin perlu **merata-ratakan data harian menjadi mingguan**.
  - Atau menggunakan **metode interpolasi** untuk mengestimasi nilai harian dari data mingguan.

- **Tujuan Prediksi**:  
  Granularitas prediksi Anda akan sering cocok dengan granularitas data input.
  - Jika Anda melatih model dengan data **harian**, prediksi Anda kemungkinan akan berupa **prediksi harian**.

---

### Kesimpulan

Secara singkat, **granularitas** adalah ukuran seberapa sering data Anda diukur atau dicatat, dan itu memiliki **dampak signifikan** pada bagaimana Anda menganalisis dan memprediksi time series.

- Semakin **tinggi granularitas**, semakin banyak **detail** yang Anda miliki, tetapi juga semakin besar **volume data** dan potensi **noise**.
- Semakin **rendah granularitas**, semakin **ringkas** data, tetapi Anda mungkin kehilangan **detail penting** atau **pola jangka pendek**.



## misal aku menerapkam arima, sarima, transformasi log pada arima, atau pun yang tidak aku buat sebelumnya seperti box cox, dan ARCH- GARCH. itu setiap mulai, aku harus mendeteksi p,d,q nya selalu kah? tidak bisa p,d,q yang sama pada arima aku gunakan untuk ARCH? dan dapatkan p,d,q melalui plot. Jadi, aku harus selalu analisis plot tiap kali menerapkan model baru?


## Pemahaman Order Model pada ARIMA, SARIMA, Transformasi, dan ARCH-GARCH

### 1. Perlukah mendeteksi ulang order (p, d, q) saat menerapkan model baru?

#### 1.1 ARIMA, SARIMA, Box-Cox + ARIMA/SARIMA
- **Ya**, perlu deteksi ulang order (p, d, q) dan (P, D, Q, s) saat menggunakan model baru.
- Penjelasan:
  1. **ARIMA** memodelkan komponen non-musiman:
     - AR (AutoRegressive)
     - I (Integrated / differencing)
     - MA (Moving Average)
  2. **SARIMA** menambahkan komponen musiman:
     - Seasonal AR, Seasonal I, Seasonal MA
     - Periode musiman `s`
  3. **Box-Cox Transformasi**:
     - Mengubah distribusi data deret waktu
     - Dapat memengaruhi pola ACF (Autocorrelation Function) dan PACF (Partial Autocorrelation Function)
     - Maka, **Box-Cox dilakukan lebih dulu**, lalu deteksi ulang order (p, d, q) dan (P, D, Q, s) pada data yang telah:
       - Ditransformasi
       - Didifferensiasi (jika perlu)

#### 1.2 ARCH-GARCH
- Model **ARCH (Autoregressive Conditional Heteroskedasticity)** dan **GARCH (Generalized ARCH)** digunakan untuk **memodelkan volatilitas atau varians residual** dari model deret waktu (biasanya setelah ARIMA/SARIMA).
- Parameter:
  - **GARCH(p, q)**:
    - `p`: lag dari varians bersyarat sebelumnya (**GARCH term**)
    - `q`: lag dari residual kuadrat sebelumnya (**ARCH term**)
  - Ini **berbeda dari p, d, q pada ARIMA** (yang untuk mean deret waktu).
- Prosedur:
  1. Latih model ARIMA atau SARIMA terlebih dahulu.
  2. Ambil **residual** dari model tersebut.
  3. Analisis residual untuk menguji apakah mengandung heteroskedastisitas.
  4. Jika ya, modelkan residual dengan ARCH/GARCH.

### 2. Bisakah p, d, q dari ARIMA digunakan untuk ARCH?

- **Tidak bisa.**
  - Parameter `p`, `d`, `q` pada **ARIMA** digunakan untuk memodelkan **rata-rata (mean)** dari deret waktu.
  - Parameter `p`, `q` pada **ARCH/GARCH** digunakan untuk memodelkan **varians (volatilitas)** dari residual deret waktu.
  - Artinya: meskipun namanya sama, **makna dan aplikasinya berbeda**.

### 3. Haruskah selalu melakukan analisis plot saat menerapkan model baru?

#### 3.1 Untuk ARIMA/SARIMA
- **Ya, harus.**
- Langkah-langkah umum:
  1. Gunakan **uji stasioneritas** seperti:
     - **ADF (Augmented Dickey-Fuller)** test
     - **KPSS (Kwiatkowski-Phillips-Schmidt-Shin)** test  
     untuk menentukan nilai **`d`** (berapa kali perlu differencing)
  2. Setelah data menjadi stasioner, lihat **plot ACF dan PACF**:
     - **ACF** bantu tentukan nilai `q`
     - **PACF** bantu tentukan nilai `p`
  3. Untuk SARIMA, analisis juga komponen musiman:
     - Gunakan ACF dan PACF musiman untuk tentukan `(P, Q)` dan `s`

#### 3.2 Untuk ARCH-GARCH
- **Plot tetap penting**, tapi dilakukan pada **residual dari model mean** (misalnya residual ARIMA)
- Langkah-langkah:
  1. Setelah fit model ARIMA, ambil **residual**
  2. Cek **heteroskedastisitas** pada residual, misalnya:
     - Gunakan **ARCH test** (Engle’s test)
  3. Jika terdapat heteroskedastisitas:
     - Plot **ACF dan PACF dari residual kuadrat** (bukan residual biasa!)
     - Plot ini membantu deteksi order (p, q) untuk model GARCH(p, q)

### 4. Kesimpulan

1. **ARIMA/SARIMA (dan setelah transformasi)**:
   - Gunakan **ADF/KPSS** untuk mendeteksi `d` (jumlah differencing yang diperlukan)
   - Gunakan **ACF/PACF** dari data stasioner untuk identifikasi `p` dan `q`
   - Untuk **SARIMA**, tentukan juga:
     - Komponen musiman `(P, D, Q, s)`
2. **ARCH-GARCH**:
   - Diterapkan **setelah fitting model mean (seperti ARIMA)**
   - Periksa **residual** untuk heteroskedastisitas
   - Gunakan **ARCH test**
   - Gunakan **ACF/PACF residual kuadrat** untuk menentukan `p` dan `q` pada GARCH
3. **Catatan Penting**:
   - **Plot ACF/PACF adalah alat serbaguna** dalam analisis deret waktu
   - Setiap model perlu analisis sendiri untuk identifikasi parameter optimalnya



### Informasi Model  
- **Model**: Mengkonfirmasi penggunaan model **ARIMA(1, 1, 1)**, di mana angka (1, 1, 1) menunjukkan orde:  
  - `1` (Autoregressive/AR)  
  - `1` (Integrated/differencing)  
  - `1` (Moving Average/MA)  
  Ini sesuai dengan analisis ACF/PACF dan uji ADF sebelumnya.  
- **Tanggal & Waktu**: Stempel waktu pelatihan model, berguna untuk pelacakan eksperimen.  

### Informasi Data  
- **Jumlah Observasi**: Menunjukkan total titik data dalam `data_latih` (jumlah baris). Penting untuk memahami skala data yang dilatih.  

### Ringkasan Koefisien  
Estimasi parameter model:  
- **ar.L1** (Autoregressive pada lag 1):  
  - `coef`: Estimasi koefisien AR(1). Nilai positif menunjukkan korelasi positif dengan data periode sebelumnya; magnitudo menunjukkan kekuatan hubungan.  
  - `std err`: Standard error estimasi. Nilai kecil mengindikasikan presisi lebih tinggi.  
  - `z`: Statistik uji (z-score).  
  - `P>|z|` (P-value): Signifikansi statistik. Jika **< 0.05**, komponen AR(1) signifikan.  
  - `[0.025, 0.975]`: Interval kepercayaan 95%. Jika tidak mencakup nol, koefisien signifikan.  

- **ma.L1** (Moving Average pada lag 1):  
  Interpretasi sama seperti `ar.L1`. Jika **P>|z| < 0.05**, komponen MA(1) signifikan.  

- **sigma²** (Variansi residual):  
  Estimasi variabilitas sisa setelah pemodelan. Nilai lebih kecil mengindikasikan model lebih baik dalam menjelaskan variabilitas data.  

### Statistik Evaluasi Model  
- **Ljung-Box (Q) & P(Q)**:  
  - Menguji autokorelasi residual.  
  - **Insight**: `P(Q) > 0.05` (untuk sebagian besar lag) menunjukkan residual menyerupai *white noise*. Jika `P(Q) kecil`, ada pola yang belum terjelaskan.  

- **Heteroskedastisitas (H) & P(H)**:  
  - Menguji konsistensi variansi residual.  
  - **Insight**: `P(H) > 0.05` diinginkan. Nilai kecil mengindikasikan heteroskedastisitas (variansi tidak konstan), yang umum pada data finansial. Solusi: pertimbangkan model **ARCH/GARCH**.  

- **Jarque-Bera (JB) & P(JB)**:  
  - Menguji normalitas residual.  
  - **Insight**: `P(JB) > 0.05` menunjukkan residual normal. Nilai kecil mengindikasikan ketidaknormalan atau pola yang belum tertangkap.  
  - **Skew** (kemiringan): Mendekati `0` untuk normalitas.  
  - **Kurtosis** (keruncingan): Mendekati `3` (distribusi normal).  

- **AIC, BIC, HQIC**:  
  Metrik penyeimbang *goodness of fit* dan kompleksitas model:  
  - **AIC** (Akaike Information Criterion)  
  - **BIC** (Bayesian Information Criterion)  
  - **HQIC** (Hannan-Quinn Information Criterion)  
  **Insight**: Nilai lebih rendah menunjukkan model lebih optimal saat membandingkan kombinasi ordo (p, q) pada dataset sama.