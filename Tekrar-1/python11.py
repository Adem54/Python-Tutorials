"""
1000 e kadar olan sayıların asal olup olmadığını bulan programı yazdık...
"""

sayi = 2
is_asal = False
while sayi < 1000:

    if sayi == 2:
        print(str(sayi) + " sayısı asaldir")
    sayac = 2
    while sayac < sayi:

        if sayi % sayac == 0:

            break
        else:

            sayac += 1
            if sayac == sayi:
                print(str(sayi) + " sayısı asaldir")
    sayi += 1

print("----------------------------------------------------------------")
sayi = 2
is_asal = False
while sayi < 1000:
    if sayi == 2:
        is_asal = True
    sayac = 2
    while sayac < sayi:
        if sayi % sayac == 0:
            is_asal = False
            break
        else:
            is_asal = True
            sayac += 1
    if is_asal:
        print(sayi)
    sayi += 1
