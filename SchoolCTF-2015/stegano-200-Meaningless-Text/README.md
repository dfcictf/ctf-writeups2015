Solve by: <b>Hamsterx & Gandiva / bl4ckb0x</b>
Deskripsi soal:
<pre>
It is absolutely meaningless text, isn't it?
http://school-ctf.org/files/task12_5b01f6a519d9a567ca098416e1499f8464e10c0c.html
</pre>
Dari link diatas kita akan diarahkan ke sebuah halaman HTML yang berisi kata-kata yang tidak terlalu mencurigakan, hmm bagaimana bila dilihat dari segi codenya, kami kemudian melihat page source dari halaman tersebut dan tebak apa yang kami temukan, ada 2 buah pola 
```bash 
"<e>zero</e>" & "<e>one</e>".
```

Kami save code tersebut kedalam sebuah file text.html, dari file tesebutlah awal petualangan dimulai, tahap demi tahap akan kami jabarkan siapkanlah gorengan dan segalon kopi manis atau susu (kalau bisa susu gantung).

<h4>Tahap 1</h4>

Memfilter pola yang sudah ditemukan tadi menggunakan grep

```bash
$ cat text.html | grep -o  "<e>[a-z]*</e>" > text_hasil.txt
```

<h4>Tahap 2</h4>

Tahap kedua ini hanya bermodal find and replace dimana kita akan mengubah pola “<e>zero</e>” menjadi 0 sedangkan “<e>one</e>” menjadi 1, lalu rapikan dan nantinya akan berbentuk binary seperti dibawah ini :

<pre>011001100110110001100001011001110101111101101001011100110101111101110100011010000110100101110011010111110110100101110011010111110110000101011111011100110110100101101101011100000110110001100101010111110111001101110100011001010110011101101111</pre>

<h4>Tahap 3</h4>

Ubah binary tersebut menjadi string, kami menggunakan fasilitas dari http://www.asciitohex.com/ untuk melakukan konfersi, nah dan apa yang kita dapat disana, voilaaa !! We got a flag 

Terima kasih www.asciitohex.com :D 

Flag: <b>flag_is_this_is_a_simple_stego</b>
