# bir sayıın kaç haneli olduğunu bulalım


sayi = "12345789434632462346"

sayi_basamak_sayisi = len(sayi)

print("sayi_basamak_sayisi: " + str(sayi_basamak_sayisi))

while sayi_basamak_sayisi > 1:
    toplam = 0
    for index in range(len(str(sayi))):

        eleman = sayi[index]

        toplam += int(eleman)

        son_index = len(str(sayi)) - 1
        if index == son_index:
            sayi = toplam
            print("sayi_Yeni_Değer : " + str(sayi))
            sayi = str(sayi)
            sayi_basamak_sayisi = len(sayi)

            print("sayi_Basamak_sauisi: " + str(sayi_basamak_sayisi))
