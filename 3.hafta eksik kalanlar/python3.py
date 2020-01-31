# 1 ile 1000 arasındaki tüm asal sayıları ekrana yazdırın.
sayi = int(input("Bir sayı girin?"))
i = 2

while i < sayi:# girilen sayı i den büyükse koşul çalışır
    j = 2
    while j < i / j: # burda eğer
        if not (i % j):
            break
        j = j + 1
    if j > i / j:# zaten eğer j  i/j den büyükse i yi zaten bölmez ondan dolayı sen i yi yaz direk i asal olur ki
        # asıl olay bir yukardaki if de kopuyor zaten
        print(i)
    i = i + 1

# mesela sayımız 30 biz 6 ile bölünüp bölünmedğine bakıyoruz 30/6 5 çıkacak 5 zaten
# 6 dan küçük olduğu için zaten konrol etmeye gerek yok
