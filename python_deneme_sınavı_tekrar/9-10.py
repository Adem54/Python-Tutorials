"""
Parametre olarak bir liste alan ve geriye o listedeki eleman sayisini donen uzunluk(bir_liste) fonksiyonunu yaziniz.
"""


def uzunluk(liste):
    return len(liste)


listem = [1, 3, 5, 7, 9, 12]
print(uzunluk(listem))

"""
Parametre olarak 2 sayi alan ve geriye ilk sayi ikinci sayidan buyuk ise 1 , sayilar esitse 0,
 ilk sayi ikinci sayidan kucukse  -1
donen karsilastirma(ilk_sayi, ikinci_sayi) fonksiyonunu yaziniz.
"""


def karsilastirma(ilk_sayi, ikinci_sayi):
    result = 0
    if ilk_sayi > ikinci_sayi:
        result = 1
    elif ilk_sayi == ikinci_sayi:
        result = 0
    elif ilk_sayi < ikinci_sayi:
        result = -1
    return result


print(karsilastirma(14, 13))
