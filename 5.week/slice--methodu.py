# Mutable
liste = [3, 11, 18, 15, 2, 12, 4]
newliste1 = liste
newliste2 = liste[:]  # burda biz liste listesinin kopyasını newliste2 ye eşitliyourz ki bizim listelerde yapmamız
# gereken bizden beklenen olay budur
liste[2] = 123
print(liste)
print(newliste1)
print(newliste2)

# Immutable
x = 12
y = x
x = 8
print(x)  # x değişmesine rağmen y değişmedi çünkü immutable değişmez primetiv verilerde bir veriyi başka bir
# veriye atayınca o verinin değerini kopyalayıp yeni veriye atıyor ondan dolayı ben tekrardan x e yeni değer atamama
# rağmen y bundan etkilenmiyor
print(y)

# slice işlemi
liste = [3, 11, 18, 15, 2, 12, 4]
print(liste[0:3:1])  # 0.indisten başla 3.indise kadar al 3.indis dahil değil ve 1 er 1 er al
print(liste[0:3:2])
print(liste[0:5])  # Doğrudan liste içerisindeki veriler 0.indisten başla 5.indise kadar al demiş oluyoruz...

# Ayrıca şuna bakalım biz listelerde referans tip elemanlardır ve eşitlik karşılaştırmasında liste de değerini
# karşılaştırmaz adreslerii karşılaştırır
liste1 = [2, 6, 9, 12, "Ahmet"]
liste2 = [2, 6, 9, 12, "Ahmet"]
# liste1 ve liste2 de de değerler aynı referanslar farklıdır
liste4 = liste1  # Hem değerler aynı hem referanslar aynı
# liste1 ve liste2 değerler aynı referanslar farklıdır
liste3 = liste1[:]  # Değerler aynı referanslar farklı
if liste1 == liste2:
    print("liste1 ve liste2 birbirine eşittir")
else:
    print("liste1 ve liste2 birbirine eşit değildir")

if liste1 == liste3:
    print("liste1 ve liste3 birbirine eşittir")
else:
    print("liste1 ve liste3 birbirine eşit değildir")
