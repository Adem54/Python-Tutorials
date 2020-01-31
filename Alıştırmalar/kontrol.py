def armstrong_sayi(sayi):
    sayi1 = list(sayi)
    toplam = 0
    uzunluk = len(sayi)
    for rakam in sayi1:
        yeni_rakam = int(rakam) ** uzunluk
        toplam = toplam + yeni_rakam

    if int(sayi) == toplam:
        print("Bu bir armstrong_sayidir")

    else:
        print("Bu bir asmstrong sayi degildir")

    return toplam


print(armstrong_sayi("1634"))
