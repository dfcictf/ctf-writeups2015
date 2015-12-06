Deskripsi soal:
<pre>
ex1
Cipher:PXFR}QIVTMSZCNDKUWAGJB{LHYEO
Plain: ABCDEFGHIJKLMNOPQRSTUVWXYZ{}

ex2
Cipher:EV}ZZD{DWZRA}FFDNFGQO
Plain: {HELLOWORLDSECCONCTF}

quiz
Cipher:A}FFDNEVPFSGV}KZPN}GO
Plain: ?????????????????????
</pre>
<h3>Solved by snoww0lf</h3>
Ini adalah salah satu tantangan yang paling mudah di event CTF SECCON 2015, jenis cipher ini hanya melakukan substitution berdasarkan
pola yang sudah dijelaskan pada bagian cipher sebelumnya. Dengan menggunakan python berikut untuk mempercepat proses mengembalikan cipher ke teks yang sebenarnya.

```python
cipher = "A } F F D N E V P F S G V } K Z P N } G O"
pola = {
	'P':'A',
	'X':'B',
	'F':'C',
	'R':'D',
	'}':'E',
	'Q':'F',
	'I':'G',
	'V':'H',
	'T':'I',
	'M':'J', 
	'S':'K',
	'Z':'L',
	'C':'M', 
	'N':'N',
	'D':'O',
	'K':'P',
	'U':'Q',
	'W':'R',
	'A':'S',
	'G':'T',
	'J':'U',
	'B':'V',
	'{':'W',
	'L':'X',
	'H':'Y',
	'Y':'Z',
	'E':'{',
	'O':'}',
}
# inverse_pola = {a: b for a, b in pola.items()}
flag = ""
for i in cipher.split():
	flag += pola[i]
print ''.join(flag.split())
```
Flag: <b>SECCON{HACKTHEPLANET}</b>
