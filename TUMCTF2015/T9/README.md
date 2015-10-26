Deskripsi soal:
<pre>
352404707644669372663764444477927397646952284349399866786464374767564472 ?
ctf.link/assets/downloads/misc/words.txt
NOT the default flag format! Do not add hxp{ }.
"Theoretisch schon"
      ~ Challenge Author
</pre>
Pada soal kali peserta diminta untuk mencoba menyelesaikan soal kategori Misc. Dilihat dari judul yaitu "T9" ( https://id.wikipedia.org/wiki/T9_%28predictive_text%29 ) mengingatkan kami pada salah satu situs yang dapat menyelesaikan permasalahan ini.
Disini kami menggunakan situs http://www.dcode.fr/t9-cipher untuk memecahkan isi pesannya. Mencoba menganalisa angka - angka yang diberikan pada soal, kami mencoba menghapus angka "0" karena angka tersebut dianggap sebagai spasi pada T9.
Maka hasil yang didapat adalah: <br />
3524 47 7644669372663764444477927397646952284349399866786464374767564472.
<br /><br />
Setelah di-decode didapatkan hasil: 
<pre>
3524  : FLAG 
47    : IS
</pre>
Lalu bagian angka setelah angka 47 tidak dapat ter-decode secara baik, mengingat kembali kita diberikan sebuah file "words.txt" maka sejenak kami berpikir kembali ( soal ini terbilang yang paling lama kami coba - coba dengan alasan stuck serta nyaris saja menyerah ).
Menganalisa sisa bagian tersebut kami mencoba untuk menghitung jumlah karakter yang ada pada sisa bagian angka tersebut. Setelah mendapatkan hasilnya yaitu 64 bytes, dengan ini kami membandingkan pada data di salah satu baris "words.txt". 
<br /><br />
Ternyata jumlah karakter - karakter per - baris data yang ada di "words.txt" memiliki jumlah yang sama. Karena hal tersebut terlihat meyakinkan bagi kami, maka kami melakukan replacing terhadap tiap karakter pada data - data tersebut dengan command berikut. 
```bash
cat words.txt | tr 'A-Za-z' '2223334445556667777888999922233344455566677778889999' | grep 7644669372663764444477927397646952284349399866786464374767564472 -n
```
Ditemukan output: 
<pre>896023:7644669372663764444477927397646952284349399866786464374767564472</pre>
Setelah mengecek baris 896023 ditemukan kata berikut: 7o4hoMXFRCNofPMiH4iIrpwBpfzrMgny5cBUieiWEwWUNoPVNHNherHSNsJOg4qB. Lalu kami mencoba menyubmit ke sistem submission, dan ternyata hasil tersebut dianggap valid sebagai sebuah flag.
<br /><br />
Flag: <b>7o4hoMXFRCNofPMiH4iIrpwBpfzrMgny5cBUieiWEwWUNoPVNHNherHSNsJOg4qB</b>
