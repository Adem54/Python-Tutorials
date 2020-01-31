# 10 dan küçük sayıları yazdırırken 5 hariç hepsini yazdırmak istersek bu şekilde ya da
counter = 10
while counter > 0:
    counter = counter - 1
    if counter != 5:
        print("Counter: " + str(counter))

# continue ile biz bir ifadeyi while ile yazdırırken içlerinden bir tanesinin yazılmasını istemessek ya da
# biz if koşulunda eğer koşul sağlamasına rağmen hiçbirşey yazmasını istersek o zaman continue ile devam yazarız
# Normalde if ile koşul uyuyorsa ve biz yazdırmak istemiyorsak print ile sadece boşluk bırakırsak gider oraya
# boşluk bırakır o satıra ama biz o satıra hiçbirşey yazmasın ama bir sonraki kodu da o satıra yazsın istersek o zaman
# continue ile birşey yazmadan devam et deriz
sayi = 10
while sayi > 0:
    sayi = sayi - 1
    if sayi == 5:
        continue
    print("Sayı: " + str(sayi))



