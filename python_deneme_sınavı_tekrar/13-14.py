"""
Kullanicidan girdi olarak bir kelime alan, kelimedeki "a"  ve "e" harflerinin toplam sayisini
ekrana yazdiran python programini yaziniz.
"""

kelime = input("Bir kelime giriniz")
counter = 0
for char in kelime:
    if char == "a" or char == "e":
        counter += 1

print(counter)

"""
Parametre olarak bir liste alan ve bu listedeki elemanlarin birbirleriyle toplamini geri donen
toplam(listem) fonksiyonunu yaziniz.
"""


def toplam(listem):
    eleman_toplam = 0
    for eleman in listem:
        eleman_toplam += eleman
    return eleman_toplam


liste = [1, 4, 7, 9, 12, 3, 4]

print(toplam(liste))
