# Bir yatırım kuruluşu 12 aylık dönemlerde müşterilerin yatırdıkları paraya göre kar payı veren bir sisteme sahiptir.
# Bu sistem müşterinin yatırdığı parayı 12 ay boyunca değerlendirip, 12 ay sonunda müşteriye yatırdığı paraya ek olarak
# kazandığı kar payını da vermektedir.
#
# Sistemde kar oranları şu şekilde belirlenmektedir;
# 1. ay için müşterinin yatırdığı para 1000TL'den az ise %20 kar, üstünde ise %30 kar verilir.
#     2. ay için;
#         yatırılan para 1500TL'den az ise %10 kar verilir.
#         yatırılan para 2000TL'den çok ise %12 kar verilir.
#         diğer şartlarda %5 kar verilir
# 3. ay için;
#         yatırılan para 1500TL'den az ise %10 kar verilir.
#         yatırılan para 2000TL'den çok ise %12 kar verilir.
#         diğer şartlarda %4 kar verilir
# Sonraki aylar için;
# Her durumda %3 kar verilmektedir.
# Sizden müşterilere yatırdıkları paraya göre elde edecekleri kar oranlarını hesaplayacak
# programı yazmanız istenmektedir.


yatirilanPara = int(input('Yatırılan para?'))

ay = 1
kazanilanPara = 0

while ay <= 12:
    if ay == 1 and yatirilanPara < 1000:
        kazanilanPara = kazanilanPara + (yatirilanPara * 2 / 10)
    elif ay == 1 and yatirilanPara >= 1000:
        kazanilanPara = kazanilanPara + (yatirilanPara * 3 / 10)
    elif ay == 2 and yatirilanPara < 1500:
        kazanilanPara = kazanilanPara + (yatirilanPara * 1 / 10)
    elif ay == 2 and 1500 < yatirilanPara < 2000:
        kazanilanPara = kazanilanPara + (yatirilanPara * 0.5 / 10)
    elif ay == 2 and yatirilanPara > 2000:
        kazanilanPara = kazanilanPara + (yatirilanPara * 1.2 / 10)
    elif ay == 3 and yatirilanPara < 1500:
        kazanilanPara = kazanilanPara + (yatirilanPara * 1 / 10)
    elif ay == 3 and 1500 < yatirilanPara < 2000:
        kazanilanPara = kazanilanPara + (yatirilanPara * 0.4 / 10)
    elif ay == 3 and yatirilanPara > 2000:
        kazanilanPara = kazanilanPara + (yatirilanPara * 1.2 / 10)
    elif ay > 3:
        kazanilanPara = kazanilanPara + (yatirilanPara * 0.3 / 10)
    print(str(ay) + ". ay elde edilen kar  " + str(round(kazanilanPara, 2)))
    ay = ay + 1

print("Son durumda kar olarak elde kalan para :  " + str(round(kazanilanPara, 1)))
print("Yatırılan Para : " + str(yatirilanPara))
kar_orani = (kazanilanPara / yatirilanPara) * 100
print(str(ay - 1) + " ay sonunda elde edilen kar oranı : %" + str(round(kar_orani, 2)))

# when the (ndigit+1)th digit is =5
print(round(2.665, 2))

# when the (ndigit+1)th digit is >=5
print(round(2.676, 2))

# when the (ndigit+1)th digit is <5
print(round(2.673, 2))
