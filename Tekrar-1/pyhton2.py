# Hesap makinesi yapalım

"""
Sizden basit bir hesap makinesi yapmanız isteniyor.

Hesap makinesi sonuç olarak ilk başta 0 gösterecek.

Kullanıcıdan yapılacak işlem ve bir sayı alınacak. Yapılacak işlem:

+ ise, girilen sayı sonuca eklenecek
- ise, girilen sayı sonuçtan çıkarılacak
* ise, girilen sayı sonuç ile çarpılarak, çarpım sonuca aktarılacak
/ ise, sonuç girilen sayıya bölünerek, bölüm sonuca aktarılacak
Her bir işlem yapıldıktan sonra sonuç ekrana yazdırılacak.

Kullanıcıdan işlem ve sayı alma adımları kullanıcı işlem olarak x girene kadar devam edecek.
Kullanıcı işlem olarak x girerse program sonlanacak.


Örneğin;

Kullanıcı sırayla +, 50, -, 10, *, 3, / ve 2 girdiği durumda, ekrana sırayla 50, 40, 120 ve 60.0 yazması gerekmektedir.

Çünkü sonuç;

ilk başta 0'dır
ardından 0 + 50 = 50 olur
ardından 50 - 10 = 40 olur
ardından 40 * 3 = 120 olur
en son olarak da 120 / 2 = 60 olur

"""
sonuc = 0
islem = input('İşlemi gir [+, -, *, /, x]? ')
sayi = int(input("Bir sayı giriniz"))

while islem != "x":
    if islem == "+":
        sonuc = sonuc + sayi

    if islem == "-":
        sonuc = sonuc - sayi
    if islem == "*":
        sonuc = sonuc * sayi
    if islem == "/":
        sonuc = sonuc / sayi
    print(sonuc)

    islem = input('İşlemi gir [+, -, *, /, x]? ')
    sayi = int(input("Bir sayı giriniz"))

    # buraya yazdığımızda her bir if in altına ayrı ayrı yazmaktansa bir kerede her if sonucunu
    # print etmiş oluyoruz
