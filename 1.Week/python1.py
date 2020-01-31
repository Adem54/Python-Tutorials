print("Welcome to Python")
print("Kardeş merhaba")
print(5)
# python da print komutunu çalıştırırken öncesinde boşluk bırakmamalıyız hata alabiliriz...
# print() komutu büyük harf küçük harf duyarlılığı vardır ondan dolayı büyük yazamayız küçük yazılmalı
# syntax hatası demek parantez i kapatmayı unutmak veya tırnak işaretini koymamak ya da yanlış koymak
# Ama python komutunu büyük harfle yazarak yanlış yazmak yazım yanlışıdır syntax hatası değildir
# = işareti ile assign yani atama işlemi yapılır atama nedir bakalım
# CTRL+ ALT +L ile format code yapabiliriz...
# İşlem önceliklerine bakacak olursak normalde matemik ile hemen hemen aynı zaten öncekikle parantez önceliğine dikkat
# etmeliyiz parantez-* ve / ardından + ve - gelir

myNumber = 9
print(myNumber)
# Unutmayalım eşittir in solundaki değişken önceden değer atanmış olsa bile sola koyulduğu zaman biz ona yeniden değer
# atıyoruz anlamına gelecektir.Dolayısı ile mesela bir döngü içinde kullansak döngü her başladığında myNumber çalışarak
# o zaman myNumber ın o anki değeri gidip sağdaki myNumber a eşit olur 5 saysını ekler ve soldaki myNumber değerine
# yeni bir atama yapmış olur....Ondan dolayı buna dikkat edelim...
# python dilinde ondalıklı sayılar , virgül ile değil . ile ayrılır 3,14 yanlıştır 3.14 doğrudur
# python dilinde
# python da string değerler de toplama işlemi ile birleştirme yapılır ancak string değerler arasında
# çıkarma işlemi yoktur
# Concatenation(kınkıtıneyşın)= string birleştirme olayına bu ad verilir
# DEĞİŞKEN ATAMA
# Değişken, bilgisayarın geçici belleğinde bilgi saklamak için ayrılan hafıza alanına verilen addır.
# Program içinde bir değişken tanımlandığında bellekte onun için bir yer ayrılır. Aslında değişken tanımlamak,
# fiziksel hafıza alanına sembolik bir isim atamaktır. Bu hafıza alanında, sayı, metin veya daha karmaşık bilgiler
# tutulabilir.
# Değişkenler geçicidir. Program çalıştığı sürece erişebiliriz. Program sonlandığı zaman tuttukları bilgi kaybolur.
# Program sonlandığında sonra bilginin kaybolmasını istemiyorsak, dosya veya veri tabanlarına yazarız.
# python da değişken oluştururken javascriptteki gibi başına var,let,const getirmemize gerek yok doğrudan yazabiliriz...
# Ayrıca pythonda birşey yazdırırken ; sonunda noktali virgül kullanmaya gerek yok..
# Python'da değişkenin değerini değiştirmek, ilk defa değer vermekten farksızdır.

myNumber = myNumber + 5
# Burda dikkat edelim myNumber ın zaten bir değeri vardı ama biz yeniden değer atıyoruz ekranda yeni bir statement
# cümleye yani satır a geldiğimiz zaman eğer = ifadesi varsa solda kalan değişkene önceden değeri olsa bile yeniden
# değer atanıyor demektir ve sağda kendi değeri +5 olduğu zaman eski değerine 5 ekleyerek yeni değer atanıyor demektir
# değişken adı yazarken arasında boşluk olmaz başlangıcı sayı ile olmaz ama _ ile başlabilir.
# Birde python un kendisinin method ya fonks olarak kullandığı isimleri değişken ismi olarak
# kullanamayız
# Pyhton Keyword i internette bulabiliriz
# ÖRnek python keyword list and       del       from      not       while
# pythonda değişkenlere birden fazla kelime vermek istersek ya aralarına _ ile birleştiiririz ya da camelCase
# kullanırız
# OKUNUR KOD YAZMANIN ÖNEMİİ!!!
# Okunur kod yazmak değişkenleri hangi amaçla kullanılıyorsa o amaca uygun isimlerle isimlendirmek çok önemlidir...
# Sonradan o değişkenle tekrar çalışılacağı zaman anlaşılması açısından çok  hayati önem taşır ve
# bu isimler tabiki ingilizce olmalıdır

print(myNumber)

print(3 * "5")
print(3 * 5)
print("3*5")

toplam = 15
toplam + 15
# toplam değişkenine biz bir üstte sadece toplam + 15 diyerek aslında hiçbirşey yapmamış olduk yani toplam değişkeninin
# artması için bu değerin tekrardan toplam değişkenine aktarılması gerekir
name = input("Adınızı giriniz:")
input("Soyadınızı giriniz:")
bornDate = input("Doğum tarihinizi giriniz:")
num = int(bornDate)
age = 2019 - num
# Not: python da bir integer ile string + ile birleştirilemez(concetanation) hata alırız bunda dikkat birleştirmek
# için integer olan ifadeyi str ile stringe çeviririz
# input içerisine rakam yazdığımızda tipi stringdir eğer sayısal işlemler için kullanacaksak o zaman önce tipini
# integer a çevirmeliyiz.int(age) bu şekilde integer a çeviririz.str(age) bu şekilde de integer ı string e çeviririz
print("Yaşınız: " + str(age))
print(type(age))  # integer gelir
print(type(name))  # string gelir

print("Yaşınız: " + input("Yaşınız kaçtır: "))
# çıktı olarak Yaşınız 34 sonucunu verir
