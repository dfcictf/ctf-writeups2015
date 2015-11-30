Deskripsi soal:
<pre>
My friend wrote a cool web server. I'm sure he's stored some great doxxxs on the website. Can you take a look and report back any interesting things you find?
The web page is at http://yws-fsiqc922.9447.plumbing
</pre>
<h3>Solved by snoww0lf</h3>
Ini adalah soal dengan poin tertinggi yang berhasil saya selesaikan, disini dapat melihat web tersebut
nampak sangat sedikit clue yang bisa ditemukan. Tapi ada beberapa bagian menarik pada file 'robots.txt' , salah satu bagian yang sangat menarik adalah instruksi berikut. 
<pre> Disallow: /.. </pre>

Dengan melakukan koneksi menggunakan telnet dengan perintah 
<pre>
telnet yws-fsiqc922.9447.plumbing 80
</pre>
dan dengan memanfaatkan celah Directory Traversal/Path Traversal kita dapat melakukan serangan pada request GET tepat pada bagian headernya.
<pre>
GET /.. HTTP/1.0
Host: yws-fsiqc922.9447.plumbing
</pre>
Ditemukanlah flagnya. 
Flag: <b>9447{D1rect0ries_ARe_h4rd}</b>
