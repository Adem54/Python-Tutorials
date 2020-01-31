"""
Bir şehirdeki nufus orani simdikiNufus olarak ifade ediliyor. Yıllık artış yüzdesi yillikArtisYuzdesi
ise ve her yıl yillikGelenSayisi yeni kişi geliyor ise;

Belirli bir hedef nufusuna (hedefNufus) ulasmak  icin gereken yil sayisini fonksiyon kullanarak hesaplayiniz.
Fonksiyonunuz, simdikiNufus , yillikArtisYuzdesi, yillikGelenSayisi ve hedefNufus degerlerini parametre
 olarak alıp, yıl değerini dönsün.
"""


def gerekenYilSayisi(simdikiNufus, yilikArtisYuzdesi, yillikGelenSayisi, hedefNufus):
    sayac = 0
    while simdikiNufus < hedefNufus:
        simdikiNufus = simdikiNufus + (simdikiNufus * (yilikArtisYuzdesi / 100)) + yillikGelenSayisi
        sayac += 1
    return sayac
    # burayi doldurun


simdikiNufus = int(input('Simdiki Nufus'))
yillikArtisYuzdesi = int(input('Yilik Artis Yuzdesi'))
yillikGelenSayisi = int(input('Yillik Gelen Sayisi'))
hedefNufus = int(input('Hedef Nufus'))
print(gerekenYilSayisi(simdikiNufus, yillikArtisYuzdesi, yillikGelenSayisi, hedefNufus))
