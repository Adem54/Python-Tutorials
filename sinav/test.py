liste = [1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 6, 7, 5]

# liste içerisinde tekrar eden her elemandan kaç tane olduğunu bulan liste
# benzersiz liste oluştur önce
uniq_list = []
for eleman in liste:
    if eleman not in uniq_list:
        uniq_list.append(eleman)

print(uniq_list)
n = 2
liste_tekrar_toplam = []
for sayi in range(len(uniq_list)):
    eleman1 = uniq_list[sayi]
    count = 0

    liste_tekrar = []
    for eleman2 in liste:

        if eleman1 == eleman2:
            count += 1
    liste_tekrar.append(eleman1)
    liste_tekrar.append(count)
    liste_tekrar_toplam.append(liste_tekrar)

print(liste_tekrar_toplam)

print(9 // 10)
