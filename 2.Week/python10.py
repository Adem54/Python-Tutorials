# Hesap makinesi yapmayıı deneyelim

sonuc = 0
islem = input('İşlemi gir [+, -, *, /, x]? ')
sayi = 0

while islem != "x":
    sayi = int(input("Bir sayı giriniz"))

    if islem == "+":
        sonuc = sonuc + sayi

    if islem == "-":
        sonuc = sonuc - sayi

    if islem == "*":
        sonuc = sonuc * sayi

    if islem == "/":
        sonuc = sonuc / sayi
    print(sonuc)
    # Döngülerde çok dikkat etmemiz gereken bir kısım burası buna dikkat edelim bu birçok döngüde var
    # mesela bu switch case de de var
    # Burası çok önemli her seferinde print(sonuc) yazdırmamıza gerek yok bu birçok döngüde karşımıza gelecek buna
    # dikkat edelim

    islem = input('İşlemi gir [+, -, *, /, x]? ')

print("İşlem olarak  'x' girdiğiniz için döngüden çıktınız")
