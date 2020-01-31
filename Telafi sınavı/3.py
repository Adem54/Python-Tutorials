"""
Kullanıcıdan alınan bir metnin büyük harflerini küçük, küçük harflerini de büyük harfe çeviren bir fonksiyon yazınız.
Bu fonksiyonu yazarken hazır olarak verilen kucuk_harfler ve buyuk_harfler listelerini kullanın.
Listelerde olmayan karakterler aynı kalmalıdır.
Örneğin boşluk ' 'listelerde yok, bu nedenle değişmemelidir.
Örnek:
Input: 'Merhaba Dünya'
Output: 'mERHABA dÜNYA'
"""

kucuk_harfler = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z']
buyuk_harfler = ['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'J',
                 'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'Y', 'Z']


def harfleri_degistir(metin):
    yeni_metin = ""
    for sayi in range(len(metin)):
        eleman = metin[sayi]
        if eleman in kucuk_harfler:
            indis = kucuk_harfler.index(eleman)
            yeni_eleman = buyuk_harfler[indis]
            yeni_metin += yeni_eleman
        if eleman in buyuk_harfler:
            indis = buyuk_harfler.index(eleman)
            yeni_eleman = kucuk_harfler[indis]
            yeni_metin += yeni_eleman
        if eleman not in kucuk_harfler and eleman not in buyuk_harfler:
            yeni_eleman=eleman
            yeni_metin += yeni_eleman

    return yeni_metin


print(harfleri_degistir(input('text? ')))
