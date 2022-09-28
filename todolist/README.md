---------TUGAS 4 PBP-----------

link Heroku :

Apa kegunaan {% csrf_token %} pada elemen <form>? 
    - CSRF Token dapat mencegah serangan CSRF yang akan membuat penyerang tidak mungkin melakukan permintaan HTTP yang secara sepenuhnya valid yang cocok untuk diumpankan ke pengguna. Tujuan utamanya adalah agar data yang dikirim ke server berasal dari website milik kita. Mencegah orang lain mengirim data ke servey tanpa melewati aplikasi.


Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
    - Browser akan mereject request / error karena browser tidak bisa memastikan asal data yang dikirim ke server. 
    Error : CSRF token missing


Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
    - Bisa dengan menggunakan tag yang disediakan HTML. Contoh tag <input> pada login.html yang dimana data yang diterima form disimpan dan dapat diakses dalam views.py dengan method get() 


Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
    - User mengisi data yang dibawa oleh request dan disimpan dalam variabel form di views.py
    - form di save untuk menyimpan data tsersebut
    - views.py meminta data models.py dari database untuk dikirimkan ke templates untuk di tampilkan


Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
    - Pertama-tama membuat aplikasi django todolist, menambahkan path todolist ke urls.py,  membuat model task dengan 4 atribut (user,date,title,description)
    - membuat beberapa fungsi dasar di views.py, register untuk menu register akun pengguna, login_user untuk halaman login awal, logout_user
    - membuat fungsi di views.py show_todolist untuk menampilkan task dan create_task untuk membuat task baru
    - membuat halaman todolist di todolist.html sebagai tempat task akan dimunculkan dan create_task untuk membuat task baru
    - mmenambahkan path ke urls.py untuk register, login, logout, show_todolist, dan create_task
    - deploy ke heroku dengan deploy ke git dahulu. menajalankan dan membuat dua akun lewat heroku.

