Deskripsi soal:
<pre>
Link: http://819bc7.hack.dat.kiwi/web/math-quiz/
So I got this douchy classmate that thinks he's super cool. He created a math quiz software for our class in 10 minutes, and claims its super secure with protections and everything. We all hate him, and if you hack his code, we're gonna love you! By the way, he told a friend of mine that he keeps his secrets among the quiz questions, but those questions are never used in the software.
</pre>
<h3>Solved by: snoww0lf</h3>
Challenge ini terbilang cukup menarik, disini saya hanya melakukan sedikit lucky method untuk mendapatkan flagnya.
Pada challenge tersebut, kita diberikan 5 parameter ( berdasarkan hasil sniffing melalui Live HTTP Header ). Di tiap masing - masing parameter unik tersebut akan memperlihatkan soal / pertanyaan matematika serta index parameternya. 

Diketahui bahwa soal - soal tersebut ada 7 buah soal. Walaupun kita menyelesaikan soal tersebut seluruhnya, tapi tetap tidak akan mendapatkan flagnya. Dengan ini saya melakukan teknik bypass terhadap parameter indexnya menjadi 'unknown identity' atau identitas parameter yang tidak dikenali urutannya yang dapat memperlihatkan beberapa error serta soal yang tidak dikenali. Dimana pilihan jawaban dari soal yang tidak dikenali tersebut merupakan flagnya.

Flag: <b>second and third</b>
