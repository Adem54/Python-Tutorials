"""
liste içerisindeki tüm elemanlara 2 katını almak istersek nasıl yaparız ama yeni bir liste oluşturmadan getir
"""
liste = [4, 7, 9, 12, 16, 19]
for eleman in range(len(liste)):
    liste[eleman] = liste[eleman] * 2

print(liste)

sayac = 0
while sayac < len(liste):
    liste[sayac] = liste[sayac] * 2
    sayac += 1

print(liste)