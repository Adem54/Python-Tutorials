"""
Öyle bir fonksiyon yazın ki, bir sayıdaki rakamları toplasın. Bu toplama işlemine sonuç tek hane olana kadar devam etsin
. Buna digial_root diyelim.

Verilen bir sayının digial_root unu bulup ekrana yazdırın

Hint: Bu problemi çözmenin en kolay yöntemi, sayıyı string haliyle kullanmak ve sonrada toplarken sayıya çevirmek

Ornek:

digital_root(16)
=> 1 + 6
=> 7


digital_root(132189)
=> 1 + 3 + 2 + 1 + 8 + 9
=> 24 ...
=> 2 + 4
=> 6

digital_root(493193)
=> 4 + 9 + 3 + 1 + 9 + 3
=> 29 ...
=> 2 + 9
=> 11 ...
=> 1 + 1
=> 2
"""


def digital_root(sayi):
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
    return sayi


sayi = input('Sayi girin:')
print(digital_root(sayi))
