Deskripsi soal:
<pre>
Description: There is something wrong with our pass validation, find it and get the flag.
http://ctfchallenges.ctf.site:10000/passcheck/ 
</pre>
Solusi: Ini adalah soal web dengan point sebanyak 50 yang hanya satu - satunya dapat kami selesaikan. Pada soal tersebut kita diberikan sebuah form untuk mengecek validasi pada inputan ( password ).
Title web "Equal equal equal!" yang secara tidak langsung mengingatkan kami pada sebuah fungsi perbandingan strcmp(); di PHP yang memiliki bug yang dapat kita manfaatkan, mengenai bug tersebut bisa dibaca pada halaman berikut http://turbochaos.blogspot.co.id/2013/08/exploiting-exotic-bugs-php-type-juggling.html.
<br /><br />
Mencoba menganalisa result header dari inputan tadi menggunakan Live HTTP Header kemudian menambah branch "[]" pada name=password menjadi name=password[] kemudian me-replaynya. Terlihat bahwa halaman website tersebut blank, kami mengira ada kesalahan yang kami lakukan disini, ternyata setelah dicoba melihat page source dari 
website tersebut didapatkanlah flagnya.
<br />
Flag: <b>EKO{strcmp_not_s0_s4fe}</b>
