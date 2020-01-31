"""
Arkadaslar bu soruya 2 ya da 3 gun sure verelim. Biraz kapsamli bir adam asmaca sorusu.
Lutfen ekledigim kazanan ve kaybeden program outputunu detayli inceleyin asagidaki kurallardan daha aciklayici
 olabilir o outputlar
Kolay gelsin.
KURALLAR
1- Bilgisayar bir kelime secmeli. Bu secme islemini su sekilde yapbilirsiniz: adam_asmaca(kelime) diye bir
fonksiyonumuz oldugunu dusunelim,
programinizi adam_asmaca("kodstar") diye cagirildiginda gizli kelime "kodstar"
adam_asmaca("istanbul") diye cagirildinda gizli kelime "istanbul" olacak sekilde design edebilirsiniz,
yani gizli kelimeyi degistirmek icin kodunuzda her seferinde ufak bir degisiklige gidecek sekilde
 bir program yazabilirsiniz.
2- Oyunun basinda gizli kelimenin kac harfli oldugu oyuncuya bildirilmeli
3 - Her seferinde oyuncudan bir harf tahmin etmesi istenmeli
4- Oyuncuya her tahminden once tahmin edilmemis harfler listesi gosterilmeli
5- Her tahminden sonra oyuncuya , tahmin ettigi harfin gizli kelimede olup olmadigiyla ilgili geri bildirim yapilmali
6- Her tahminden sonra oyuncuya o ana kadar kelime'nin tahmin edilen ve tahmin edilmemis harfleri gosterilmeli
7- Oyuncunun sadece 8 tahmin hakki olmali
8- Oyuncunun tahmin hakki, sadece oyuncu yanlis tahmin yaptiginda azalmali

9- Oyuncu ayni harfi tekrar tahmin ederse, tahmin hakki azaltilmamali, oyuncuya "Bu harfi daha once tahmin etmistiniz"
tarzinda bir uyari verilmeli

10- Oyun, oyuncu kelimeyi bildiginde veya tum tahmin haklari tukendiginde sonlanmali.


outputlarda gizli kelime su formatta
Iyi tahmin:ko_ _ _ _ r
siz bir liste seklinde gosterebilirsiniz, kalan harflerin gosterildigi gibi bir liste.
Bir harften birden fazla olabilir
salih Abi bence sadece ingilizce karakterler (x ve w olmayabilir ) ve sadece kucuk harfler
tamam abi, arkadaslarin aklinda soru isareti kalmasin diye sordum.
yalniz xmas ve ingilizce karakter falan. dis guclerin bir oyunu olmasin
"""

"""
1)Program her başladığında yeni bir gizli kelime oluşturan bir fonksiyonla başlaycak
2)Gizli kelimenin kaç harfli olduğunu oyun başında belirtilmeli
3) Her seferinde oyuncudan bir harf tahmin etmesi istenmeli
4- Oyuncuya her tahminden once tahmin edilmemis harfler listesi gosterilmeli
5- Her tahminden sonra oyuncuya , tahmin ettigi harfin gizli kelimede olup olmadigiyla ilgili geri bildirim yapilmali
6- Her tahminden sonra oyuncuya o ana kadar kelime'nin tahmin edilen ve tahmin edilmemis harfleri gosterilmeli
7- Oyuncunun sadece 8 tahmin hakki olmali
8- Oyuncunun tahmin hakki, sadece oyuncu yanlis tahmin yaptiginda azalmali
9- Oyuncu ayni harfi tekrar tahmin ederse, tahmin hakki azaltilmamali, oyuncuya "Bu harfi daha once tahmin etmistiniz"
tarzinda bir uyari verilmeli
10- Oyun, oyuncu kelimeyi bildiginde veya tum tahmin haklari tukendiginde sonlanmali.
11)Harfler küçük harf olmalı
"""

kelime = input("Bir kelime giriniz")
new_kelime = kelime.lower()
print(kelime)
print(new_kelime)


# Kelime üretme işini iki şekilde de yapabiliriz
# 1A-Kelime üretme
def yeni_kelime_uret(word):
    return word


print(yeni_kelime_uret("armut"))

# 1B-Kelime üretme
from random import randint


def kelime_uret():
    kelime_liste = ["kodstar", "programci", "kaptan", "merhaba", "python", "kemal", "mustafa", "sakarya", "yilbasi",
                    "karanlik"]
    rand = randint(1, 10)
    return kelime_liste[rand]


# 2)Kelimenin uzunluğunu belirtelim (biz 2.kelime üretme yöntemini seçtik)
# kelime = kelime_uret()
# print(kelime)

# print("Gizli kelimemizin karakter uzunluğu " + str(len(kelime)) + " harften oluşuyor")

# 3)Her seferinde oyuncudan bir harf tahmin etmesini isteyelim.Ama her tahmin öncesinde tahmin edilmemiş
# harf listesi gösterelim dolayısı ile ilk tahmin öncesinde tüm alfabeyi gösterip yazdıralım


