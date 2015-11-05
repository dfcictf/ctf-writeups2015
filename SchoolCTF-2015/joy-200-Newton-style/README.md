<h3>Solved by: snoww0lf</h3>
Deskripsi soal:
<pre>
Win the game and get the flag!
Game for linux ( http://school-ctf.org/files/task29l_a6eeaaaf605746d5beaef809945812b29f142b03.zip )
Game for windows ( http://school-ctf.org/files/task29w_1c4e393acb15cfd8d94779cb94e99dc2ce2bdbeb.zip )
</pre>
Soal ini adalah soal dengan kategori joy, binary / executable tersebut adalah sebuah game dimana pada game tersebut
kita dapat memainkan game tersebut dengan tugas player untuk menghindar dari apel - apel yang jatuh dari atas. Di salah satu menu dijelaskan apabila points
1000 maka kita akan mendapat sesuatu yang diduga kemungkinan itu adalah flagnya.

Tapi disini saya langsung mencoba untuk melakukan analisa secara statis terhadap salah satu binary yang menarik untuk dianalisa pada folder Game_Data.
Mencoba melakukan pencarian string yang terkait dengan harapan string - string tersebut tidak ter-obfuscate dan prefix menggunakan kata default yaitu "flag".
Melakukan analisa secara statis pada salah satu binary yang ada pada folder tersebut yaitu level0 dengan perintah berikut. 

```bash
strings level0 | grep flag
```

Flag: <b>flag_is_dont_let_apples_hit_your_brain</b>
