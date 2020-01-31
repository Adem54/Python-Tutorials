"""
Kullanıcın verdiği sayılar arasından en küçüğünü bulan bir program yazmak istiyoruz. Bu program, kullanıcıdan
rakam girmesini isteyecek ve bu işlem kullanıcı sıfır girene kadar devam edecek. Kullanıcı sıfır girdiğinde,
o ana kadar girilmiş olan sayılardan en küçük olanı gösterecek.
"""
sayi = int(input("Bir sayı giriniz"))
en_kucuk_sayi = sayi
while sayi != 0:

    sayi = int(input("Bir sayı giriniz"))
    if en_kucuk_sayi > sayi:
        en_kucuk_sayi = sayi
    print(en_kucuk_sayi)
