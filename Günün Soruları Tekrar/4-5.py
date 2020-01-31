"""
[['ocak', -5, 2, 2, -3, 4, 0, 5, 1, 4, 1, -3, 2, -1, 4, 1, 5, 4, -1, 5, -5, -5, -3, -2, 4, 2, -2, -3, 2, 5, 0, -4],
['subat', -7, -1, 2, -2, 3, -6, 0, 2, 2, -7, -4, -1, 1, 1, 0, -1, -4, -3, 1, -2, 1, -2, -7, -6, -2, 3, 0, -7],
['mart', 3, 3, 7, 4, 0, 1, 7, 5, -1, 0, 7, 5, 0, 3, 1, 4, 4, 4, -1, 0, 0, 3, 0, 5, 5, 1, 1, 0, 4, 2, 6],
['nisan', 2, 11, 12, 10, 10, 9, 10, 4, 12, 12, 5, 3, 12, 2, 4, 8, 7, 9, 10, 4, 3, 7, 2, 9, 8, 7, 2, 13, 4, 15],
['mayis', 16, 17, 14, 9, 7, 7, 9, 10, 19, 16, 5, 9, 17, 14, 10, 17, 16, 10, 16, 11, 6, 18, 19, 5, 19, 20, 13,
17, 8, 21, 6],
['haziran', 24, 18, 25, 18, 20, 24, 25, 17, 21, 20, 24, 20, 21, 22, 25, 22, 24, 20, 22, 21, 23,
21, 24, 20, 23, 25, 17, 21, 21, 20],
['temmuz', 35, 34, 37, 33, 36, 39, 29, 30, 38, 34, 36, 40, 37, 36, 33, 34,
 31, 33, 35, 36, 29, 39, 36, 27, 34, 31, 27, 28, 39, 33, 35],
['agustos', 35, 33, 32, 30, 29, 32, 30, 30, 32,
  26, 26, 31, 28, 28, 34, 25, 26, 30, 33, 35, 25, 28, 30, 28, 34, 30, 32, 34, 26, 34, 27],
['eylul', 17, 20,
  20, 24, 17, 15, 19, 21, 20, 24, 15, 18, 17, 15, 25, 19, 15, 22, 21, 24, 21, 15, 21, 24, 15, 15, 22, 22, 20, 19],
['ekim', 17, 16, 17, 20, 11, 12, 10, 15, 14, 20, 20, 19, 10, 16, 17, 12, 17, 19, 14, 13, 18, 16, 13, 17, 13,
    12, 14, 11, 16, 16, 16],
['kasim', 7, 6, 4, 10, 9, 4, 4, 8, 5, 5, 5, 6, 9, 10, 9, 9, 5, 9, 3, 4, 7, 10, 4,
    8, 3, 7, 8, 10, 6, 3],
['aralik', 0, 2, -1, 3, 1, 1, 6, 2, 3, -1, 8, 6, 5, 1, 7, 8, 0, 1, -1, 5, 0, -1,
     3, 1, 6, 7, 8, 2, 6, 5, 5]]



Verilen ekteki yillik_sicaklik_verisi bilgisine gore:
1- Her ayin ortalama sicakligini
2- Yillin sicaklik ortalamasi en yuksek ayini
3- Yilin sicaklik ortalamasi en dusuk ayini
4- Yilin en sicak gun ya da gunlerini
5  Yilin en soguk gun ya da gunlerini ekrana yazdiran  python programini yaziniz.
"""

