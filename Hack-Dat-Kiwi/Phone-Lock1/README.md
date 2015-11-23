Deskripsi soal:
<pre>
http://819bc7.hack.dat.kiwi/web/phone-lock/
</pre>
<h3>Solved by: snoww0lf</h3>
Pada tantangan kali ini peserta diberikan sebuah url dimana kita harus menebak pola pin dari sebuah ponsel.
Di tantangan tersebut, saya coba menganalisa source-code yang terdapat didalamnya. Ditemukanlah sebuah kode javascript yang cukup menarik.

```javascript
result="";
tries=0;
locked=false;
salt="abb6f243fb340025d312c2a41cfa8beb";
valid="00a1e1072212ceae0445dcffde045da4";
//md5(salt+answer)

function buttonClick(e)
{
	if (locked) return false;
	var t=$("#result");
	t.val(t.val()+"X");
	result+=e.target.text;
	if (t.val().length>=4)
	{
		if (md5(salt+result)==valid)
		{
			alert("Flag is: "+md5(salt+result+result));
		}
		else
		{
			locked=true;
			  $("#resultHolder").effect("shake", { times:tries }, 
tries*100,function(){
				t.val("");
				result="";
				tries++;
				locked=false;
			  });
		}
	}
}

```
Ada hal yang cukup menarik disini, yakni disalah satu bagian berikut.
```javascript
if (md5(salt+result)==valid)
{
	alert("Flag is: "+md5(salt+result+result));
}
```
Untuk mendapatkan flag, formula yang digunakan cukup sederhana yaitu md5 hash yang dihasilkan dari variabel salt+result haruslah sama 
pada nilai hash yang tertampung didalam variabel valid. Tetapi yang menjadi permasalahan, kita tidak tahu angka berapa yang setelah diformulasikan
akan sama dengan nilai hash pada variabel valid.

Untuk itu, saya membuat script random number generator dengan jumlah 4 digit dengan jarak tiap nilainya yakni 0 - 9.
Berikut script penyelesaiannya : 

```python
import hashlib
import random

salt = "abb6f243fb340025d312c2a41cfa8beb"
valid = "00a1e1072212ceae0445dcffde045da4"

def load_number():
	result = ""
	for i in range(0, 4):
		result += str(random.randrange(0,10))
	return result

def main():
	stat = True
	valid_bro = ""
	while  stat:
		v = load_number()
		to_md5 = hashlib.md5((salt + v)).hexdigest()
		print "%s ( %s ) -> %s" % (to_md5, v, valid)
		if to_md5 == valid:
			valid_bro = v
			stat = False
		else:
			continue
			
	print "Password matches: %s" % (valid_bro)
	
if __name__ == '__main__':
	main()
```

Setelah script dijalankan output yang didapatkan adalah sebagai berikut: 

<pre>
.............................................................................
.............................................................................
.............................................................................
618a37ea71b515a7149bffaf40a5982c ( 5394 ) -> 00a1e1072212ceae0445dcffde045da4
0d3a69ce14add610354b22a4ff40f45c ( 5084 ) -> 00a1e1072212ceae0445dcffde045da4
2c978aa7f311263c523ce58c65678195 ( 3409 ) -> 00a1e1072212ceae0445dcffde045da4
f1f038165ceaaca47445bf0bc49de543 ( 2462 ) -> 00a1e1072212ceae0445dcffde045da4
2cabc8fa86161b057176cdd0c6689d2f ( 2990 ) -> 00a1e1072212ceae0445dcffde045da4
71ca2f11009d7662e26391aca2985b36 ( 4160 ) -> 00a1e1072212ceae0445dcffde045da4
234724de900192e6f494a46b0d8fa541 ( 1132 ) -> 00a1e1072212ceae0445dcffde045da4
8f21400b085479179f63d133361bc514 ( 4507 ) -> 00a1e1072212ceae0445dcffde045da4
e482b26d33e915d2e92f95c434c8275e ( 8884 ) -> 00a1e1072212ceae0445dcffde045da4
a624b907b7034a798b5ef0593400d561 ( 4873 ) -> 00a1e1072212ceae0445dcffde045da4
6eb2cecfed9cab621a187b2803f78457 ( 3885 ) -> 00a1e1072212ceae0445dcffde045da4
00a1e1072212ceae0445dcffde045da4 ( 1014 ) -> 00a1e1072212ceae0445dcffde045da4
Password matches: 1014
</pre>
Ditemukan password yang valid yaitu 1014, setelah mencoba menginput password tersebut pada pin ditemukan flagnya.
<br />
Flag: <b>f8cfc7a1a57dbc5f72acc70093e48c41</b>
