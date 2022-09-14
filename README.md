----TUGAS 2 PBP----

link HEROKU :  http://catalogpbp.herokuapp.com/katalog/

   - Bagan request clien :
      https://drive.google.com/file/d/1OsYMYqz1EbiaqL3LA9OEZAu6UW00LNvg/view?usp=sharing

   - Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? 
      Virtual environment adalah sebuah environment manager yang digunakan untuk membuat lingkungan python virtual yang terisolasi. yang berguna untuk memastikan kalau library yang kita gunakan di suatu proyek tidak akan berubah apabila ada update di library yang sama di proyek lain. Intinya adalah agar proyek kita tidak tercampur. Aplikasi tetap dapat dibuat tanpa venv tetapi python sangat merekomendasikan menggunakan venv. Dan juga ada kemungkinan bahwa ketika proyek dijalankan dengan Django akan ada permasalahan-permasalahan. Ada kemungkinan proyek kita tidak bisa beradaptasi dengan Django versi lainnya. Oleh karena itu, penggunaan venv merupakan hal yang penting dalam menggunakan Django.

   - Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
      Pertama, membuat repository baru di github dan clone ke device menggunakan template yang disediakan. Mulai mengerjakan proyek dimulai dari views.py (membuat fungsi show_katalog untuk menerima parameter request). Selanjutnya menampung data dan contextnya NAMA dan NPM. Lalu mapping ke html dengan menggunakan context. Selanjutnya routing views.py pada urls.py untuk menghubungkan antara HTML dan web. Selanjutnya mapping data agar bisa ditampilkan di web browser untuk menampilkan item nama, harga, stok, rate, deskripsi, dan url nya.
      Setelah proses ini selesai, lanjut untuk melakukan migration, meload data, dan menjalankan proyek tersebut. Lalu melakukan pengecekan pada web localhost katalog untuk memastikan bahwa hasil proyek saya telah bisa ditampilkan. Terakhir, melakukan deploy ke aplikasi Heroku dengan mengcopy APi key dan menyambungkan ke secret Github. Selesai.
