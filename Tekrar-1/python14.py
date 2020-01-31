"""
Bir yatırım kuruluşu 12 aylık dönemlerde müşterilerin yatırdıkları paraya göre kar payı veren bir sisteme sahiptir.
 Bu sistem müşterinin yatırdığı parayı 12 ay boyunca değerlendirip, 12 ay sonunda müşteriye yatırdığı paraya ek olarak
  kazandığı kar payını da vermektedir.

Sistemde kar oranları şu şekilde belirlenmektedir;
    1. ay için müşterinin yatırdığı para 1000TL'den az ise %20 kar, üstünde ise %30 kar verilir.
    2. ay için;
        yatırılan para 1500TL'den az ise %10 kar verilir.
        yatırılan para 2000TL'den çok ise %12 kar verilir.
        diğer şartlarda %5 kar verilir
    3. ay için;
        yatırılan para 1500TL'den az ise %10 kar verilir.
        yatırılan para 2000TL'den çok ise %12 kar verilir.
        diğer şartlarda %4 kar verilir
  Sonraki aylar için;
        Her durumda %3 kar verilmektedir.
Sizden müşterilere yatırdıkları paraya göre elde edecekleri kar oranlarını hesaplayacak programı yazmanız istenmektedir.
"""
yatirilan_para = int(input("Yatırılan para miktarını giriniz"))
ay = 1
kazanilan_para=0
while ay <= 12:
    if ay == 1 and yatirilan_para < 1000:
        kazanilan_para = kazanilan_para + yatirilan_para * 0.2
    elif ay == 1 and yatirilan_para >= 1000:
        kazanilan_para = kazanilan_para + yatirilan_para * 0.3
    if ay == 2 and yatirilan_para < 1500:
        kazanilan_para = kazanilan_para + yatirilan_para * 0.1
    elif ay == 2 and yatirilan_para >= 2000:
        kazanilan_para = kazanilan_para + yatirilan_para * 0.12
    elif ay == 2 and 1500 < yatirilan_para < 2000:
        kazanilan_para = kazanilan_para + yatirilan_para * 0.05
    if ay == 3 and yatirilan_para < 1500:
        kazanilan_para = kazanilan_para+ yatirilan_para * 0.1
    elif ay == 3 and yatirilan_para >= 2000:
        kazanilan_para = kazanilan_para + yatirilan_para * 0.12
    elif ay == 3 and 1500 < yatirilan_para < 2000:
        kazanilan_para = kazanilan_para + yatirilan_para * 0.04
    if ay > 3:
        kazanilan_para = kazanilan_para + yatirilan_para * 0.03
    ay += 1


print(round(kazanilan_para,2))