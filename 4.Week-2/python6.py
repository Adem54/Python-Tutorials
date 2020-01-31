# 1 ile n arasındaki bütün tek sayıları bulan bir kod yazmak istiyoruz. Bunun için  tek_sayilari_listele
# adında bir fonksiyon tanımlayacağız.
# 1-n arasındaki tek sayıları bulup bir liste olarak dönen tek_sayilari_listele fonksiyonunu yazın.


def tek_sayilari_listele(n):
    liste = []
    for index in range(1, n):
        if index % 2 != 0:
            liste.append(index)
    return liste


print(tek_sayilari_listele(20))
