# Yazacağımız program, kullanıcıdan rakam girmesini isteyecek ve bu işlem kullanıcı sıfır girene kadar devam edecek.
# Kullanıcı sıfır girdiğinde, o ana kadar girilmiş olan sayılardan en büyük olanı gösterecek.İlk sayıyı en büyük sayı
# olarak kabul edeceğiz


girilen_sayi = int(input("Bir sayi giriniz?"))
print("Girilen sayi: " + str(girilen_sayi))
en_buyuk_sayi = girilen_sayi
print("En büyük sayi: " + str(en_buyuk_sayi))
while girilen_sayi != 0:
    if en_buyuk_sayi < girilen_sayi:
        en_buyuk_sayi = girilen_sayi
    girilen_sayi = int(input("Bir sayi giriniz?"))
    print("Girilen sayi: " + str(girilen_sayi))

if girilen_sayi == 0:
    print("Kullanıcı 0 girdi ve en büyük sayımız: " + str(en_buyuk_sayi))

# sayısal integer bir veri ile string bir veriyi karşılaştırırsak hata alabiliriz
x = "kodStar"
y = x == "kodStar"  # dikkat edelim tek eşittir işareti atama işlemidir iki eşittir ise karşılaştırma operatörüdür
print("y: 0" + str(y))

x = 3
y = 6
# print(x + y + 1 = 10) bu işlemde hata alırız çünkü 1 e 10 sayısını atamaya çalışmış değişkenler rakamla başlamaz
if x == True:
    print("3 ile True birbirine eşit çıktı")
else:
    print("3 ile True ifadesi birbiri ile karşılaştırılabiliyor ama eşit değildir")