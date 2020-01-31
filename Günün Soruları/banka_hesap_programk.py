"""
[7:48 AM] KemalGUNUN SORUSU-HESAP UZMANI
    General

Bu sorumuzda cok basit bir banka hesap programi yazacagiz.
Programimizin su islevleri olmali:
1- Hesap Acma
2- Hesaba Para Yatirma
3- Hesaptan Para Cekme
4- Bakiye goruntuleme
5- Programimiz kullanici cikmak isteyene kadar calismali
Hesaplari tutmak icin asagidaki sekilde bir veri yapisi kullanabilirsiniz
hesaplar ana listesi icinde her bir hesap ve bakiyesinin oldugu listeler
Yani
hesaplar = [[hesap_no, bakiye], [hesap_no, bakiye]..... vs]
ORNEK PROGRAM OUTPUTU VE ACIKLAMALAR
# Once ilk hesabimizi aciyoruz
hesap acmak icin a'ya, Para Yatrimak icin y'ye, Para Cekmek icin w'ye, Bakiye kontrolu icin b'ye,
cikis icin q'ya basiniz: a
Bireysel Hesap Numaraniz =  1 # ilk hesap oldugu icin sistem bize hesap numarasi olarak 1 verdi
# burda hesaplar ana listesini yazdiriyoruz size aciklamak icin normalde bunu yazdirmaya gerek,
ama siz de programinizi kontrol icin yazdirabilirsiniz
# Burda goruldugu gibi ilk hesabimiz acildi hesap numaramiz 1 ve hesap bakiyesi 0 Euro
Hesaplar =  [[1, 0]]
# Bir hesap daha acalim ikinci hesabimizi
hesap acmak icin a'ya, Para Yatrimak icin y'ye, Para Cekmek icin w'ye, Bakiye kontrolu icin b'ye, cikis icin q'ya basiniz: a
Bireysel Hesap Numaraniz =  2 # Yeni bir hesap actik ve sistemdeki 2. hesap oldugu icin sistem bize hesap numarasi olarak 2 verdi
Hesaplar =  [[1, 0], [2, 0]] # Gordugumuz gibi hesaplar ana listemizde simdi 2 hesap var ikisinde de bakiye 0 Euro
# Simdi hesaplara para yatiralim
hesap acmak icin a'ya, Para Yatrimak icin y'ye, Para Cekmek icin w'ye, Bakiye kontrolu icin b'ye,
 cikis icin q'ya basiniz: y
hesap numarasi giriniz: 1 # Para yatirmak istedigimiz hesap numarasini sectik 1 numarali hesaba para yatirmak istiyoruz
ne kadar yatirmak istiyorsunuz: 100 # 100 Euro yatiralim
Hesaplar =  [[1, 100], [2, 0]] # Gordugumuz gibi 1 numarali hesabimiz update edildi artik bakiyesi 100 Euro
# Ikinci hesaba da para yatiralim
hesap acmak icin a'ya, Para Yatrimak icin y'ye, Para Cekmek icin w'ye, Bakiye kontrolu icin b'ye,
 cikis icin q'ya basiniz: y
hesap numarasi giriniz: 2 # hesap numarasi olarak 2 girdik
ne kadar yatirmak istiyorsunuz: 200 # Bu hesaba 200 Euro yatirmak istiyoruz
Hesaplar =  [[1, 100], [2, 200]] # son durum 1. hesapta 100 Euro 2. hesapta da 200 euro var
# Bakiye kontrolu yapalim simdi de
hesap acmak icin a'ya, Para Yatrimak icin y'ye, Para Cekmek icin w'ye, Bakiye kontrolu icin b'ye,
cikis icin q'ya basiniz: b
hesap numaranizi giriniz: 2 # 2 numarali hesabin bakiyesini kontrol etmek istiyoruz
Bakiyeniz : 200 # 2 numarali hesabin bakiyesini goruntuledik
# Simdi Para cekmeyi deneyelim
hesap acmak icin a'ya, Para Yatrimak icin y'ye, Para Cekmek icin w'ye, Bakiye kontrolu icin b'ye,
 cikis icin q'ya basiniz: w
hesap numarasi giriniz: 2 # 2 numarali hesaptan para cekelim
ne kadar para cekmek  istiyorsunuz: 50 # cekmek istedigimiz miktar 50 Euro
Hesaplar =  [[1, 100], [2, 150]] # goruldugu gibi 50 Euro cekildikten sonra 2 numarali hesapta 150 Euro kaldi
# Simdi de olmayan bir hesapla ilgili her hangi bir islem yapmaya calisalim
hesap acmak icin a'ya, Para Yatrimak icin y'ye, Para Cekmek icin w'ye, Bakiye kontrolu icin b'ye,
 cikis icin q'ya basiniz: y
hesap numarasi giriniz: 3 # biliyoruz ki hesap numarasi 3 olan bir hesap yok
hesap numarasi bulunamadi # olan bir hhesap numarasi 3 esap olmadigi icin hesap numarasi bulunamadi hatasi aldik
#Simdi 1 numarali hesaptan 150 Euro cekmeye calisalim, ama biliyoruz ki 1 numarali hesabin bakiyesi sadece 100 Euro
hesap acmak icin a'ya, Para Yatrimak icin y'ye, Para Cekmek icin w'ye, Bakiye kontrolu icin b'ye,
 cikis icin q'ya basiniz: w
hesap numarasi giriniz: 1
ne kadar para cekmek  istiyorsunuz: 150
 yetersiz bakiye # gordugumuz gibi 150 euro cekmek istedigimizde yetersiz bakiye hatasi aldik
Hesaplar =  [[1, 100], [2, 150]]
# Ve programimizi sonlandiralim
hesap acmak icin a'ya, Para Yatrimak icin y'ye, Para Cekmek icin w'ye, Bakiye kontrolu icin b'ye,
cikis icin q'ya basiniz: q


"""
#
bireysel_hesap_numarasi = 0
hesap_bakiyesi = 0

