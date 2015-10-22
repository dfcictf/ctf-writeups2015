Deskripsi soal: 
<pre>
Since his students never know what date it is and how much time they have until the next homework's deadline, Mr P. H. Porter wrote a little webapp for that.
</pre>
URL: http://school.fluxfingers.net:1522/
<br />
Pada tantangan kali ini, peserta diberikan sebuah soal dimana terdapat beberapa modules yang dapat kita lihat yaitu <b>date</b> serta <b>timer</b>.
<br />
Pertama kami mengira untuk mendapatkan modules yang diminta ( yang kami rasa itu adalah flagnya ) dengan mem-bypass timing dari javascript countdown timer hingga waktu tersebut hanya tinggal beberapa detik lagi.
Tetapi kami meleset, setelah mencoba hal tersebut dan ternyata tidak ada hasil apa - apa. Maka kami coba untuk melakukan hal yang lain yaitu dengan mengecek direktori <b>modules</b> pada situs tantangan tersebut.
Sebelumnya, cara kami mendapatkan direktori modules tersebut adalah pada informasi halaman / page source situs tantangan tersebut.
<br />
Direktori tersebut dapat dicek di page source situs tantangan ini, dengan itu kami berasumsi bahwa situs ini memiliki kerentanan akan serangan LFI ( Local File Inclusion ). Dimana didalam direktori <b>modules</b> terdapat beberapa file yakni.
<pre>
date 
timer 
</pre>
Dengan parameter yang ada pada situs tersebut , kita dapat mengakses file - file yang ada pada direktori tersebut dengan parameter yang sudah tercantum.
<pre>
https://school.fluxfingers.net:1522/?module=date
https://school.fluxfingers.net:1522/?module=timer&time=yy-mm-dd
</pre>
Jadi skema code dalam pemrograman phpnya kurang lebih seperti berikut ini : 

```php
<?php
$modul = $_GET['module'];
include('modules/'.$modul);
?>
```
Jika dilihat dari kode tersebut, berarti secara tidak langsung kita dapat memanfaatkan beberapa hal untuk mengakses file diluar dari direktori modules itu sendiri. Dengan cara pointing ke direktori yang sebelumnya dengan menggunakan perintah "../" pada parameter module.
Disini target file yang akan kami cari ialah file <b>.htaccess</b> untuk mengecek konfigurasi apa saja yang diatur didalam file tersebut, kita harus mengakses kebagian direktori utamanya.
Untuk itu teknik yang kami gunakan disini adalah sebagai berikut : 
<h3>1. Mengecek kerentanan pada serangan LFI :</h3>
<pre>https://school.fluxfingers.net:1522/?module=../index.php ( terlihat jelas bahwa halaman page yang sama tertumpuk, berarti sudah pasti serangan LFI dapat dijalankan ).</pre>
<h3>2. Mengecek file .htaccess</h3>
<pre>https://school.fluxfingers.net:1522/?module=../.htaccess ( voila! ).</pre>

File <b>.htaccess</b> ditemukan dengan output yang diberikan adalah sebagai berikut.
<pre># needs to be hidden from direct access</pre>
Sepertinya itu adalah salah satu clue yang diberikan. Maka dari itu kami berasumsi bahwa ada sesuatu yang disembunyikan, langkah selanjutnya ialah kami mengecek apakah ada sesuatu yang disembunyikan pada halaman tersebut.
Benar saja, setelah kami mencoba melihat page source, beberapa konfigurasi ternyata diberi tag komentar. Dan dari isi dari file <b>.htaccess</b> yang di-block komentar tersebut tampil seperti berikut: 
```html
<!--
# seems to be not working, though
#<Directory "3cdcf3c63dc02f8e5c230943d9f1f4d75a4d88ae">
#    Options -Indexes
#</Directory>
# -->
```
Terlihat bahwa sebuah informasi direktori dengan nama <b>3cdcf3c63dc02f8e5c230943d9f1f4d75a4d88ae</b> yang kami yakin bahwa direktori tersebut menyimpan file flag. Setelah langsung mencoba mengakses https://school.fluxfingers.net:1522/3cdcf3c63dc02f8e5c230943d9f1f4d75a4d88ae/ terlihat ada sebuah file php bernama <b>flag.php</b>. Tetapi setelah diakses muncul pesan "not that easy, fella".
Ini menunjukkan file tersebut tidak bisa diakses langsung dengan mudahnya, langkah yang dapat diambil adalah kembali lagi ke parameter module, lalu mengaksesnya dengan perintah seperti berikut: 
<pre>https://school.fluxfingers.net:1522/?module=../3cdcf3c63dc02f8e5c230943d9f1f4d75a4d88ae/flag.php</pre>
Ditemukan flag: <b>flag{hidden_is_not_actually_hidden}</b>
