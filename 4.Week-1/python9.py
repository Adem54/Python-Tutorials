liste = ["elma", "muz", "portakal", "mandalina"]
for indis in range(len(liste)):
    eleman = liste[indis]
    print(str(eleman) + " indis " + str(indis))
# Normalde, for döngüsü kullanıldığında indise gerek yoktur. Ancak bazen hem elemana hem de elmeanın listedeki indisine
# ihtiyaç duyulabilir. Bunun için illa ki while döngüsüne gerek yoktur,  for döngüsü kullanılarak
# bu şekilde de kullanılabilir:

meyveler = ["elma", "muz", "portakal", "mandalina"]

for index in range(len(meyveler)):
    # range içerisinde sayı döndürmemiz gerekiyor ne sayısı sayaç kaça kadar gitsin diye
    # biz sayacın kaça kadar gitmesini istiyoruz liste içerisinde kaç tane eleman varsa o kadar istiyoruz
    # ondan dolayı bizde direk range içerisine len(liste) yazarsak doğrudan liste içeriisinde kaç tane elman varsa
    # zaten o kadar sayaç sayar ve bizdee bu şekilde yazdığımız listenin içerisindeki elemanları görüntüleyebiliriz
    eleman = meyveler[index]
    print(eleman)
print("------------------------------------------------")

liste = ["Ahmet", "Mehmet", "Kazım", "Tamer"]

for count in liste:
    print(count)
