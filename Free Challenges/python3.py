# 4)Girilen sayının asal sayı mı değil mi olduğunu bulan python programını yazınız
# Asal sayılar sadece kendisine ve 1'e bölünebilen 1'den büyük doğal sayılar olarak tanımlanır.
# Örneğin ilk 10 asal sayı 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 biçiminde sıralanır
# Kendisinden ve 1 den başka bölüneni olup olmadığını kontrol ederiz döngü ile tek tek böleriz ve kalana bakarız
get_count = int(input("Bir sayı girin? "))
sayac = 1
while sayac < get_count:
    sayac = sayac + 1
    if sayac < get_count and get_count % sayac == 0:
        print("Bu sayı " + str(sayac) + " sayısına tam bölündüğü için asal sayı değildir")
        sayac = get_count
    elif sayac == get_count:
        print(str(get_count) + " sayısı kendisinden ve 1 den başka sayıya bölünemediği için asal sayıdır")
