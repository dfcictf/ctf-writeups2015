Deskripsi soal:
<pre>
login.pwn.seccon.jp:10000
</pre>
<h3>Solved by snoww0lf</h3>
Pada tantangan kali ini, kita hanya diberikan sebuah url dengan port yang sudah ditentukan. Mengakses url tersebut lumayan lambat, jadi harus cukup sabar
untuk menunggu hingga seluruh halaman ter-load dengan sempurna. Di halaman tersebut, nampak kalimat yang menyerupai flagnya tetapi banyak sekali padding yang cukup menggangu dan tidak berguna.
Solusinya saya menggunakan python untuk memperbaiki kalimat flag tersebut agar menjadi kalimat yang mudah untuk dibaca dan valid saat di-submit di sistem submissionnya.

Berikut kode pythonnya.

```python
def main():
	str_flag = "S E C C O N { S o m e t i m e s _ w h a t _ y o u _ s e e _ i s _ N O T _ w h a t _ y o u _ g e t } "
	print "Flag: ",''.join(str_flag.split()).replace("\x08", "")
	
if __name__ == '__main__':
	main()
```

Flag: <b>SECCON{Sometimes_what_you_see_is_NOT_what_you_get}</b>
