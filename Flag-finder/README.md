Deskripsi soal:
<pre>
I've forgotten my flag. I remember it has the format "9447{<some string>}", but what could it be?
This task is sadly broken (it is too easy).
</pre>
<h3>Solved by Hamsterx</h3>
Soal yang satu ini merupakan soal pemanasan di kategori reverse enginering, pada soal ini kita diberi file ELF 64-bit LSB executable dan cari flag di dalamnya.
Hal yang saya lakukan hingga mendapat flag :
Memberi permission execute pada file ELF tadi.

```bash
chmod +x flagfinder
```

Jalankan elf tersebut

./flagfinder

Saat dijalankan akan muncul string pada layar CLI 
Usage: ./flagfinder-bbc6305273a39e9ccd751c24df86ac61 <password>
Dimana string itu merupakan panduan untuk mengkesekusi file elf ini, nah karena diminta memasukan password saya awalnya mencoba memasukan string.

./flagfinder a

Ketika saya masukan string tersebut muncul pesan error beserta flagnya.

Flag: <b>9447{C0ngr47ulaT1ons_p4l_buddy_y0Uv3_solved_the_H4LT1N6_prObL3M_n1c3_}</b>
