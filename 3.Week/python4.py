# Girilen bir sayının faktöriyel değerini bulunuz?
sayi = int(input("Bir sayı giriniz?"))
toplam = 1
counter = 0
while counter < sayi:
    counter = counter + 1
    toplam = toplam * counter
    print("faktToplam: " + str(toplam))

print("faktEnSonToplam: " + str(toplam))
# 1'den 100'e kadar olan sayılardan tek sayıları yazdıran kodu, while ve if yapısını kullanarak mod operatörü
# yardımıyla kullanarak kodlayınız
count = 0

while count < 100:
    count = count + 1
    if count % 2 == 1:
        print(count)
