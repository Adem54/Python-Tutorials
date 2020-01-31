sayi = int(input("Sayi girin: "))
print(sayi + int(str(sayi) * 2) + int(str(sayi) * 3))
# input u int e çevirmese idik o zaman da print te yazdırırken str ye çevirmeyecektik.....
print(123 * sayi)

print(sayi * 100 + sayi * 2 + sayi * 3)

print("------------------------------------------------------")
print(bool("False"))  # True
print(bool(""))  # False
print(bool(None))  # False
print(bool(0))  # False
print(bool(1))  # True
