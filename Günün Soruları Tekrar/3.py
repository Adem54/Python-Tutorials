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
kelime = input("Bir kelime giriniz")
girilen_kelime = kelime.lower()

sesli_harfler = "aeiou"

counter = 0
indis = -1
sesli_harf_indisler = []
for harf in girilen_kelime:
    indis += 1
    sesli_harf_indis = []
    if harf in sesli_harfler:
        counter += 1
        print(harf + " sesli harfi kelimenin " + str(indis) + ". sıradadır")
        sesli_harf_indis.append(harf)
        sesli_harf_indis.append(indis)
        sesli_harf_indisler.append(sesli_harf_indis)
print(counter)

print(sesli_harf_indisler)
