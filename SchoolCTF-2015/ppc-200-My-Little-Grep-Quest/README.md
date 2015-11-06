Solved by: <b>Wizz</b>
<br />Deskripsi soal:
<pre>
Follow the white rabbit! Khm.. I mean "file" 
http://school-ctf.org/files/start_dec1dd9b04e5e6f51e017573270dec210106031a.zip
</pre>
Pembahasan dari soal ini sebenarnya sangat simple, soal ini terdiri dari arsip dengan terdapat beberapa folder dan file txt. Silahkan extrak terlebih dulu.
Saat membuka folder “start”maka akan terdapat beberapa folder dan file start.txt.

Pada file tersebut sudah terdapat huruf pertama dari flag. File sudah berisi path atau directory lengkap ke file berikutnya. Dan tinggal membuka file berikutnya yang berisi huruf dari flag dan path dari file selanjudnya. Setelah menggabungkan huruf dari file file yg tunjukan maka akan mendapat sebuah flag.

<h3>Another Solving Method</h3>
Code by: <b>snoww0lf</b><br />
Dengan menggunakan kode python berikut, tanpa perlu melakukan metode manual kita dapat menyatukan setiap flag - flag pada masing - masing file txtnya. Dan berikut kode yang saya tulis :

```python
def search():
	flag = ''
	start = 'start.txt'
	st = True
	while st:
		with open(start, 'r') as f:
			x = f.readlines()
			c = x[0]
			start = c[6:].replace("\n", "")
			print "Membaca file %s " % (start)
			flag += x[1]
			if start == '':
				st = False
	print "Ditemukan flag: %s" % (flag)

def main():
	search()

if __name__ == '__main__':
	main()
```

<h3>Output</h3>
<pre>
Membaca file uspom/yvawi/uihcw/jukrd/ndycl.txt 
Membaca file hfxzr/xwvww/nbgku/gtllw/ghqqv/dxlzy.txt 
Membaca file xlmhr/tmjbb/ebqyr/bknuv/tazas/naehz.txt 
Membaca file jogxi/uhvfo/qfofe/krrdt/pvpdt/tvvfm.txt 
Membaca file jogxi/ffuqp/ymdld/dwyxh/pemgt/eunjh.txt 
Membaca file lgquw/dhuxg/pokut/fpyvm/cjzgt.txt 
Membaca file xlmhr/hbgww/klmeo/hwseq/gxhec/vxamr.txt 
Membaca file xlmhr/tvwzs/kqyxv/zqdnb/jtamd/nnufk.txt 
Membaca file hfxzr/nsxka/mxndz/ohtcg/jdrxx/cxxoy.txt 
Membaca file zflgw/fqeek/yfizl/oexhp/wymbi/jnjpf.txt 
Membaca file uspom/tsyrw/erblc/rkqux/aljxg/bgebn.txt 
Membaca file nqddz/nkjbd/fkftk/rwrcy/vwxqa/wpmix.txt 
Membaca file nqddz/neccl/dpnvp.txt 
Membaca file satac/olwyn/warao/ewnbf/rqeoc/whjcc.txt 
Membaca file uspom/tsyrw/nxxzp/nxogh/nvzjc/aitdh.txt 
Membaca file uspom/dzwpb/msupu/tonho/ugsxs.txt 
Membaca file jogxi/bwloc/qrapp/dcqhi/shfvv/osnsi.txt 
Membaca file satac/cuzco/rlrke/ziung/tufpp/xqlkk.txt 
Membaca file niphy/chzvq/wglln/wegig.txt 
Membaca file xlmhr/zeonb/fyktc/kiyej/tqdrq/sipsx.txt 
Membaca file hfxzr/jljfo/kyohd/djxug/glkyx/rxthg.txt 
Membaca file nqddz/neccl/zrzqs/vpley/yepgr/veopr.txt 
Membaca file  

Ditemukan flag: flag_1s_1t_w@s_t00_easy
</pre>
Flag: <b>flag_1s_1t_w@s_t00_easy</b>
