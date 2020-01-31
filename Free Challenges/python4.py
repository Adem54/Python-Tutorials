# 5)Python ile sayı tahmin programı yapınız.5 hakkınız olsun.5 kere de bilirseniz tebrikler yazdırınız kodstardaki gibi
# import random sayiuret=random.randint(1,20) bu kod 1-20 arasında rastgele sayı üretiyor,
# ve sayıuret değişkenine atıyor

import random

# Biz counter ı 1 den başlattık çünkü dışarda zaten bir kez tahmin ettik ve sayı da üretildi ondan dolayı
# artık döngü içerisinde 4 kez daha dönmesi yeterli olacak çünkü içerde de 5 kez dönerse
# o zaman 6 olur bir fazla olur o zmaanda
sayiuret = random.randint(1, 5)  # bu şekilde bize içerisine yazdğımız iki sayı arasında random bir sayı üretir

appraisal_value = int(input("Üretilen sayıyı tahmin et "))
counter = 1
if counter == 1:
    print(str(counter) + ".sayı tahmin edildi")
    print(str(counter) + ". üretilen sayı " + str(sayiuret))

while counter < 5:

    if sayiuret == appraisal_value:
        print("Tebrikler " + str(counter) + ".deneme de üretilen sayıyı buldunuz ")

        counter = 6
    else:
        sayiuret = random.randint(1, 5)

        appraisal_value = int(input("Üretilen sayıyı doğru tahmin edemediniz lütfen yeniden tahmin ediniz"))

        counter = counter + 1
        print(str(counter) + ". üretilen sayı " + str(sayiuret))
        print(str(counter) + ".sayı tahmin edildi")
        if counter == 5:
            print("Malesef " + str(counter) + " kez deneme hakkınız sona ermiştir.Üretilen sayıyı " + str(
                counter) + " deneme de bilemediniz")
