# Not ortalaması 2.5 tan büyük olanlar geçmiş sayılacak gecenler fonksiyonu yazınız

def gecenler(liste):
    gecen_isimler = []
    for ogrenci in liste:
        not_sayisi = len(ogrenci) - 1
        not_ortalamasi = (ogrenci[1] + ogrenci[2] + ogrenci[3]) / not_sayisi
        if not_ortalamasi > 2.5 and ogrenci[3] > 2.1:
            gecen_ogrenci_ismi = ogrenci[0]
            gecen_isimler.append(gecen_ogrenci_ismi)
    return gecen_isimler


ogrenciler = [["baris", 3.5, 4, 2], ["ayse", 3, 4, 4], ["onur", 0, 2.85, 3]]
print(gecenler(ogrenciler))


def kalanlar(list):
    kalan_isimler = []
    for ogrenci in list:
        not1 = ogrenci[1]
        not2 = ogrenci[2]
        not3 = ogrenci[3]
        not_sayisi = len(ogrenci) - 1
        if (not1 + not2 + not3) / not_sayisi < 2.5:
            kalan_ogrenci = ogrenci[0]
            kalan_isimler.append(kalan_ogrenci)
    return kalan_isimler


ogrenciler = [["baris", 3.5, 4, 2], ["ayse", 3, 4, 4], ["onur", 0, 2.85, 3]]
print(kalanlar(ogrenciler))
