## Prosedur Algoritma Forecasting Harga Komoditas Global Tunggal dengan ARIMA

**Model yang Digunakan**: ARIMA (AutoRegressive Integrated Moving Average)  
**Target**: Memprediksi harga masa depan untuk satu komoditas global (misalnya, *Crude Oil*) menggunakan data historisnya sendiri.

### Langkah-langkah:

#### 1. Memuat dan Mempersiapkan Data
- Muat dataset komoditas yang diinginkan (misalnya, `dataset_crudeOil`) menggunakan `pandas`.
- Pastikan kolom `'date'` sudah dalam tipe data `datetime` menggunakan `pd.to_datetime()`.
- Atur kolom `'date'` sebagai indeks DataFrame. Ini penting untuk analisis time series.
- Pilih kolom target yang akan diprediksi (misalnya, `'price'`). Kolom lain seperti `'Volume'` bisa digunakan di model kompleks, tapi tidak untuk ARIMA tunggal.
- Tangani nilai hilang (NaN) dengan interpolasi, penghapusan baris, atau metode lain.
- Pastikan data sudah diurutkan berdasarkan tanggal.

#### 2. Visualisasi Deret Waktu
- Plot deret waktu harga (`price` terhadap `'date'`) untuk melihat tren, musiman, dan anomali.

#### 3. Uji Stasioneritas
- ARIMA memerlukan deret waktu yang **stasioner** (rata-rata dan variansi konstan sepanjang waktu).
- Gunakan uji **Augmented Dickey-Fuller (ADF)** untuk menguji stasioneritas.
- Jika tidak stasioner (p-value ADF > 0.05), lakukan diferensiasi (pengurangan nilai saat ini dengan sebelumnya).
- Jumlah diferensiasi = parameter `d` dalam ARIMA.

#### 4. Identifikasi Ordo Model ARIMA (p, d, q)
- `d`: Jumlah diferensiasi dari langkah sebelumnya.
- `p` (AR - AutoRegressive): Lihat **PACF plot**, tentukan lag ketika PACF pertama kali menyilang batas kepercayaan.
- `q` (MA - Moving Average): Lihat **ACF plot**, tentukan lag ketika ACF pertama kali menyilang batas kepercayaan.
- Ini proses iteratif, coba berbagai kombinasi `(p, d, q)`.

#### 5. Pembagian Data Latih dan Uji
- Bagi data menjadi set pelatihan dan pengujian berdasarkan waktu.
- Contoh: data hingga tahun tertentu untuk pelatihan, sisanya untuk pengujian.

#### 6. Pelatihan Model ARIMA
- Import `ARIMA` dari `statsmodels.tsa.arima.model`.
- Inisialisasi model dengan `(p, d, q)` dan data latih.
- Latih model dengan `.fit()`.

#### 7. Membuat Prediksi
- Gunakan model terlatih untuk memprediksi data uji.
- Bisa memprediksi satu langkah atau banyak langkah ke depan.

#### 8. Evaluasi Model
- Bandingkan hasil prediksi dengan data aktual.
- Hitung metrik evaluasi:
  - MAE (Mean Absolute Error)
  - MSE (Mean Squared Error)
  - RMSE (Root Mean Squared Error)
  - MAPE (Mean Absolute Percentage Error)

#### 9. Penyempurnaan Model (Tuning)
- Ulangi langkah 4–8 dengan kombinasi `(p, d, q)` berbeda jika performa belum optimal.
- Proses ini dikenal sebagai **tuning hyperparameter**.

#### 10. Prediksi Masa Depan (Setelah Tuning)
- Setelah model final dipilih, latih ulang dengan seluruh data (latih + uji).
- Gunakan model akhir untuk memprediksi harga di masa depan.

---

### Perhatikan:
- Pemilihan ordo `(p, d, q)` memerlukan analisis ACF/PACF dan eksperimen.
- Gunakan `pmdarima.auto_arima` untuk pencarian ordo otomatis.
- ARIMA hanya menangani pola linier dan tidak cocok untuk pola musiman yang kuat.  
  Untuk pola musiman, pertimbangkan menggunakan **SARIMA (Seasonal ARIMA)**.
- Setiap langkah memerlukan implementasi Python dengan library seperti:
  - `pandas`
  - `matplotlib`
  - `statsmodels`
