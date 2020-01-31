"""
Asal sayılar 1 ve kendisinden başka hiç bir sayıya bölünemeyen sayılardır.
İç içe döngüler kullanarak sayıların asal olup olmadıklarını kontrol edebilirsiniz.
1 ile 1000 arasındaki tüm asal sayıları ekrana yazdırın.
"""

sayi = 2
is_asal = False

# Burdad öncelikle bir sayının asal olup olmadığını kontrol edelim

asal_mi = int(input("Bir sayı giriniz"))
sayac = 2

if asal_mi == 2:
    print("Bu sayı asal  saydır")
while sayac < asal_mi:

    if asal_mi % sayac == 0:
        print("Bu sayı asal değildir çünkü " + str(sayac) + " 'a bölünebiliyor")
        break
    else:
        print(str(asal_mi) + " sayısı " + str(sayac) + " sayısına tam bölünemedi")
        sayac += 1
        if sayac == asal_mi:
            print(str(asal_mi) + " sayısı asaldir")