Hesaplar = []
basilan_tus = input("hesap acmak icin a'ya, Para Yatrimak icin y'ye, Para Cekmek icin w'ye, "
                    "Bakiye kontrolu icin b'ye,cikis icin q'ya basiniz: ")
# Önce hesap açalım
# # Burda goruldugu gibi ilk hesabimiz acildi hesap numaramiz 1 ve hesap bakiyesi 0 Euro
# Hesaplar =  [[1, 0]]

while basilan_tus != "q":
    hesap = []
    if basilan_tus == "a":
        bireysel_hesap_numarasi += 1

        hesap.append(bireysel_hesap_numarasi)
        hesap.append(hesap_bakiyesi)
        Hesaplar.append(hesap)
        print("Hesaplar: " + str(Hesaplar))
    basilan_tus = input("hesap acmak icin a'ya, Para Yatrimak icin y'ye, Para Cekmek icin w'ye, "
                        "Bakiye kontrolu icin b'ye,cikis icin q'ya basiniz: ")
    # para yatırma yapıyroz şimdi-y
    if basilan_tus == "y":
        hesap_numarasi = int(input("Bireysel hesap numarası giriniz"))
        yatirilacak_miktar = int(input("Ne kadar yatırmak istiyorsunuz"))
        is_hesap_no = ""
        for yatirilacak_hesap in Hesaplar:
            is_hesap_no = True  # hesap varsa True yoksa FAlse olacak
            if yatirilacak_hesap[0] == hesap_numarasi:
                yatirilacak_hesap[1] = yatirilacak_miktar
                break
            else:
                is_hesap_no = False
        if not is_hesap_no:
            print("Hesap numarası bulunamadı")
        print("Hesaplar: " + str(Hesaplar))
    # şimdi de bakiye kontrolü yapalım -b
    if basilan_tus == "b":
        hesap_numarasi = int(input("Bireysel hesap numarası giriniz"))
        # verilen hesap numarasında ne kadar bakiye varsa Bakiyeniz:200 gibi yazdıralım
        for hesap_kontrol in Hesaplar:
            if hesap_kontrol[0] == hesap_numarasi:
                bakiye = hesap_kontrol[1]
                print("Bakiyeniz: " + str(bakiye))
    # Simdi Para cekmeyi deneyelim-w
    if basilan_tus == "w":
        hesap_numarasi = int(input("Bireysel hesap numarası giriniz"))
        cekilecek_miktar = int(input("Ne kadar para çekmek istiyorsunuz"))
        is_hesap_no = ""
        for cekilecek_hesap in Hesaplar:
            is_hesap_no = True
            if cekilecek_hesap[0] == hesap_numarasi and cekilecek_hesap[1] >= cekilecek_miktar:
                cekilecek_hesap[1] -= cekilecek_miktar
                break
            elif cekilecek_hesap[0] == hesap_numarasi and cekilecek_hesap[1] <= cekilecek_miktar:
                print("Yetersiz bakiye")
                break
            else:
                is_hesap_no = False
        if not is_hesap_no:
            print("Hesap numarası bulunamadı")
        print("Hesaplar: " + str(Hesaplar))
    # Hesap Kapatma işlemi
    if basilan_tus == "c":
        hesap_numarasi = int(input("Bireysel hesap numarası giriniz"))
        is_hesap_no = ""
        for hesaplar in Hesaplar:
            is_hesap_no = True
            if hesaplar[0] == hesap_numarasi:
                Hesaplar.remove(hesaplar)
                break
            else:
                is_hesap_no = False
        if not is_hesap_no:
            print("Hesap numarası bulunamadı")
        print("Hesaplar: " + str(Hesaplar))

"""
ne kadar para cekmek  istiyorsunuz: 150
 yetersiz bakiye # gordugumuz gibi 150 euro cekmek istedigimizde yetersiz bakiye hatasi aldik
Hesaplar =  [[1, 100], [2, 150]]
"""
