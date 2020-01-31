# SORU-1 =========================================================

# Kullanicidan bir tam sayi alip asagidaki kurala gore kullanicidan alinan sayiya karsilik gelen sayi dizisini,
# while dongusu kullanarak olusturan python programini yaziniz.

# Sayi Dizinin kurali:

# 1- Dizinin ilk terimi kullanicidan alinan sayi olacak, bu sayiyi n degiskenine atadigimizi varsayarsak;
# 2- Sonraki terimler icin su 3 sart uygulanacak:
#    a- n 2'ye tam bolunuyorsa, sonraki terim n//2
#	 b- Eger n 2'ye tam bolunmuyorsa, sonraki terim 3*n + 1 olacak
#	 c- Sayi dizisi n=1 olunca sonlanacak


# Kullanicinin 3 ve 7 girdigi durumlardaki programin outputu su sekilde olmali


# Lutfen bir sayi giriniz: 3
# 3 10 5 16 8 4 2 1

# Lutfen bir sayi giriniz: 7
# 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1

n = int(input("Bir sayı giriniz: "))
list = []
list.append(n)
print(list)

while n != 1:
    if n % 2 == 0:
        n = n // 2
        list.append(n)

    else:
        n = 3 * n + 1
        list.append(n)

print(list)

