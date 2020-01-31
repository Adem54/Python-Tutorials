# 1 ile n arasındaki tek sayıları listeleyen fonksiyonu yazınız
def tek_sayilari_listele(n):
    liste = []
    sayac = 1
    while sayac < n:
        if sayac % 2 != 0:
            liste.append(sayac)
        sayac += 1
    return liste


print(tek_sayilari_listele(29))
