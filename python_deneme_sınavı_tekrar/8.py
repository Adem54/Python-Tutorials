"""
Kullanicidan, kullanici "0" girine kadar surekli yeni bir tam  sayi alan ve bu sayilarin ortalamasini ekrana
 yazdiran python programini yaziniz.
Programin sayi girisini sonlandiran "0" rakamini ortalamaya dahil etmeyin
Kullanicinin  tam sayi haricinde bir veri girmedigini varsayabilirsiniz.
Ilk program outputunda goreceginiz gibi kullanici 1, 2, 3, 4, 5 ve 0 rakamlarini giriyor
program 1, 2, 3,4,5 sayilarinin ortalamasini aliyor. 0'i ortalamaya dahil etmiyor
Ornek Program Outputu -1
===================================
sayi = 1
sayi = 2
sayi = 3
sayi = 4
sayi = 5
sayi = 0
Ortalama = 3.0
====================================
Ornek Program Outputu -2
==========================================
sayi = 0
Ortalama = 0.0
"""
sayi = ""
toplam = 0
counter = 0
while sayi != 0:
    sayi = int(input("Bir sayi gir"))
    if sayi != 0:
        counter += 1
    ortalama = 0
    if counter == 0 and sayi == 0:
        ortalama = 0.0

        break
    toplam += sayi
    ortalama = toplam / counter

print(ortalama)
