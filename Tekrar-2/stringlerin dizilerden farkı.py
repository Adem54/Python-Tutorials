# Bir listede o listenin içindeki elemanı doğrudan değiştiririz ancak stringde bunu yapamayız ondan dolayı biz bir
# string içinde değiişiklik yapmak istersek yeni bir string oluşturarak bu işlemi yapmalıyız

liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
liste3 = liste1 + liste2
print(liste3)

string1 = "elma"
string2 = "armut"
string3 = string1 + string2
print(string3)

"""
Sonuç olarak biz nasıl ki sayılar için her seferinde döngülerde vs indis+=1 yapıyoruz aynı bu işlemi listelerde
 veya stringlerde de yapabiliriz bunu unutmayalım yani normalde append ile yaptığımız bu işlemi doğrudan da yapabiliriz
"""