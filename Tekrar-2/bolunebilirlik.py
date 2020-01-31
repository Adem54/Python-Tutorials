liste = [10, 12, 17, 81, 19, 21]


def bolunebilirlik(list, bolen):
    new_list = []
    for eleman in list:
        bolunuyor = False
        if eleman % bolen == 0:
            bolunuyor = True
        new_list.append(bolunuyor)
    return new_list


liste = [10, 12, 17, 81, 19, 21]
print(bolunebilirlik(liste, 3))
