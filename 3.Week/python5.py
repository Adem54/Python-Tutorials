# Asal sayılar 1 ve kendisinden başka hiç bir sayıya bölünemeyen sayılardır.
# İç içe döngüler kullanarak sayıların asal olup olmadıklarını kontrol edebilirsiniz.
# 1 ile 1000 arasındaki tüm asal sayıları ekrana yazdırın.
i = 2
while i < 1000:
    j = 2
    while j <= (i / j):  # j küçük ya da eşit ise i nin j ye bölümüne ki i nin j ye bölümü en fazla 1 olur
        if not (i % j):  # i nin j ye bölümünden kalan 0 ise 0 False dur ve  notFalse da True olacağı için
            # bu if koşulunun sağlanması için i j ye tam bölünmesi gerekir ve eğer öyles ise bitir demiş
            break
        j = j + 1
    if j > i / j:
        print(i)
    i = i + 1

counter1 = 2

while counter1 < 999:
    if counter1 == 2:
        print(str(counter1) + " sayısı bir asal sayıdır")

    counter1 = counter1 + 1
    # ikinci while döngüsünün sayacı burda başlamalı zaten bu önemli...
    counter2 = 2
    print("counter1 " + str(counter1))
    print("counter2:  " + str(counter2))
    # counter1 in asal sayı olup olmadığını belirleyeceğiz
    # Eğer while döngüsüne giremezse o zaman tekrar en dıştaki while döngüsünü baştan başlatıyor
    while counter2 < counter1:

        if counter1 % counter2 == 0:
            print(str(counter1) + " sayısı bir asal sayı değildir")
            counter2 = counter1  # diyerek içerdeki döngüden çık...çünkü sayının anladık asal olmadığını
            print("counter2: " + str(counter2))

        elif counter1 % counter2 != 0:
            if counter2 == counter1 - 1:
                print(str(counter1) + " sayısı bir asal sayıdır")

        counter2 = counter2 + 1
        print("counter2: " + str(counter2))
    print("içerdeki while döngüsü bitti ve en son counter1 değeri : " + str(counter1))
