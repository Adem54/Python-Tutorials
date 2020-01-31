# 1 den 1000 e kadar olan sayıların asal olanlarını bulma
i = 2
sayi = int(input("Bir sayı giriniz"))
while i < sayi:
    j = 2
    print("j: " + str(j))
    print("i/j : " + str(i / j))
    print("Eğer " + str(j) + "  " + str(i / j) + " ' den küçükse while döngüsüne girer yoksa girmez")
    while j <= (i / j):
        print("------------------------------")
        print("i: " + str(i))
        print("j: " + str(j))
        if not (i % j):
            break
        j = j + 1
    if j > i / j:
        print("Eğer j: " + str(j) + "   " + str(i / j) + "  'den büyükse  i değeri bir allta yazdırılıyor")
        print(i)
    i = i + 1
    print("Burdan sonra en dıştaki while daki koşulu sorgular doğru mu diye! ---   i: " + str(i))
