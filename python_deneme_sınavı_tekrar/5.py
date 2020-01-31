"""
 Kullanicidan input olarak bir pozitif tam sayi alan,

ve eger sayi 10'dan kucukse "1 basamakli"

eger sayi 10 ile 100 arasindaysa "2 basamakli"

eger 100'den buyukse ekrana "3 veya daha fazla basamakli" yazdiran python programini yaziniz.
"""
sayi = int(input("Bir sayi gir"))
if sayi < 10:
    print("1 basamaklı")
elif 10 <= sayi < 100:
    print("2 basamaklı")
elif sayi >= 100:
    print("3 veya daha fazla basamakli")
