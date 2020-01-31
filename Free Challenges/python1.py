# 1) 1 ile 100 arası 3′ e ve 5′ e tam bölünen  sayıları bulan python programını yazınız
# 2) 1 den kullanıcının girdiği sayıya kadar sayıları listeleyen python programını yazınız
# 3) Kullanıcının girdiği iki sayı arasındaki sayıların toplamını gösteren python programını yazınız
# (Örneğin 3 ve 6 girdiğinizde 4 ve 5 i toplayacak )
# 4)Girilen sayının asal sayı mı değil mi olduğunu bulan python programını yazınız
# 5)Python ile sayı tahmin programı yapınız.5 hakkınız olsun.5 kere de bilirseniz tebrikler yazdırınız kodstardaki gibi
# import random sayiuret=random.randint(1,20) bu kod 1-20 arasında rastgele sayı üretiyor,
# ve sayıuret değişkenine atıyor

sayi = 0

while sayi < 100:

    sayi = sayi + 3
    if sayi >= 100:  # burayı yapma sebebimiz sayı normalde 100 den küçük olarak döngü içerisine girer
        # ama döngü içerisine girdikten sonra
        print(sayi - 3)
    else:
        print(sayi)
    print("Bu satır yazıldı...")

myNumber = 0

while myNumber < 100:

    myNumber = myNumber + 15
    if myNumber >= 100:
        print()
    else:
        print("myNumber: " + str(myNumber))

#  2) 1 den kullanıcının girdiği sayıya kadar sayıları listeleyen python programını yazınız
