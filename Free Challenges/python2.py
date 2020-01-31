# 2) 1 den kullanıcının girdiği sayıya kadar sayıları listeleyen python programını yazınız

sayi = int(input("Bir sayı giriniz?"))
sayac = 1
while sayac <= sayi:
    print("sayac:  " + str(sayac))
    sayac = sayac + 1

# 3) Kullanıcının girdiği iki sayı arasındaki sayıların toplamını gösteren python programını yazınız
# (Örneğin 3 ve 6 girdiğinizde 4 ve 5 i toplayacak )

first_count = int(input("ilk sayıyı giriniz?"))
second_count = int(input("İkinci sayıyı giriniz?"))

if first_count <= second_count:
    counter = first_count + 1
else:
    counter = second_count + 1
toplam = 0
while counter < first_count or counter < second_count:
    toplam = toplam + counter
    print("Toplam: " + str(toplam))
    counter = counter + 1

print("En son toplam: " + str(toplam))
