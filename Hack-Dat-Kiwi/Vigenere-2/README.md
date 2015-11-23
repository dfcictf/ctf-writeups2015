Deskripsi soal:
<pre>
Link: http://c4c045.hack.dat.kiwi/crypto_stegano/vigenere/vigenere.php?mode=2
So you got crypto skills, right? Try it again on Known Plaintext Mode:
</pre>
<b>Solved by: ArtOfS</b><br />
Pada challenges ini kami diberikan plaintext dan ciphernya. Untuk mencari keynya dapat digunakan Rumus : (Cipher-Plain)%26 dengan asumsi [A-Z]=[0-25]
Dengan sedikit pengetahuan python saya membuat skrip untuk mendapatkan keynya, berikut skripnya: 
```python
pt = 'CRYPTOGRAPHYORCRYPTOLOGYF'
ct = 'ZVPDQLKIOMECFFZOCGHLISXMC'
vp,vc,key = [],[],[]

# plain to angka
for p in pt:
    vp.append(int(ord(p)-65))
# cipher to angka
for p in ct:
    vc.append(int(ord(p)-65))
# key 
c=0
for p in pt:
    key.append((chr(((vc[c]-vp[c])%26)+65)))
    c+=1

print ('Plaintext  : ' + pt)
print ('Ciphertext : ' + ct)
print ('Key        : ' + ''.join(key))
```
Dan hasilnya :
<pre>
Plaintext  : CRYPTOGRAPHYORCRYPTOLOGYF
Ciphertext : ZVPDQLKIOMECFFZOCGHLISXMC
Key        : XEROXXEROXXEROXXEROXXEROX
</pre>
Flag: <b>XEROX</b>
