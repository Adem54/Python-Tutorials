# 20 ile 50 arasındaki çift sayıların toplamını bulan kodu yazın.
toplam = 0
for sayi in range(20, 50):
    if sayi % 2 == 0:
        toplam = toplam + sayi
print(toplam)