sicaklik_verileri = [
    ['ocak', -5, 2, 2, -3, 4, 0, 5, 1, 4, 1, -3, 2, -1, 4, 1, 5, 4, -1, 5, -5, -5, -3, -2, 4, 2, -2, -3, 2, 5, 0, -4],
    ['subat', -7, -1, 2, -2, 3, -6, 0, 2, 2, -7, -4, -1, 1, 1, 0, -1, -4, -3, 1, -2, 1, -2, -7, -6, -2, 3, 0, -7],
    ['mart', 3, 3, 7, 4, 0, 1, 7, 5, -1, 0, 7, 5, 0, 3, 1, 4, 4, 4, -1, 0, 0, 3, 0, 5, 5, 1, 1, 0, 4, 2, 6],
    ['nisan', 2, 11, 12, 10, 10, 9, 10, 4, 12, 12, 5, 3, 12, 2, 4, 8, 7, 9, 10, 4, 3, 7, 2, 9, 8, 7, 2, 13, 4, 15],
    ['mayis', 16, 17, 14, 9, 7, 7, 9, 10, 19, 16, 5, 9, 17, 14, 10, 17, 16, 10, 16, 11, 6, 18, 19, 5, 19, 20, 13,
     17, 8, 21, 6],
    ['haziran', 24, 18, 25, 18, 20, 24, 25, 17, 21, 20, 24, 20, 21, 22, 25, 22, 24, 20, 22, 21, 23,
     21, 24, 20, 23, 25, 17, 21, 21, 20],
    ['temmuz', 35, 34, 37, 33, 36, 39, 29, 30, 38, 34, 36, 40, 37, 36, 33, 34,
     31, 33, 35, 36, 29, 39, 36, 27, 34, 31, 27, 28, 39, 33, 35],
    ['agustos', 35, 33, 32, 30, 29, 32, 30, 30, 32,
     26, 26, 31, 28, 28, 34, 25, 26, 30, 33, 35, 25, 28, 30, 28, 34, 30, 32, 34, 26, 34, 27],
    ['eylul', 17, 20,
     20, 24, 17, 15, 19, 21, 20, 24, 15, 18, 17, 15, 25, 19, 15, 22, 21, 24, 21, 15, 21, 24, 15, 15, 22, 22, 20, 19],
    ['ekim', 17, 16, 17, 20, 11, 12, 10, 15, 14, 20, 20, 19, 10, 16, 17, 12, 17, 19, 14, 13, 18, 16, 13, 17, 13,
     12, 14, 11, 16, 16, 16],
    ['kasim', 7, 6, 4, 10, 9, 4, 4, 8, 5, 5, 5, 6, 9, 10, 9, 9, 5, 9, 3, 4, 7, 10, 4,
     8, 3, 7, 8, 10, 6, 3],
    ['aralik', 0, 2, -1, 3, 1, 1, 6, 2, 3, -1, 8, 6, 5, 1, 7, 8, 0, 1, -1, 5, 0, -1,
     3, 1, 6, 7, 8, 2, 6, 5, 5]]
"""
Verilen ekteki yillik_sicaklik_verisi bilgisine gore:
1- Her ayin ortalama sicakligini
2- Yillin sicaklik ortalamasi en yuksek ayini
3- Yilin sicaklik ortalamasi en dusuk ayini
4- Yilin en sicak gun ya da gunlerini
5  Yilin en soguk gun ya da gunlerini ekrana yazdiran  python programini yaziniz.
"""
# elimizde bir dizi ve o dizi içerisinde diziler var ve içerdeki dizilerde sadece 0.indis ay adı diğerleri
# ise günlük sıcaklık değerleridir

aylik_sicaklik_ortalamalar = []
for aylik_sicaklik_listesi in sicaklik_verileri:
    counter = 0
    toplam = 0
    ay_sicaklik_ort = []
    for sicaklik_deger in aylik_sicaklik_listesi:
        if type(sicaklik_deger) == str:
            ay_adi = sicaklik_deger
        if type(sicaklik_deger) != str:
            counter += 1
            toplam += sicaklik_deger

    ortalama = round((toplam / counter), 2)
    ay_sicaklik_ort.append(ay_adi)
    ay_sicaklik_ort.append(ortalama)
    aylik_sicaklik_ortalamalar.append(ay_sicaklik_ort)

print(aylik_sicaklik_ortalamalar)

ocak = ["ocak", -5, 2, 2, -3, 4, 0, 5, 1, 4, 1, -3, 2, -1, 4, 1, 5, 4, -1, 5, -5, -5, -3, -2, 4, 2, -2, -3, 2, 5, 0, -4]
subat = ["subat", -7, -1, 2, -2, 3, -6, 0, 2, 2, -7, -4, -1, 1, 1, 0, -1, -4, -3, 1, -2, 1, -2, -7, -6, -2, 3, 0, -7]


# her bir ayın ortalama sıcaklığğını bulan fonksiyon
def ort(liste):
    toplam = 0
    counter = 1
    ay_ad = liste[0]
    liste.remove(ay_ad)
    for deger in liste:
        toplam += deger
        ortalama = round((toplam / counter), 2)
        counter += 1
    return ortalama


print(ort(ocak))
print(ort(subat))
"""
2- Yillin sicaklik ortalamasi en yuksek ayini
3- Yilin sicaklik ortalamasi en dusuk ayini
"""
max_sicaklik = -100
min_sicaklik = 100
yil_max_min_sic_ortalama = []
for ay_sicaklik_degerler in sicaklik_verileri:
    sicaklik_ortalama = ort(ay_sicaklik_degerler)
    if sicaklik_ortalama > max_sicaklik:
        max_sicaklik = sicaklik_ortalama
    elif sicaklik_ortalama < min_sicaklik:
        min_sicaklik = sicaklik_ortalama

print("max-sicaklik: " + str(max_sicaklik))
print("min-sicaklik:" + str(min_sicaklik))

# 2)


# Ay ay her ayın en düşük ve en yüksek sıcaklıklarını buluyourz



