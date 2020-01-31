
def asal_mi(sayi):
    # Eger sayi 2 ise True
    if sayi == 2:
        return True
    # Eger sayi 2 den kucukse False
    elif sayi < 2:
        return False
    # Diger durumlarda
    else:
        # 2 den baslayarak sayiya kadar olan tum sayilar icin
        for i in range(2, sayi):
            # Eger tam bolunurse False
            if sayi % i == 0:
                return False
        # True
        return True


print(asal_mi(73))
print(asal_mi(101))