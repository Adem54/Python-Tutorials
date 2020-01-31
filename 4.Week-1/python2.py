sayi1 = int(input("Bir sayı giriniz"))
if sayi1 < 0:
    mutlak_sayi1 = sayi1 * -1
else:
    mutlak_sayi1 = sayi1

sayi2 = int(input("Bir sayı giriniz"))
if sayi2 < 0:
    mutlak_sayi2 = sayi2 * -1
else:
    mutlak_sayi2 = sayi2

print(mutlak_sayi1 + mutlak_sayi2)
