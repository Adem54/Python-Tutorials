"""
SORU-4 SAYI TAHMIN OYUNU
========================================
Bu soruda kullanicinin aklindan tutugu 1 ile 100 arasindaki sayi , kullanicidan alacagi komutlarla bulacak bir python
 programi yazmaniz isteniyor.

Program soyle calismali :
1- Kullanici aklindan 1 ile 100 arasinda bir sayi tutacak
2- Bilgisayar bir tahminde bulunacak, sonra bilgisayar kullanicidan su sekilde bir  input isteyecek
	"Tahmin dogruysa 'd' ye , tutulan sayidan yuksekse 'y' ye, tutulan sayidan alcaksa 'a' ya basiniz"
3- Bilgisayar bir ust soruda aldigi cevaba gore yeni bir tahmin uretecek ve bu dongu bilgisayar sayiyi dogru tahmin
edene kadar yani kullanici
    "Tahmin dogruysa 'd' ye , tutulan sayidan yuksekse 'y' ye, tutulan sayidan alcaksa 'a' ya basiniz" bu input
    komutuna 'd' girene, yani tahmin dogru diyene kadar  devam edecek.

4- Programi yazarken kullinicinin her zaman 'd' 'y' ve 'a' dan birini ve dogru sekilde girdigini varsayabilirsiniz.


ALGORITMA TAVSIYESI

Bu program icin soyle bir algoritma kullanabilirsiniz.

Diyelim ki kullanici aklinda 56 sayisini tuttu.

1. Tahmin: Bilgisayarin ilk tahmini her zaman 50 olmali 0 ve 100 un yarisi, tahmin 50 oldugunda, kullanici
input olarak 'a' girecek cunku 50 tutulan sayidan(56) alcak.
2. Tahmin: 50 tutulan sayidan alcak olduguna gore, tutulan sayi 50 ile 100 arasinda olmali, bu durumda
 bilgisayarin 2. tahmini 75 olacak yani 50 ile 100'un yarisi
3. Tahmin: 75 tahmini icin kullanici input olarak 'y' girecek cunku 75 tutulan sayi(56)dan yuksek,
 bu durumda bilgisayarin 3. tahmini 62 olacak yani 50 ile 75 in yarisi(int division)
4. Tahmin: 62 tahmini icin kullanici  input olarak 'y' girecek cunku 62 tutulan sayi(56)dan yuksek,
 bu durumda bilgisayarin 3. tahmini 56 olacak yani 50 ile 62'nin yarisi

Bilgisayar 4. tahminde aklimizda tutugumuz sayiyi bulmus oldu . 56 tahmini icin kullanici input olarak
 'd' girecek ve program sonlanacak

Kullanicinin aklindan 56 tutugu durumdaki ornek  program outputu
-----------------------------------------------------------------------------
Lutfen aklinizdan 1 ile 100 arasinda bir sayi tutunuz
Tutugunuz sayi  50 mi/mu?
Tahmin dogruysa 'd' ye , tutulan sayidan yuksekse 'y' ye, tutulan sayidan alcaksa 'a' ya  basiniz : a
Tutugunuz sayi  75 mi/mu?
Tahmin dogruysa 'd' ye , tutulan sayidan yuksekse 'y' ye, tutulan sayidan alcaksa 'a' ya  basiniz : y
Tutugunuz sayi  62 mi/mu?
Tahmin dogruysa 'd' ye , tutulan sayidan yuksekse 'y' ye, tutulan sayidan alcaksa 'a' ya  basiniz : y
Tutugunuz sayi  56 mi/mu?
Tahmin dogruysa 'd' ye , tutulan sayidan yuksekse 'y' ye, tutulan sayidan alcaksa 'a' ya  basiniz : d
Bildim!!! Tutugunuz sayi :  56

------------------------------------------------------------------------------

SORU-4 SAYI TAHMIN OYUNU
========================================
Bu soruda kullanicinin aklindan tutugu 1 ile 100 arasindaki sayi , kullanicidan alacagi komutlarla bulacak bir python
 programi yazmaniz isteniyor.

Program soyle calismali :
1- Kullanici aklindan 1 ile 100 arasinda bir sayi tutacak
2- Bilgisayar bir tahminde bulunacak, sonra bilgisayar kullanicidan su sekilde bir  input isteyecek
	"Tahmin dogruysa 'd' ye , tutulan sayidan yuksekse 'y' ye, tutulan sayidan alcaksa 'a' ya basiniz"
3- Bilgisayar bir ust soruda aldigi cevaba gore yeni bir tahmin uretecek ve bu dongu bilgisayar sayiyi dogru tahmin
edene kadar yani kullanici
    "Tahmin dogruysa 'd' ye , tutulan sayidan yuksekse 'y' ye, tutulan sayidan alcaksa 'a' ya basiniz" bu input
    komutuna 'd' girene, yani tahmin dogru diyene kadar  devam edecek.

4- Programi yazarken kullinicinin her zaman 'd' 'y' ve 'a' dan birini ve dogru sekilde girdigini varsayabilirsiniz.


"""

import random

kullanici_tutugu_sayi = int(input("Aklınızda tuttuğunuz sayıyı giriniz"))
uretilen_sayi = random.randint(1, 20)
print(uretilen_sayi)
basilan_harf = ""
if uretilen_sayi > kullanici_tutugu_sayi:
    basilan_harf = input("Üretilen sayi tuttuğunuz sayıdan büyüktür.'y' ye basınız")
elif uretilen_sayi < kullanici_tutugu_sayi:
    basilan_harf = input("Üretilen sayi tuttuğunuz sayıdan küçüktür.'a' ya basınız")
elif uretilen_sayi == kullanici_tutugu_sayi:
    basilan_harf = input("Üretilen sayı tuttğunuz sayıya eşittir.'d' ye basınız")

while basilan_harf != "d":

    uretilen_sayi = random.randint(1, 20)
    print("üretilen sayı :" + str(uretilen_sayi))

    if uretilen_sayi > kullanici_tutugu_sayi:
        basilan_harf = input(" bilgisayarın ürettiği sayi siziin tuttuğnuz sayıdan büyük old için 'y' ye basın")

    elif uretilen_sayi < kullanici_tutugu_sayi:
        basilan_harf = input("Üretilen sayi tuttuğunuz sayıdan küçüktür.'a' ya basınız")


    elif uretilen_sayi == kullanici_tutugu_sayi:
        basilan_harf = input("Üretilen sayı tuttğunuz sayıya eşittir.'d' ye basınız")