alfabe = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
          "y", "z"]
print("Kalan Harfler: " + str(alfabe))

# Bu harfi küçük harfe çevir ne olur ne olmaz oyuncu büyük harf girse bile küçük harfe biz çevirelim
# Bu arada tahmin edilen harf sadece ingilizce karakter  (x ve w olmayabilir ) ve sadece kucuk harfler


# 5- Her tahminden sonra oyuncuya , tahmin ettigi harfin gizli kelimede olup olmadigiyla ilgili geri bildirim yapilmali
# Iyi tahmin:k_ _ _ _ _ _     Oops! Yanlis tahmin:_ _ _ _ _ _ _
kelime = "elmasci"

tahmin_durumu = ["e", "l", "m", "a", "s", "c",
                 "i"]  # gizli kelime uzunluğnu bildiğimiz için o kadar boşluk bıraktıkuzunluk = len(tahmin_durumu)
copy_tahmin_durumu = tahmin_durumu[:]
print("copy_tahmin_durumu: " + str(tahmin_durumu))
deneme_sayisi = 0
tahmin_edilen_harfler = []
copy_alfabe = alfabe[:]
while deneme_sayisi < 8:
    harf = input("Lutfen bir harf tahmin edin: ")
    tahmin_edilen_harf = harf.lower()
    if tahmin_edilen_harf not in copy_alfabe:
        harf = input("Lutfen alfabe içinde olan bir harf tahmin edin: ")
        tahmin_edilen_harf = harf.lower()

    kelime = "elmasci"
    indis = 0
    tahmin = False
    print("tahmin_edilen_harfler " + str(tahmin_edilen_harfler))
    print("tahmin_edilen_harf " + tahmin_edilen_harf)
    print(tahmin_edilen_harf not in tahmin_edilen_harfler)
    print("tahmin edilen harfler uzunluğu : " + str(len(tahmin_edilen_harfler)))
    if len(tahmin_edilen_harfler) > 0 and tahmin_edilen_harf in tahmin_edilen_harfler:
        deneme_sayisi = deneme_sayisi
        print("Aynı harfi daha önce tahmin ettiğiniz için deneme sayısı: " + str(deneme_sayisi))
    else:
        for sayi in range(len(tahmin_durumu)):
            char = tahmin_durumu[sayi]
            print("tahmin_edilen_harf " + tahmin_edilen_harf)
            print("CHAR: " + char)
            if tahmin_edilen_harf == char:
                copy_tahmin_durumu.remove(char)
                print("Tahmin durumu" + str(copy_tahmin_durumu))
                print("INDIS: " + str(sayi))
                tahmin = True
            else:
                tahmin = tahmin
            print("INDIS: " + str(sayi))
            print("Tahmin Durumu Uzunluğu: " + str(len(tahmin_durumu)))
            if tahmin and sayi == (len(tahmin_durumu) - 1):
                print("Iyi tahmin: " + str(copy_tahmin_durumu))
            elif sayi == (len(tahmin_durumu) - 1):
                print("Oops! Yanlis tahmin: " + str(copy_tahmin_durumu))

            if sayi == (len(tahmin_durumu) - 1):
                tahmin_edilen_harfler = tahmin_edilen_harfler + [tahmin_edilen_harf]
                print("Tahmin ettiğniz harfler: " + str(tahmin_edilen_harfler))
                alfabe.remove(tahmin_edilen_harf)
                print("Kalan Harfler: " + str(alfabe))

            print("indis: " + str(sayi))
        if tahmin:

            deneme_sayisi = deneme_sayisi
            print("Doğru tahminn ettiğiniz için deneme sayısı: " + str(deneme_sayisi))
        else:
            deneme_sayisi += 1
            print("Yanlış tahminn ettiğini için deneme sayısı: " + str(deneme_sayisi))
        if deneme_sayisi <= 8 and len(copy_tahmin_durumu) == 0:
            print("Tebrikler tüm harfleri " + str(deneme_sayisi) + " hakta bildiniz ve oyunu kazandınız")
        elif deneme_sayisi == 8 and len(copy_tahmin_durumu) != 0:
            print("Malesef " + str(deneme_sayisi) + " hakkınız doldu tüm harfleri bilemediniz")

"""
    if tahmin_edilen_harf not in tahmin_edilen_harfler:
    else:
        print(tahmin_edilen_harf + "  Bu harfi daha once tahmin etmistiniz")
        deneme_sayisi = deneme_sayisi
        print("Bu sayıyı daha önce tahmin ettiğiniz için deneme sayısı: " + str(deneme_sayisi))    
"""

# Kesinlikle for ile döndürdüğün listenin içinde o listeden eleman silmemeye çalış bu çok önemli for döngüsü tamamen
# bitene kadar liste uznluğunun or orjinaline dokunmamalı ancak o for döngüsü biter döngü 2.for döngüsünde
# yeni birharf girmeyi isterse orda artık  for içinde dönecek olan listemizin son hali güncellenebilir
