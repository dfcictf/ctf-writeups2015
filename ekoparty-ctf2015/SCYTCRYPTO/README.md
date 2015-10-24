Deskripsi soal: 
<pre>
Decrypt this strange word: ERTKSOOTCMCHYRAFYLIPL 
</pre>
Point yang didapat apabila dapat menyelesaikan soal ini akan mendapat sebanyak 50 point. Sekilas bentuk kata tersebut seperti sebuah cipher, tetapi banyak jenis - jenis cipher yang kami coba decode ternyata tidak ada yang mengeluarkan hasil seperti yang kami harapkan.
Setelah berpikir sejenak muncul beberapa ide konyol yang secara tidak sengaja ternyata membuahkan sebuah hasil. Melakukan sedikit analisis terhadap kata tersebut, mengingat setiap flag yang akan kami submit pasti memiliki kata kunci "EKO".
<br />
<b>E</b>RT<b>K</b>SO<b>O</b>TCMCHYRAFYLIPL , sudah terlihat ada hal yang menarik dari beberapa karakter yang ditebalkan ini. Maka kami membentukan pola seperti berikut : 
<br />
<pre>
ABC
DEF
GHI
JKL
MNO
...
Pada kata yang harus kita decrypt tersebut kami susun menjadi seperti pola diatas.
ERT
KSO
OTC
MCH
YRA
FYL
IPL
Jika disusun menjadi: EKOMYFIRSTCRYPTOCHALL.
</pre>
Flag: <b>EKO{MYFIRSTCRYPTOCHALL}</b>
