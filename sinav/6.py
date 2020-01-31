"""
Ali'nin dersi için hazırlaması gereken bir sunum vardır. Bu sunumda 5 yıl içerisinde çeşitli ülkelere
 yapılan göç miktarları yer alacaktır.  Ali'nin aynı zamanda her ülke için ayrı ayrı ortalama
 göç oranlarını ve tüm ülkelerde ki göç oranlarının ortalamasını hesaplaması gerekiyor.
Bu işlemleri yapan bir program yazınız.

(fonksiyon kullanin)

Örnekler:
1)
goc_ortalama_hesapla(['Amerika', 'Ingiltere', 'Almanya'], [[100, 200, 450, 800, 1200], [450, 390, 267, 578, 360], [460, 360, 250, 400, 900]])

Bu durumda, Amerikanın göç miktarları 100,200,450,800 ve 1200 dür.

Beklenen sonuç şu şekildedir:

Amerika: 550.0
Ingiltere: 409.0
Almanya: 474.0
Genel:  2388.3333333333335
-------------
2)
goc_ortalama_hesapla(['Irak', 'Brezilya', 'Kanada'], [[20, 35, 45, 20, 50], [300, 280, 360, 50, 20], [500, 400, 2000, 550, 790]])

Irak: 34.0
Brezilya: 202.0
Kanada: 848.0
Genel:  1806.6666666666667
"""


def ortalama(liste):
    toplam = 0
    for sayi in range(len(liste)):
        toplam += liste[sayi]
        ortala = toplam / (sayi + 1)
    return ortala


countries = ['Irak', 'Brezilya', 'Kanada']
goc_miktar = [[20, 35, 45, 20, 50], [300, 280, 360, 50, 20], [500, 400, 2000, 550, 790]]


def goc_ortalama_hesapla(ulkeler, goc_miktarlari):
    for sayi1 in range(len(ulkeler)):
        for sayi2 in range(len(goc_miktarlari)):
            if sayi1 == sayi2:
                orta = ortalama(goc_miktarlari[sayi2])
                print(ulkeler[sayi1] + ": " + str(orta))


countries = ['Irak', 'Brezilya', 'Kanada']
goc_miktar = [[20, 35, 45, 20, 50], [300, 280, 360, 50, 20], [500, 400, 2000, 550, 790]]
goc_ortalama_hesapla(countries, goc_miktar)
