# Aplikasi Penerjemah

Aplikasi Penerjemah adalah sebuah program sederhana yang dibangun menggunakan Python dan Tkinter, yang memungkinkan pengguna untuk menerjemahkan teks dari satu bahasa ke bahasa lainnya dengan mudah. Aplikasi ini menggunakan Google Translate API melalui paket `googletrans`.

## Fitur

- **Pilih Bahasa**: Pengguna dapat memilih bahasa sumber dan bahasa target dari dropdown menu yang disediakan.
- **Teks Input**: Pengguna dapat memasukkan teks yang ingin diterjemahkan. Teks ini memiliki batas maksimum 50.000 karakter.
- **Hasil Penerjemahan**: Teks yang telah diterjemahkan akan ditampilkan di area output setelah proses terjemahan.
- **Tukar Bahasa**: Fitur untuk menukar bahasa sumber dan target secara cepat.
- **Hitung Karakter**: Menampilkan jumlah karakter yang telah dimasukkan dan memberikan peringatan jika melebihi batas karakter.

## Kelebihan Aplikasi

- **User-Friendly**: Antarmuka yang sederhana dan mudah digunakan membuatnya cocok untuk pengguna dari semua kalangan.
- **Cepat dan Efisien**: Proses penerjemahan berlangsung dengan cepat berkat penggunaan Google Translate API.
- **Dukungan Banyak Bahasa**: Aplikasi ini mendukung banyak bahasa, memungkinkan pengguna untuk menerjemahkan antara berbagai bahasa di seluruh dunia.

## Teknologi yang Digunakan

Aplikasi ini dibangun dengan menggunakan teknologi berikut:

- **Python**: Bahasa pemrograman yang digunakan untuk membangun logika aplikasi.
- **Tkinter**: Pustaka GUI untuk membuat antarmuka pengguna desktop.
- **googletrans**: Pustaka untuk mengakses Google Translate API.

## Instalasi dan Penggunaan

### Prasyarat

Sebelum menjalankan aplikasi, pastikan Anda memiliki:

- Python 3.x terinstal di sistem Anda.
- Koneksi internet untuk mengakses Google Translate API.

### Instalasi

1. **Kloning Repositori**

   Jika Anda menggunakan Git, Anda dapat mengkloning repositori dengan perintah:

   ```bash
   git clone https://github.com/Athallah1234/Translator.git
   ```

2. **Navigasi ke Direktori Aplikasi**

   ```bash
   cd Translator
   ```

3. **Instal Dependensi**

   Jalankan perintah berikut untuk menginstal semua dependensi yang diperlukan:

   ```bash
   pip install -r requirements.txt
   ```

5. **Menjalankan Aplikasi**

   Setelah semua langkah di atas selesai, Anda dapat menjalankan aplikasi dengan perintah:

   ```bash
   python run.py
   ```

## FAQ

### 1. Apa yang harus dilakukan jika saya mendapatkan kesalahan saat menerjemahkan?

Jika Anda mengalami kesalahan saat melakukan terjemahan, pastikan Anda memiliki koneksi internet yang stabil. Selain itu, periksa apakah Anda telah memilih bahasa sumber dan target dengan benar.

### 2. Apakah aplikasi ini gratis?

Ya, aplikasi ini sepenuhnya gratis untuk digunakan. Namun, penggunaan Google Translate API mungkin dikenakan biaya tergantung pada batasan dan kebijakan mereka.

### 3. Dapatkah saya menggunakan aplikasi ini tanpa koneksi internet?

Tidak, aplikasi ini memerlukan koneksi internet untuk mengakses Google Translate API untuk melakukan terjemahan.

### 4. Bagaimana cara menambahkan bahasa baru ke dalam aplikasi?

Aplikasi ini secara otomatis mengambil daftar bahasa dari Google Translate. Namun, jika Anda ingin menambahkan dukungan untuk bahasa tertentu secara manual, Anda dapat melakukannya dengan memperbarui daftar bahasa di kode sumber.

## Lisensi
Proyek ini dilisensikan di bawah [MIT License](LICENSE), yang berarti Anda bebas menggunakan, menyalin, memodifikasi, dan mendistribusikan kode ini, selama Anda memberikan kredit kepada penulis asli.

## Kontak
Jika Anda memiliki pertanyaan, masalah, atau masukan mengenai aplikasi ini, silakan hubungi kami melalui:
- Email: [email@example.com](mailto:email@example.com)
- GitHub Issues: [Laporkan masalah di sini](https://github.com/username/url-shortener/issues)
