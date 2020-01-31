"""
Kullanicidan girdi olarak bir kelime alan, kelimedeki "a"  ve "e" harflerinin toplam sayisini
 ekrana yazdiran python programini yaziniz.
"""
kelime = input("Bir kelime yazınız")
toplam = 0
for harf in kelime:
    if harf == "a" or harf == "e":
        toplam = toplam + 1


print(toplam)
