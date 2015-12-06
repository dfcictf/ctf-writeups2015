Deskripsi soal:
<pre>
Please win 1000 times in rock-paper-scissors
rps.apk ( http://scontents.quals.seccon.jp/files/rps.apk )
</pre>
<h3>Solved by snoww0lf</h3>

Ini adalah soal reverse-engineering apk yang terbilang cukup mudah, sebelum itu saya melakukan decompiling terhadap file apk tersebut.
Disini saya menggunakan dex2jar-2.0	untuk merubah file .dex menjadi .jar agar dapat di analisa pada aplikasi jd-gui.

```bash
snoww0lf:dex2jar-2.0 root# ./d2j-dex2jar.sh classes_SECCON.dex
dex2jar classes_SECCON.dex -> ./classes_SECCON-dex2jar.jar
```
Baik, file .jar sudah terbuat. Maka saatnya melakukan pengecekan apakah hasil decompile terjadi corrupt atau tidak.
Ditemukan package yang menarik untuk dianalisa, setelah dibuka ternyata aman dan tidak terjadi corrupt. 
<pre>
com.example.seccon2015.rock_paper_scissors;
</pre>
Disini saya akan mencoba untuk menganalisa class MainActivity dan berikut kode yang didapat dari hasil decompiling.

```java
package com.example.seccon2015.rock_paper_scissors;

import android.app.Activity;
import android.os.Bundle;
import android.os.Handler;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;
import java.util.Random;

public class MainActivity
  extends Activity
  implements View.OnClickListener
{
  Button P;
  Button S;
  int cnt = 0;
  int flag;
  private final Handler handler = new Handler();
  int m;
  int n;
  Button r;
  private final Runnable showMessageTask = new Runnable()
  {
    public void run()
    {
      TextView localTextView = (TextView)MainActivity.this.findViewById(2131492946);
      MainActivity localMainActivity;
      if (MainActivity.this.n - MainActivity.this.m == 1)
      {
        localMainActivity = MainActivity.this;
        localMainActivity.cnt += 1;
        localTextView.setText("WIN! +" + String.valueOf(MainActivity.this.cnt));
      }
      for (;;)
      {
        if (1000 == MainActivity.this.cnt) {
          localTextView.setText("SECCON{" + String.valueOf((MainActivity.this.cnt + MainActivity.this.calc()) * 107) + "}");
        }
        MainActivity.this.flag = 0;
        return;
        if (MainActivity.this.m - MainActivity.this.n == 1)
        {
          MainActivity.this.cnt = 0;
          localTextView.setText("LOSE +0");
        }
        else if (MainActivity.this.m == MainActivity.this.n)
        {
          localTextView.setText("DRAW +" + String.valueOf(MainActivity.this.cnt));
        }
        else if (MainActivity.this.m < MainActivity.this.n)
        {
          MainActivity.this.cnt = 0;
          localTextView.setText("LOSE +0");
        }
        else
        {
          localMainActivity = MainActivity.this;
          localMainActivity.cnt += 1;
          localTextView.setText("WIN! +" + String.valueOf(MainActivity.this.cnt));
        }
      }
    }
  };
  
  static
  {
    System.loadLibrary("calc");
  }
  
  public native int calc();
  
  public void onClick(View paramView)
  {
    if (this.flag == 1) {
      return;
    }
    this.flag = 1;
    ((TextView)findViewById(2131492946)).setText("");
    TextView localTextView1 = (TextView)findViewById(2131492944);
    TextView localTextView2 = (TextView)findViewById(2131492945);
    this.m = 0;
    this.n = new Random().nextInt(3);
    int i = this.n;
    localTextView2.setText(new String[] { "CPU: Paper", "CPU: Rock", "CPU: Scissors" }[i]);
    if (paramView == this.P)
    {
      localTextView1.setText("YOU: Paper");
      this.m = 0;
    }
    if (paramView == this.r)
    {
      localTextView1.setText("YOU: Rock");
      this.m = 1;
    }
    if (paramView == this.S)
    {
      localTextView1.setText("YOU: Scissors");
      this.m = 2;
    }
    this.handler.postDelayed(this.showMessageTask, 1000L);
  }
  
  protected void onCreate(Bundle paramBundle)
  {
    super.onCreate(paramBundle);
    setContentView(2130968600);
    this.P = ((Button)findViewById(2131492941));
    this.S = ((Button)findViewById(2131492943));
    this.r = ((Button)findViewById(2131492942));
    this.P.setOnClickListener(this);
    this.r.setOnClickListener(this);
    this.S.setOnClickListener(this);
    this.flag = 0;
  }
}
```
Ini adalah permainan RPS ( Rock, Paper, Scissors ). Dimana CPU melakukan random choice dengan apa yang dikeluarkan nantinya, jadi pola
apa yang akan dikeluarkan CPU akan sangat sulit untuk kita tebak, mengingat pada package ini juga mengimport library java.util.Random.

Mencoba menganalisa lebih jauh ternyata ada hal yang cukup menarik disini yaitu pada bagian berikut ini.

```java
if (1000 == MainActivity.this.cnt) {
    localTextView.setText("SECCON{" + String.valueOf((MainActivity.this.cnt + MainActivity.this.calc()) * 107) + "}");
}
```
Terlihat apabila variable cnt bernilai 1000 maka kita akan mendapatkan flagnya. Syarat untuk mendapat nilai 1000 kita harus dapat memenangkan pertandingan 
sebanyak 1000 set tanpa ada kekalahan sedikitpun. Tapi, saya rasa sangat sulit mengingat fungsi random tersebut digunakan dan polanya tidak dapat di tebak.

Mengingat hal tersebut cukup mustahil, maka kita lihat bagian berikut ini yang menurut saya sangat menarik. 

```java
localTextView.setText("SECCON{" + String.valueOf((MainActivity.this.cnt + MainActivity.this.calc()) * 107) + "}");
```

Apabila kita perhatikan dengan seksama, formula dari flag yang digunakan ialah.
<pre>
(1000 + n) * 107
</pre>

Nilai dari "n" belum dapat kita ketahui, setelah menganalisa method calc() ternyata ada sebuah "Shared Library" yang dipanggil dengan nama "calc".
Untuk itu saya kembali ke workspace hasil decompile sebelumnya, dan menganalisa direktori "lib" dan mencoba melakukan reverse-engineering terhadap file "libcalc.so" pada direktori x86.

Disini saya melakukan reverse-engineering menggunakan Hopper Dissasembler v3. Ditemukan beberapa function menarik dengan nama 
Java_com_example_seccon2015_rock_1paper_1scissors_MainActivity_calc.

Mencoba menganalisa kode assemblynya.

```assembly
00000400         mov        eax, 0x7
00000405         ret        
```

Atau jika dijadikan pseudocode, hasilnya lebih enak dibaca.

```C
int Java_com_example_seccon2015_rock_1paper_1scissors_MainActivity_calc() {
    return 0x7;
}
```

Ah, ternyata cukup mudah function tersebut hanya melakukan "return" bernilai 0x7 ( 7 dalam desimal ). Dalam hal ini, nilai "n" tadi sudah kita dapatkan yaitu bernilai 0x7.
Kemudian saya gunakan python untuk menyelesaikan formulanya.

```python
python -c 'print "SECCON{"+str((1000+0x7)*107)+"}"'
```

Flag: <b>SECCON{107749}</b>

