---TUGAS 3 PBP---
Link Deploy Heroku : http://catalogpbp.herokuapp.com/mywatchlist/html/


Jelaskan perbedaan antara JSON, XML, dan HTML!
Ketiganya adalah sama sama format yang digunakan untuk menyimpan dan menukar informasi dari web server agar dapat dibaca oleh pengguna. Perbedaannya ada pada:
    - JSON menyimpan elemen secara elemen tetapi tidak rapi dilihat, sementara XML menyimpan elemen dengan terstruktur dan mudah dibaca manusia tetapi kurang efisien. HTMl lebih dirancang untuk memfasilitasi transfer dokumen berbasis web. HTML digunakan untuk membuat halaman web dan aplikasi web. Tujuan desain XML difokuskan untuk mengangkut data.
    - JSON digunakan untuk mengirimkan data dengan cara data diurai lalu dikirimkan melalui internet. XML memiliki data terstruktur dan dapat ditambahkan catatan
    - Nama file JSON diakhiri ekstensi .json, file XML dikahir ekstensi .xml, file HTML diakhiri dengan ekstensi  .html

Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    Karena nantinya dalam proses pengimplementasian sebuah platform, akan butuh mengirimkan data dari satu stack ke stack lainnya. Data tersebut bisa berbentuk macam-macam seperti HTML,XML atau JSON.


Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
    [] Membuat suatu aplikasi baru bernama mywatchlist di proyek Django Tugas 2 pekan lalu:
        -Menjalankan perintah python manage.py startapp mywatchlist, lalu mendaftarkan app tersebut ke project_django dengan cara menambahkan app ke variabel INSTALLED_APPS

    [] Menambahkan path mywatchlist sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist
        - Menambahkan path('wishlist/', include('wishlist.urls')), ke file urls.py

    [] Membuat sebuah model MyWatchList
        - membuat sebuah class baru di file models.py sesuai ketentuan yang ada pada soal (watched,title,rating,realesed date,review)
        - Melakukan migraton dengan perintah makemigartion dan migaret

    [] Menambahkan minimal 10 data untuk objek MyWatchList yang sudah dibuat di atas
        - objek dibuat pada file json dalam folder fixtures sesuai watchlist
        - me load data tersebut dengan perintah python manage.py loaddata initial_mywatchlist_data.json agar data tadi masuk ke database Django

    [] Mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat sebelumnya dalam tiga format
        - Membuat fungsi baru dan menyimpan hasil semua data yang telah di entry kan, lalu mereturn sesuai parameter data sesuai dengan html/json/xml

    [] Membuat routing sehingga data di atas dapat diakses melalui URL HTML, XML, JSON
        - Menambahkan path ke file urls.py agar routing ke 3 url tersebut diantaranya:
            path('html/', show_mywatchlist, name='show_mywatchlist'),
            path('xml/', show_xml, name='show_xml'),
            path('json/', show_json, name='show_json'),
        - Terakhir, menjalankan perintah python manage.py runserver untuk menjalankannya.
