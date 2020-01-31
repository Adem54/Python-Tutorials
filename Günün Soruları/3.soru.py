"""
Kullanicidan bir kelime alan, ve bu kelimedeki sesli harflerin toplam sayisini ve sesli harflerin kelimenin
kacinci harfleri oldugunu ekrana yazdiran python programini yaziniz.
Kullanicinin sadece kucuk harfleri kullanidigini varsayabilirsiniz.
Ornek Program Outputu:
====================================
lutfen bir kelime giriniz: merhaba
girdiginiz kelimede 3 tane sesli harf var
e kelimenin 2. harfidir
a kelimenin 5. harfidir
a kelimenin 7. harfidir
"""


kelime1 = input("Bir kelime giriniz")
kelime = kelime1.lower()
sesli = "aeıioöuü"
sayac = 1
count = 0
for eleman in kelime:
    if eleman in sesli:
        count += 1
        print(eleman + " kelimenin " + str(sayac) + ". harfidir")
    sayac += 1

print("girdiginiz kelimede " + str(count) + " tane sesli harf var")



