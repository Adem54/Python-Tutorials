def gecenler(ogrenciler):
    list = []
    for eleman in range(len(ogrenciler)):
        element = ogrenciler[eleman]
        if (element[1] + element[2] + element[3]) / 3 > 2.5:
            list.append(element)

        else:
            continue
    return list


ogrenciler = [["baris", 3.5, 4, 2], ["ayse", 3, 4, 4], ["onur", 0, 2.85, 3]]
gecenler = gecenler(ogrenciler)
print(gecenler)
