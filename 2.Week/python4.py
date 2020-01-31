# 10 a kadar sayıları içerecek olan çarpım tablosu yapalım
my_sayac = 1
my_number = 1

while my_sayac <= 10:
    print(str(my_sayac) + " ler/lar çarpım tablosu")
    my_in_sayac = 1
    while my_in_sayac <= 10:
        my_number = my_in_sayac * my_sayac
        print(str(my_sayac) + " x " + str(my_in_sayac) + " = " + str(my_number))
        my_in_sayac = my_in_sayac + 1
    my_sayac = my_sayac + 1
# Dikkat edersek burada döngü içerisinde döngü kullandık...