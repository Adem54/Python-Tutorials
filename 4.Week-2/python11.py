# Burda şuna dikkat edelim biz aynı işlemi ayrı ayrı yazmak yerine o işlem için bir kere fonksiyon oluşturduk ve
# o fonksiyonu iki yerde de kullanarak işimizi kolaylaşıtıyoruz



def gecebilir(not1, not2, not3):
    if (not1 + not2 + not3) / 3 > 2.5 and not3 > 2.1:
        return True;
    else:
        return False;


def kalanlar(ogrenciler):
    kalanlar = []

    for ogrenci in ogrenciler:
        not1 = ogrenci[1]
        not2 = ogrenci[2]
        not3 = ogrenci[3]

        if not gecebilir(not1, not2, not3):
            kalanlar.append(ogrenci)

    return kalanlar


def gecenler(ogrenciler):
    gecenler = []

    for ogrenci in ogrenciler:
        not1 = ogrenci[1]
        not2 = ogrenci[2]
        not3 = ogrenci[3]

        if gecebilir(not1, not2, not3):
            gecenler.append(ogrenci)

    return gecenler


ogrenciler = [["baris", 3.5, 4, 2], ["ayse", 3, 4, 4], ["onur", 0, 2.85, 3]]
print(gecenler(ogrenciler))
print(kalanlar(ogrenciler))
