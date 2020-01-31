# Daha önce 1000'e kadar olan tüm asal sayıları bulan bir kod yazmıştık. Şimdi onu fonksiyonları
# kullanarak tekrar yazacağız:
#
# Bir sayının asal sayı olup olmadığını bulan bir asal_mi adlı bir fonksiyion yazın.
# Verilen bir sayıya kadar olan tüm asal sayıları liste olarak dönen asal_sayilari_bul adlı bir fonksiyon yazın.

def asal_mi(n):
    isAsal = True
    for bolen in range(2, n):
        if n % bolen == 0:
            isAsal = False
            break
        else:
            isAsal = True
    return isAsal


print(asal_mi(3))
print(asal_mi(24))


# Verilen bir sayıya kadar olan tüm asal sayıları liste olarak dönen asal_sayilari_bul adlı bir fonksiyon yazın.

def asal_sayilari_bul(n):
    asallar = []
    sayi = 2
    while sayi < n:
        if asal_mi(sayi):
            asallar.append(sayi)
        sayi = sayi + 1
    return asallar

# print(asal_sayilari_bul(100))
