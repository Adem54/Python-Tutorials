"""
Daha önce 1000'e kadar olan tüm asal sayıları bulan bir kod yazmıştık.
Şimdi onu fonksiyonları kullanarak tekrar yazacağız:
Bir sayının asal sayı olup olmadığını bulan bir asal_mi adlı bir fonksiyion yazın.
Verilen bir sayıya kadar olan tüm asal sayıları liste olarak dönen asal_sayilari_bul adlı bir fonksiyon yazın.
"""


def asal_mi(sayi):
    is_Asal = False
    count = 2
    if sayi == 2:
        is_Asal = True
    while count < sayi:
        if sayi % count == 0:
            is_Asal = False
            break
        else:
            is_Asal = True
            count += 1
    if is_Asal:
        return sayi





sayi_asal = asal_mi(44)
print(sayi_asal)


def asal_sayilari_bul(sayim):
    sayac = 2
    asal_sayi_listesi = []
    while sayac < sayim:
        asal_sayi = asal_mi(sayac)
        if type(asal_sayi) == int:
            asal_sayi_listesi.append(asal_sayi)

        sayac += 1
    return asal_sayi_listesi

print(asal_sayilari_bul(1000))

