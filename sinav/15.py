"""
Ahmet'in dönem sonu ödevi için 250 kelimelik bir makale yazması gerekiyor.
Ahmet yazdığı metinde kaç tane kelime olduğunu öğrenmek için bir program yazmak istiyor.
Ahmet'in istediğini yapmasi için girilen inputu boşluklara göre bölen bir program yazması gerekiyor.
Verilen bir metnin içerisinde bulunan kelimeleri liste şeklinde veren kelime_parcalayici fonksiyonunu yazınız.

Not: Hazir fonsiyon kullanmayin

Örnek:

Girdi:
'Merhaba Dünya'
Çıktı:
['Merhaba', 'Dünya']
"""
# kodu buraya yazın
girdi = input('metin: ')


def kelime_parcalayici(metin):
    liste_genel = []
    liste1 = ""
    for sayi in range(len(metin)):
        harf = metin[sayi]

        char = " "
        if harf == char:
            liste_genel.append(liste1)
            liste1 = ""
        else:
            liste1 += harf

        if sayi == (len(metin) - 1):

            liste_genel.append(liste1)
    return liste_genel


print(kelime_parcalayici(girdi))
