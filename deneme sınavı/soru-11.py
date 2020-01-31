# soru-11

urun_fiyat_listesi = [["canta", 50], ["ayakkabi", 65], ["ceket", 100]]


def fiyat_guncelleme(liste, zam):
    for eleman in liste:
        eleman[1] = eleman[1] + zam
    return liste


print(fiyat_guncelleme(urun_fiyat_listesi, 10))
