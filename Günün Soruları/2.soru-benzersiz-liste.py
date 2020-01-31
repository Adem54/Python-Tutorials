"""
Aşağıdaki her iki çözüm de  benzersiz bir liste oluşturmamızı sağlar..
"""

liste = [2, 5, 7, 2, 5, 9, 12, 4, 6]
yeni_liste = []
for eleman in liste:
    if eleman not in yeni_liste:
        yeni_liste.append(eleman)

print(yeni_liste)

liste2 = [4, 6, 12, 11, 4, 6, 7, 9, 11]

new_list = []
for eleman in liste2:
    if eleman in new_list:
        continue
    else:
        new_list.append(eleman)

print(new_list)
