# Kullanıcın girdiği iki sayı arasındaki tek sayıların toplamını yazdırın (girilen sayılar haric).
baslangic_sayisi = int(input("Baslangic sayisini girin: "))
bitis_sayisi = int(input("Bitis sayisini girin: "))
toplam = 0
sayac = baslangic_sayisi + 1
while baslangic_sayisi < bitis_sayisi:

    baslangic_sayisi = baslangic_sayisi + 1
    if baslangic_sayisi % 2 == 1 and baslangic_sayisi < bitis_sayisi:
        toplam = toplam + baslangic_sayisi

print(toplam)

# ------------------------------------------------------------------------------

bas_sayisi = int(input("Baslangic sayisini girin: "))
bit_sayisi = int(input("Bitis sayisini girin: "))
top = 0
say = bas_sayisi + 1
while say < bit_sayisi:

    if say % 2 == 1:
        top = top + say
    say = say + 1

print("top " + str(top))
