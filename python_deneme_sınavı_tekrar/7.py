"""
Kullanicidan girdi olarak bir pozitif tam sayi alan , ve ekrana 0 dan kullanicinin girdigi
sayiya kadar(kullanicinin girdi sayi dahil degil)
olan cift sayilarin toplamini ekrana yazdiran python programini yaziniz
"""
sayi = int(input("Bir sayi gir"))
sayac = 0
toplam = 0
while sayac < sayi:
    if sayac % 2 == 0:
        toplam += sayac
    sayac += 1

print(toplam)
