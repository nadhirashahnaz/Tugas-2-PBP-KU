Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
    Asynchronous adalah proses jalannya program bisa dilakukan secara bersamaan tanpa harus menunggu proses antrian. Ini menandakan bahwa pemrograman asynchronous tidak melakukan pekerjaannya secara old style / cara lama yaitu dengan eksekusi baris program satu persatu secara hirarki. Asynchronous programming melakukan pekerjaannya tanpa harus terikat dengan proses lain atau dapat kita sebut secara Independent.

    Synchronous merupakan bagian dari Asynchronous (1 antrian) dimana proses akan dieksekusi secara bersamaan dan untuk hasil tergantung lama proses suatu fungsi synchronous .
    Task akan dieksekusi satu persatu sesuai dengan urutan dan prioritas task. Hal ini memiliki kekurangan pada lama waktu eksekusi karena masing-masing task harus menunggu task lain selesai untuk diproses terlebih dahulu.

Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
    Event-Driven programming juga bisa dibilang suatu paradigma pemrograman yang alur programnya ditentukan oleh suatu event / peristiwa yang merupakan keluaran atau tindakan pengguna atau bisa berupa pesan dari program lainnya.
    Penerapannya pada tugas ini terdapat pada implementasi tombol submit form penambahan task. Bila tombol ditekan maka terdapat event yang ditangani oleh AJAX sebagai perantara untuk mengirim data yang diisi dari form ke server. AJAX akan memperbarui data pada section Todolist secara asynchronous.


Jelaskan penerapan asynchronous programming pada AJAX.
    Membuat view dan url path baru yang mereturn sebuah response JSON. Pada tugas ini terdapat function get serta post untuk mengambil serta mengirim data JSON ke server, serta mengatur tampilan pada Todolist secara asynchronous sesuai data yang ada pada database.
    
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
    - Membuat function baru yang mereturn response berupa JSON
    - Menambahkan atribut onClick di button Create-Task dan modals pop up
    - Menambahkan function javascript untuk get dan post request ke server
