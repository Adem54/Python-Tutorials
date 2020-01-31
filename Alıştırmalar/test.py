sayi = input("Bir sayı girin")

liste = []
eleman_ayni = False
for eleman in sayi:
    eleman_ayni = False
    liste.append(eleman)
    for eleman1 in liste:

        if eleman == eleman1:
            eleman_ayni = True

if eleman_ayni:
    print("Tüm elemanları eşit tir")
else:
    print("Tüm elemanlar aynı değil")
