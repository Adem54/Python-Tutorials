# a ve b değerleri kullanıcı tarafından girilecektir. a ve b tam sayı olmak üzere; a ve b arasındaki (a ve b dahil)
# sayılardan karekökü çift olan sayıları yazdırın.

a = int(input("a sayisini girin: "))
b = int(input("b sayisini girin: "))
# karekök bulma  matematikte normalde karekök demek 4 üzeri 1/2 demektir ondan dolayı
# 4**0.5 dersek 4 ün karekökünü al demiş oluruz
while a <= b:
    if (a ** 0.5) % 2 == 0:
        print(a)
    a = a + 1
