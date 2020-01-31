def kalanlar(ogrenciler):
    kalanlar = []

    for ogrenci in ogrenciler:
        not1 = ogrenci[1]
        not2 = ogrenci[2]
        not3 = ogrenci[3]

        if (not1 + not2 + not3) / 3 < 2.5:
            kalanlar.append(ogrenci)

    return kalanlar


ogrenciler = [["baris", 3.5, 4, 2], ["ayse", 3, 4, 4], ["onur", 0, 2.85, 3]]
# print(gecenler(ogrenciler))
print(kalanlar(ogrenciler))
