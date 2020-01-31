liste = [[1, 100], [2, 200]]
# 0.indislerdeki değerlerin içerisinde var mı yok mu konntrol edelim ve sonundas tek mesaj verelim
# Not eğer bir liste içerisinde bir eleman sorugluyoruz ve tek bir değer dönmesini istiyorsak o zamn True False
# ile boolean değerler ile öözebiliriz
for eleman in liste:
    is_hesap = False
    if 3 != eleman[0]:
        is_hesap = True
if is_hesap:
    print("Böyle bir numara mevcut değildir")
