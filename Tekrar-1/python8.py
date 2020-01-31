sayi = 1

while sayi < 100:
    if sayi % 2 != 0:
        print(sayi)
    sayi += 1

print("-------------------------------------------")
sayi = int(input("Faktöriyelini alınmasını istediğini sayıyı giriniz"))
toplam = 1
sayac = 1
while sayac <= sayi:
    toplam = toplam * sayac
    print(toplam)
    sayac += 1
print(toplam)
