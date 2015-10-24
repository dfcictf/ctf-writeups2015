Deskripsi soal:

<pre>
The state of art on encryption, can you defeat it?
CjBPewYGc2gdD3RpMRNfdDcQX3UGGmhpBxZhYhFlfQA= 
</pre>

Dari soal yang ada , kita harus bisa memecahkan enkripsi yang di encode base64 ini <b>CjBPewYGc2gdD3RpMRNfdDcQX3UGGmhpBxZhYhFlfQA=</b>
Jika kita secara langsung mendecode base64 tersebut , maka hasil yang diterima adalah: 0O{shti1_t7_uhiabe}.

Melihat kembali ke source code python yang didownload. 
```python
import struct
import sys
import base64

if len(sys.argv) != 2:
    print "Usage: %s data" % sys.argv[0]
    exit(0)

data = sys.argv[1]
padding = 4 - len(data) % 4
if padding != 0:
    data = data + "\x00" * padding

result = []
blocks = struct.unpack("I" * (len(data) / 4), data)
for block in blocks:
    result += [block ^ block >> 16]

output = ''
for block in result:
    output += struct.pack("I", block)

print base64.b64encode(output)
```

Terlihat bahwa algoritma untuk meng-encrypt hasil inputan adalah melakukan proses XOR terhadap bagian blocknya sendiri dan kemudian melakukan right shift sebanyak 16 lalu menampung hasilnya pada variabel result.
Setelah data tertampung pada list result maka kembali proses loop dibagian bawah melakukan proses perubahan tiap - tiap data pada list kedalam bentuk karakter ter-obfuscate oleh proses tadi yang kemudian di encode kedalam base64.
Untuk melakukan recover dan mengembalikan ke bentuk Plain-text aslinya, maka cara yang digunakan ialah merubah sedikit bagian dari algoritma encryptnya. Berikut code python yang saya ubah sedikit :

```python
import struct
import base64

def encrypt(data):
	padding = 4 - len(data) % 4
	if padding != 0:
	    data = data + "\x00" * padding

	result = []
	blocks = struct.unpack("I" * (len(data) / 4), data)
	for block in blocks:
	    result += [block ^ block >> 16]
	    print block
	#print blocks
	#print result
	output = ''
	for block in result:
	    output += struct.pack("I", block)

	print base64.b64encode(output)

def decrypt(data):
	result = ""
	decode_b64 = base64.b64decode(data)
	print "Base64 decoded: ", decode_b64
	blocks = struct.unpack("I" * (len(decode_b64) / 4), decode_b64)
	for block in blocks:
		result += struct.pack("I", block ^ block >> 16)
		print result
	print "Found flag: %s" % (result)

def main():
	sample_plain = "AABBCCDDEEFFGG"
 	enc = "CjBPewYGc2gdD3RpMRNfdDcQX3UGGmhpBxZhYhFlfQA="
	
	#encrypt(sample_plain)
	decrypt(enc)

if __name__ == '__main__':
	main()
```

<h3>Output</h3>
<pre>
Base64 decoded:  
0O{shti1_t7_uhiabe}
EKO{
EKO{unsh
EKO{unshifti
EKO{unshifting_t
EKO{unshifting_the_u
EKO{unshifting_the_unshi
EKO{unshifting_the_unshiftab
EKO{unshifting_the_unshiftable}
Found flag: EKO{unshifting_the_unshiftable}
</pre>
Flag: <b>EKO{unshifting_the_unshiftable}</b>
