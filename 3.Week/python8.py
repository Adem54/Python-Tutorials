# Bir sayının asal sayı ise o sayıyı ekrana yazdırma
i = int(input("Bir sayı giriniz ve asal sayı ise yazdırılacak "))
j = 2
while j <= (i / j):  #
    if not (i % j):  # girdiğmiz sayının 2 ile böl den kalan 0 ise yani tam bölünüyorsa başına not koyunca true olacak
        # ve asal sayı olmadığı kesin olacak ve bitirecek direk if koşulunu ve bir alta geçip 2 ile başlayan j yi bir
        # artıracak ve bir altında da
        break
    j = j + 1
if j > i / j:
    print("i: " + str(i))
    print("j: " + str(j))
print("Eğer asal sayı değilse bu değer 1 kez karşınıza gelir yok asal sayı ise 2 kez göreceksiniz  " + str(i))
