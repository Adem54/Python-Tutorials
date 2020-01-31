"""
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
    ['haziran', 24, 18, 25, 18, 20, 40, 25, 17, 21, 20, 24, 20, 21, 22, 25, 22, 24, 20, 22, 21, 23,
     21, 24, 20, 23, 25, 17, 21, 40, 20],
    ['temmuz', 35, 34, 37, 33, 36, 39, 29, 30, 38, 34, 36, 40, 37, 36, 33, 34,
     31, 33, 35, 36, 29, 39, 36, 27, 34, 31, 27, 28, 39, 33, 35],
    ['agustos', 40, 33, 32, 30, 29, 32, 30, 30, 32,
     26, 26, 31, 28, 28, 34, 25, 26, 30, 33, 40, 25, 28, 30, 28, 34, 30, 32, 34, 26, 34, 27],
    ['eylul', 17, 20,
     20, 24, 17, 15, 19, 21, 20, 24, 15, 18, 17, 15, 25, 19, 15, 22, 21, 24, 21, 15, 21, 24, 15, 15, 22, 22, 20, 19],
    ['ekim', 17, 16, 17, 20, 11, 12, 10, 15, 14, 20, 20, 19, 10, 16, 17, 12, 17, 19, 14, 13, 18, 16, 13, 17, 13,
     12, 14, 11, 16, 16, 16],
    ['kasim', 7, 6, 4, 10, 9, 4, 4, 8, 5, 5, 5, 6, 9, 10, 9, 9, 5, 9, 3, 4, 7, 10, 4,
     8, 3, 7, 8, 10, 6, 3],
    ['aralik', 0, 2, -1, 3, 1, 1, 6, 2, 3, -1, 8, 6, 5, 1, 7, 8, 0, 1, -1, 5, 0, -1,
     3, 1, 6, 7, 8, 2, 6, 5, 5]]

"""
for aylik_sicaklik_verileri in sicaklik_verileri:
    counter = 1
    max_sicaklik
"""

agustos = ['agustos', 35, 33, 32, 30, 29, 32, 30, 30, 32,
           26, 26, 31, 28, 28, 34, 25, 26, 30, 33, 35, 25, 28, 30, 28, 34, 30, 32, 34, 26, 34, 27]


# en büyük sicaklikları birden fazla ise hangi günler kaçıncı günelerine denk geliyor onu bul ve min günleri de
# aynı şekilde birden fazla ise kaçıncı günlerine denk geliyor onu bul
def max_sicaklik_degerleri(liste):
    max_sicaklik = -100
    min_sicaklik = 100
    for sicaklik in liste:

        if type(sicaklik) != str:

            if sicaklik > max_sicaklik:
                max_sicaklik = sicaklik

            elif sicaklik < min_sicaklik:
                min_sicaklik = sicaklik

    ay_max_sicaklik_gunleri = []
    ay_min_sicaklik_gunleri = []
    max_sicaklik_gunleri = []
    min_sicaklik_gunleri = []
    for sayi in range(len(liste)):
        sicaklik = liste[sayi]
        if sicaklik == max_sicaklik:
            max_sicaklik_gunleri.append(sayi)
        if sicaklik == min_sicaklik:
            min_sicaklik_gunleri.append(sayi)
    ay_max_sicaklik_gunleri.append(liste[0])
    ay_max_sicaklik_gunleri.append(max_sicaklik)
    ay_max_sicaklik_gunleri.append(max_sicaklik_gunleri)
    ay_min_sicaklik_gunleri.append(min_sicaklik)
    ay_min_sicaklik_gunleri.append(min_sicaklik_gunleri)
    return ay_max_sicaklik_gunleri

# Bir liste içindeki birden fazla max değer varsa onları bize getiren fonksiyonu yazdık...
print(max_sicaklik_degerleri(agustos))
max_sicak = -100
for sicaklik_degerleri in sicaklik_verileri:
    max_sicaklik_deger = max_sicaklik_degerleri(sicaklik_degerleri)
    for max_sicaklik in max_sicaklik_deger:
        if type(max_sicaklik) == int:
            if max_sicaklik > max_sicak:
                max_sicak = max_sicaklik
                max_sicaklik_deger_son = max_sicaklik_deger

print(max_sicak)
print(max_sicaklik_deger_son)
# burda şuna bakalım eğer aylar içerisinde max sicaklik değeri meseala 40 derece sıcaklik birden fazla var
# o zaman nasıl yapmalıyız
max_sicaklik_aylar = []
for sicaklik_degerleri in sicaklik_verileri:
    max_sicaklik_ay_gun = []
    max_sicaklik_list_gun = []
    count = 0
    for sayi in range(len(sicaklik_degerleri)):
        sicaklik_deger = sicaklik_degerleri[sayi]
        if max_sicak == sicaklik_deger:
            max_sicaklik_list_gun.append(sayi)
    if len(max_sicaklik_list_gun)>0:
        max_sicaklik_ay_gun.append(sicaklik_degerleri[0])
        max_sicaklik_ay_gun.append(max_sicak)
        max_sicaklik_ay_gun.append(max_sicaklik_list_gun)
        max_sicaklik_aylar.append(max_sicaklik_ay_gun)


print(max_sicaklik_aylar)

"""
Eğer bir listede en büyük değeri bulmak istiyorsk ancak o listede max değerden birden fazla varsa bizde
 kaçıncı indislerde olduğu ile beraber getirmek istiyorsak o zaman yapacağımız iş şudur ki önce en büyük değeri
  bulalım hatta önce bir listede enbüyük değeri bulan fonksiyonu yazalım daha sonra da tekrar o listeyi 
  for ile döndürerek ama for ile döndürüp  indisleri gösterecek şekilde for sayi range(len(liste))  ile hem indisleri
  görelim hem de elemanları görecek şekilde for döngüsü ile max değerin hangi indislerde olduğnu bulabiliriz tamamen
   mantığımız bu yönde olmalı ve  bu sefer bir liste içinde eşit olan max değer birden fazla ise 
   onu bulan fonksiyonu da yazalım
Yani genel mantık olarak herzamn bir problemi küçük parçalara böleerek çözmeye çalışalım o şekilde işlerimiz kolaylaşıyor
"""