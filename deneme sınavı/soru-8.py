"""
Kullanicidan, kullanici "0" girine kadar surekli yeni bir tam  sayi alan ve bu sayilarin ortalamasini
ekrana yazdiran python programini yaziniz.

Programin sayi girisini sonlandiran "0" rakamini ortalamaya dahil etmeyin

Kullanicinin  tam sayi haricinde bir veri girmedigini varsayabilirsiniz.

Ilk program outputunda goreceginiz gibi kullanici 1, 2, 3, 4, 5 ve 0 rakamlarini giriyor

program 1, 2, 3,4,5 sayilarinin ortalamasini aliyor. 0'i ortalamaya dahil etmiyor

Ornek Program Outputu -1
"""
# Soru-8
sayi = ""
toplam = 0
ortalama = 0
sayac = 1
while sayi != 0:
    sayi = int(input("Bir sayi gir"))
    if sayi == 0 and sayac == 1:
        ortalama = 0.0
    if sayi != 0:
        toplam = toplam + sayi
        ortalama = toplam / sayac
        sayac += 1

print("Ortalama = " + str(ortalama))
