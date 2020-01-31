# Bir sayısının asal sayı olup olmadığını bulalım
sayi = int(input("Asal sayı olup olmadığını anlamak istedğini bir sayıyı gir? "))
counter = 2

while counter < sayi:
    print("counter: " + str(counter))
    print("sayı/counter: " + str(sayi % counter))
    if sayi % counter == 0:

        print(str(sayi) + " sayısı " + str(counter) + " sayısına bölünebildiği için asal sayı değildir")
        counter = sayi  # asal sayı olmadığını anladığımız anda döngüyü bitirmek için yaparız bunu
    elif sayi % counter != 0:
        if counter == sayi - 1:  # bunu yazarız çünkü burda en son kendinden önceki sayı ya da bölünemezse
            # işte o zaman diyebiliyoruz ki bu asal sayıdır
            print(str(sayi) + " bir asal sayıdır")
    counter = counter + 1
# 1 den 1000 e kadar olan sayıların asal olanlarını bulma
i = 2
while i < 1000:
    j = 2
    while j <= (i / j):
        if not (i % j):
            break
        j = j + 1
    if j > i / j:
        print(i)
    i = i + 1
