"""
Girilen sayıların ortalamasını bulan bir program yazacağız.

Ortalama Nasıl Hesaplanır

Ortalama hesabı belli sayıdaki rakamların toplamının, rakamların sayısına bölünmesiyle yapılır.

Örneğin; 4, 6, 2, 8 sayılarının ortalaması 20 / 4 = 5 tir.
Yazacağımız program, kullanıcıdan rakam girmesini isteyecek ve bu işlem kullanıcı sıfır girene kadar devam edecek.
 Kullanıcı sıfır girdiğinde, o ana kadar girilmiş olan rakamların ortalamasını gösterecek.
"""

toplam = 0
girilen_rakam_sayisi = 0
sayi = int(input('Bir sayı gir?'))
sayac = 1
while sayi != 0:
    toplam = toplam + sayi
    ortalama = toplam / sayac
    print(str(sayac) + " sayının ortalaması " + str(ortalama) + " dır")
    sayac += 1
    sayi = int(input('Bir sayı gir?'))
