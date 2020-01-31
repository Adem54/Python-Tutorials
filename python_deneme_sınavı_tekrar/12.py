"""
Kullanicidan girdi olarak bir kelime alan, eger kelime 5'ten fazla harf  iceriyorsa ekrana "uzun",
daha az harf iceriyorsa ekrana "kisa"
yazdiran bir python programi yaziniz
"""

kelime = input("Bir kelime girin")
if len(kelime) > 5:
    print("uzun")
else:
    print("kısa")
