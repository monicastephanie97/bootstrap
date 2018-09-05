# Bootstrap

Bootstrap adalah teknik untuk mengambil sampel dari dataset secara acak. Konsep dasar dari bootstrap adalah mengambil elemen dari dataset secara random (dengan pengembalian) dan mengulanginya secara beberapa kali. Sehingga, kita akan memiliki sebuah kelompok berisi sampel Bootstrap.

Dalam coding ini, __ratio__ dibutuhkan untuk menentukan berapa jumlah elemen yang akan kita ambil dari dataset. Sedangkan __size__ adalah ukuran sampel bootstrap atau berapa kali kita akan mengulang percobaan kita.

## Apa yang akan dipakai di coding ini?

Dataset yang kita pakai disini adalah vektor berukuran 20 berisi bilangan bulat random dengan nilai 1 sampai 9. Pada coding ini, kita akan menghitung rata-rata (mean) dari sampel-sampel bootstrap dan membandingkan hasilnya dengan nilai rata-rata sebenarnya (dihitung langsung dari dataset). Ratio yang dipilih adalah 0,5. Artinya, kita akan mengambil 10 elemen dari dataset lalu menghitung rata-ratanya. Percobaan ini akan kita ulang sebanyak __size__ kali. Lalu, di setiap percobaan, rata-ratanya akan disimpan didalam suatu array. Terakhir, kita akan menghitung rata-rata dari array berisi rata-rata ini.

Dapat dilihat bahwa semakin besar sampel bootstrap, semakin besar pula akurasinya.


## Input:
- Ratio
- Size

## Output:
- Sample Size, Mean

## Cara pakai:
1. Input manual ratio
2. Input manual size
3. _Run your code_!

Notes: Dataset bisa diganti sesuka hati :)