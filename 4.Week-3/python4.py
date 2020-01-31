# Verilen bir sayının o.b.e.b ini bulan fonksiyonu yazalım

def obeb(sayi1, sayi2):
    bolen = 2
    while bolen < sayi1 and bolen < sayi2:
        if sayi1 % bolen == 0 and sayi2 % bolen == 0:
            en_buyuk_ort_bol = bolen  # biz burda direk bolen i en_buyuk_ort_bol değişkenini atama yapıyoruz ki zaten en
            # son en büyük değer e eşit olacağı için biz otomatik olarak en büyük ortak bölen i değişkene atamış oluruz
        print("bolen: " + str(bolen))
        bolen = bolen + 1
    return en_buyuk_ort_bol


print(obeb(32, 48))
