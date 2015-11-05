<h3>Solved by: ArtOfS</h3>
Deskripsi soal:
<pre>
My friend is the greatest web designer I've ever seen. Once he even made the web site for his favourite husky Fourier. Sadly he is not very good at site administration.
http://sibears.ru:10026/site
http://sibears.ru:12026/site
http://sibears.ru:13026/site
Some ports: 11026, 15026, 16026
</pre>

Buka salah satu link diatas dan dari web tersebut dapat disimpulkan /site bukanlah index dari web tersebut.
Coba hapus site dan kita mendapatkan folder ssh yang isinya private key yang bisa digunakan untuk mengakses ssh tanpa password (download file sshnya : http://sibears.ru:10026/ssh/ ).

Akses ssh dengan username admin@sibears.ru dan gunakan private key admin dan some ports yang diberikan disini kami menggunakan port 11026. Voila !!! Login sukses !!! 
Terdapat flag.txt pada saat di cat ternyata tidak bisa kemudian masukan perintah ? / help untuk mengetahui perintah apa saja yang dapat digunakan dan ternyata flag tidak dapat begitu saja dengan mudah dibaca.

Setelah cek history terdapat perintah-perintah yang sangat menarik untuk dicoba. Pada saat memasukan perintah 
```bash
echo $(cat flag.txt)
```
Perintah cat dapat dijalankan dengan mengetik perintah diatas dan telihat flagnya.
Flag: <b>4dm1n_1s_1mp0r74nt_m^^mk3y</b>
