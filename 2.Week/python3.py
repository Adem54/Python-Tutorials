# Girilen Sayının Faktöriyelini Bulma
sayi = int(input("Bir sayı giriniz!"))
myNumber = 1
sayac = 1

while sayac <= sayi:
    myNumber = myNumber * sayac
    print(myNumber)
    sayac = sayac + 1

print(str(sayi) + " sayısının faktöriyeli " + str(myNumber) + " 'dır")

# 1 den 100 e kadar olan sayıları yazdırınız
myNum = 1
while myNum < 101:
    print(myNum)
    myNum = myNum + 1


