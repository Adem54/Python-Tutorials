from python1 import asal_mi

# Verilen bir sayının  asal çarpanlarını bulan fonksiyonu yazalım
asal_mi(34)


def asal_carpan_bul(sayi):
    asal_carpanlar = []
    bolen = 2
    while bolen < sayi:
        if sayi % bolen == 0 and asal_mi(bolen):
            asal_carpanlar.append(bolen)
        bolen = bolen + 1
    return asal_carpanlar


print(asal_carpan_bul(210))
