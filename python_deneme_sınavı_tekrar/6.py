"""
 Kullanicidan girdi olarak bir pozitif tam sayi alan , ve ekrana 1'den kullanicinin
  girdigi sayiya kadar(sayi dahil) olan sayilarin karelerini yazdiran python programini yaziniz
Ornek Program Outputu
Lutfen Bir Sayi Giriniz: 3

1
4
9
"""
sayi = int(input("Bir sayi giriniz"))
sayac = 1
while sayac <= sayi:
    print(sayac ** 2)
    sayac += 1

