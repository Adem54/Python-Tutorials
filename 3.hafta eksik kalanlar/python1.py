# 5 hariç 10 dan 0 a kadar olan sayıların yazdırımı
sayi = 10
while sayi >= 0:
    if sayi != 5:
        print(sayi)
    sayi = sayi - 1
print("--------------------------------------------------------------------")
# 1 den 100 e kadar olan sayıların toplamı
counter = 0
toplam = 0
while counter < 100:
    counter = counter + 1
    toplam = toplam + counter

print("toplam" + str(toplam))


