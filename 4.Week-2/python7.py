# Bir listede verilen sayilarin verilen bir sayiya bolunebilirligini bulup liste halinde donen bir program
# yazmak istiyoruz. Bunun için  bolunebilir adında bir fonksiyon tanımlamak istiyoruz.
# Bu fonksiyonu tamamlayın.
# Kodu çalıştırın ve sonucun [False, True, False, True, False, True] olduğunu kontrol edin.

def bolunebilir(liste, bolen):
    list = []
    for eleman in liste:
        list.append(eleman % bolen == 0)

    return list


print(bolunebilir([10, 12, 17, 81, 19, 21], 3))
