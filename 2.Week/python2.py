age = True
married = True
# not True veya False boolean değerleri tersine çevirir ve 0 değeri False dur ama 0 dan büyük değerler True
if not married:
    print("Bu aday bekardır")
else:
    print("Bu aday evlidir ")
# Mümkünse not ı az kullanmamız gerekir kodun okunabilirliğini azaltan bir ifadedir not
# and or ve not öncelik de neye bakılır
# önce parantez içi hesaplanır
# sonra not
# ardından and
# en son or işlemleri yapılır.

aldigi_ders_sayisi = int(input("Aldığın ders sayısını gir: "))

if aldigi_ders_sayisi < 5:
    print("Geçmek istiyorsan hiç bir dersten kalamazsın")
elif (aldigi_ders_sayisi >= 5 and aldigi_ders_sayisi <= 8):
    print("Geçmek istiyorsan en fazla bir dersten kalabilirsin")
elif aldigi_ders_sayisi > 8:
    print("Geçmek istiyorsan en fazla üç dersten kalabilirsin")

yas = int(input("Çocuğunuzun yaşını giriniz"))
# 5-14 yaş arası grunskule ye gitmek zorunlu
# 0-5 yaş kreşe gidebilir
# 5-10 yaş barneskuleye gidebilir
# 14-16 arası vidorogoonde ye gidebilir
# 16 dan sonra da ister üniversite isterse de meslek okuluna gidebilir

if yas < 14:
    if yas < 5:
        print("Çocuğunuz ana okuluna gitmelidir")
    else:
        print("Çocuğunuz barneskule de olmalıdır")

else:
    if yas <= 16:
        print("Çocuğunuz vidorogoonde eğitimi almalıdır")
    else:
        print("Gerisi size kalmış ister vidorogoondeye devam eder isterseniz de etmezsiniz")
# Eğer biz if in True değeri ne ise o değer içerisinde de gruplandırma yapacaksak yani yas<14 içinde
# birde 14 yaş tan küçük çocuklar arası bir gruplandırma yapıp mesela eğer yaşı 5 ten küçükse ana okulu
# 5-14 arası da barneskule ye gidecek yazdırmak istersek o zaman gidip
# if yas < 14 ün hemen altına bir if bloğu daha açarız

