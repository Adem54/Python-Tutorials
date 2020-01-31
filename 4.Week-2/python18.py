# Verilen iki listenin ortak elemanlarını bulan kesisim bir fonksiyon yazın.

def kesisim(liste1, liste2):
    yeni_liste = []
    for eleman1 in liste1:
        for eleman2 in liste2:
            if eleman1 == eleman2:
                yeni_liste.append(eleman1)
    return yeni_liste


def kesisim(liste1, liste2):
    sonuc = []
    for sayi in liste1:
        if sayi in liste2:
            sonuc.append(sayi)

    return sonuc


print(kesisim([2, 3, 4, 5, 6], [32, 23, 4, 15, 6]))
