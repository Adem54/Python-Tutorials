"""
Mehmet'in elinde üzerlerinde sayı bulunan kartların olduğu listeler vardır.
 Mehmet arkadaşlarıyla bu listeleri kullanarak bir oyun oynayacaktır.
  Her oyuncu, elinde bulunan kart destesinde ki her bir sayı için,

Eğer sayı tüm kartların ortalamasından büyükse veya ortalamaya eşitse +5 puan; küçükse -3 puan alacaktır.
Kazanan oyuncuyu ve puanını liste şeklinde veren kim_kazandi fonksiyonunu yazınız.
"""


def kim_kazandi(oyuncular, kart_desteleri):
    toplam = 0
    counter = 1
    ortala = 0

    for sayilar1 in kart_desteleri:
        for sayi in sayilar1:
            toplam += sayi
            ortala = round((toplam / counter), 2)
            counter += 1


    liste = ["", 0]
    for sayi1 in range(len(oyuncular)):
        puan = 0
        for sayi2 in range(len(kart_desteleri)):
            if sayi1 == sayi2:
                for sayi in kart_desteleri[sayi2]:

                    if sayi >= ortala:
                        puan += 5
                    elif sayi < ortala:
                        puan -= 3
        if liste[1] < puan:
            liste[1] = puan
            liste[0] = (oyuncular[sayi1])
    return liste
    # kodu buraya yazın


print(kim_kazandi(['Ayşe', 'Mehmet', 'Fatma'], [
    [40, 50, 60], [20, 30, 40], [70, 80, 90]]))
