def tekrar_eden_elemanlari_bul(test_list):
    liste = []
    for eleman in test_list:
        if eleman not in liste:
            liste.append(eleman)
    new_list = []
    for eleman in liste:

        if eleman in test_list:
            count = 0  # aynı elemanlardan kaç tane olduğunu buulmak için
            sayac = -1  # aynı elemanların indislerinin kaç olduğunu bulmak için

            yeni_liste = []
            every_member = []
            new_indis = []

            for member in test_list:

                sayac += 1

                if member == eleman:
                    new_indis.append(sayac)

                    count += 1

            yeni_liste.append(eleman)
            yeni_liste.append(count)
            every_member.append(yeni_liste)
            every_member.append(new_indis)
            new_list.append(every_member)
    return new_list


my_list = [1, 5, 3, 6, 5, 3, 5, 6, 1, 3, 5]
liste = ["Ahmet", "Hasan", "Zeynep", "Adem", "Ahmet", "Hasan", "Adem", "Ahmet"]
print(tekrar_eden_elemanlari_bul(liste))
