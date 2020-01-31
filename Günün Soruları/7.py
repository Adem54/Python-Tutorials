"""
Bugun gorece kolay bir sorumuz var

Kullanicinin girdigi kelimenin normal okunusuyla , tersten okunusunun ayni olup olmadigini
kontrol eden python programini yaziniz.

"""
# Bir kelime alırız ve bu kelimeyi iki tane for döngüsü ile döndür biri kelime yi baştan sona gitsin diğeri de sondan
# başa gelsin ve her seferinde karşılaştırsın sıra ile ve farklı olduğu anda bitirsin işlevi aynı ise devam etsin
# ve sonunda eşit ise eşit desin
kelime = input("Bir kelime giriniz")
sayac = len(kelime) - 1
for sayi in range(len(kelime)):

    print(kelime[sayi])

    print(kelime[sayac])
    if kelime[sayi] == kelime[sayac]:
        print("- " + str(kelime[sayi]) + " -ile - " + str(kelime[sayac]) + " -  kelimesi birbirine eşittir")
        print("sayac: " + str(sayac))
        if sayac == 0:
            print("Bu kelime tersi ile birbirine eşittir")
    else:
        print("Bu kelimenin tersten okunuşu ile kendisi birbirine eşit değildir")
        break
    sayac -= 1

    print("----------------------------------------------------------")
