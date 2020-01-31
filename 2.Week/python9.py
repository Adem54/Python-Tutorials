# Yazacağımız program, kullanıcıdan rakam girmesini isteyecek ve bu işlem kullanıcı sıfır girene kadar devam edecek.
# Kullanıcı sıfır girdiğinde, o ana kadar girilmiş olan rakamların ortalamasını gösterecek.


toplam = 0
girilen_rakam_sayisi = 0
sayi = int(input('Bir sayı gir?'))

while sayi != 0:
    girilen_rakam_sayisi = girilen_rakam_sayisi + 1
    toplam = toplam + sayi
    sayi = int(input('Bir sayı gir?'))

print(toplam / girilen_rakam_sayisi)
