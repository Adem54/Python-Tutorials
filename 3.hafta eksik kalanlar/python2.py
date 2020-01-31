# 1'den 100'e kadar olan sayılardan tek sayıları yazdıran kodu, while ve if yapısını kullanarak mod operatörü
# yardımıyla kullanarak kodlayınız

counter = 1
sayi = 100

while counter < 100:
    if counter % 2 != 0:
        print("Tek sayı: " + str(counter))
    counter = counter + 1

print("--------------------------------------------------------------")

sayi1 = int(input("Bir sayı girin"))

count = 1
toplam = 1

while count <= sayi1:
    toplam = toplam * count
    count = count + 1

print(toplam)
