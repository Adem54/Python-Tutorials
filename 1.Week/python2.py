sayi = int(input("Bir sayı giriniz:"))
# Doğrudan bu şekilde de integer a çevirebiliriz..
sayi = sayi + 5
print(sayi)
# Şuna dikkat edelim int değri tam sayıya çeviren bir değerdir dolayısı ile biz bir string i tam sayıya çevirmeye
# çalışıyorsak eğer o ifadenin string halinde bir tam sayı olması gerekir yoksa hata alabiliriz
# int("merhaba") int("3.15") bunlar zaten tam sayı olmadğı için int ile tam sayıya çevirmeye çalışırsak hata alırız
# str ile string e çevirme genellikle bir int değişkeninin başına bir açıklama yazıp o int değeri yazdırmak istersek
# böyle durumlarda biz int tipindeki değişkenimizi string tipine str(age) şekline çevirerek yazdırmalıyız...

rooms = 3
print("He has " + str(rooms) + " romms in her house")
print(type(rooms))
# Öncelikle biz değişkenimizin tipini öğrenmek için type() methodunu kullanırız.Ayrıca şuna dikkat edelim biz normalde
# print içerisinde bir int değeri str ile string e çevirdikten sonra bir sonraki satırda o değişkenin tipini
# sorgulayınca tipi integer çıkıyor ondan dolayı str ile tiğini stringe çevirme işlemi o satıra has oluyor bir alt
# satıra geçince tekrardan kendi asıl veri tipi integer old için onunla devam edecek
# İşte hemen üst satırdaki anlattığımız sebepten dolayı doğrudan input u int parantezlerine alarak sayı işlemleri
# yapılıyor ki her sayı istediğmizde sayı dönsün doğrudan ve tekrardan int ile sayıya çevirmek zorunda kalmayalım
