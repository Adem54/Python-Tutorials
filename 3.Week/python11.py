# Bir yatırım kuruluşu üç aylık dönemlerde müşterilerin yatırdıkları paraya göre kar payı veren bir sisteme sahiptir.
# Bu sistem müşterinin yatırdığı parayı 3 ay boyunca değerlendirip 3 ay sonunda müşteriye yatırdığı paraya ek olarak
# kazandığı kar payını da vermektedir. Müşterinin sistemden 3 ay dolmadan ayrılması durumunda ayrıldığı aya göre ve
# müşterinin bilgilerine göre yatırılan para üzerinden ceza verilmektedir. Sistemde müşterilerin yatırdıkları paraya,
# cinsiyetlerine ve çalışma durumlarına göre kar payı veya caza hesaplamaları yapılmaktadır.
# # Sistemde kar oranları şu şekilde belirlenmektedir;
#    1. ay için;
#      - Müşterinin yatırdığı para 1000TL'den az ise %20 kar, üstünde ise %30 kar verilir.

#  2. ay için;
#     - Erkek müşteriler için yatırılan para 1500TL'den az ise veya müşteri emekli ise %10 kar verilir.
#    - Kadın müşteriler için yatırılan para 1500TL'den az ise ve emekli ise %13 kar verilir.
#   - Diğer şartlarda %5 kar verilir

#    3. ay için;
#       - Emekli erkek müşteriler için yatırılan para 2000TL'den az %10 kar verilir.
#      - Çalışan kadın müşteriler için yatırılan para 2000TL'den az değilse ve 3000TL'den çok değilse %11 kar verilir.
#     - Çalışan erkek müşteriler için yatırılan para 2000TL'den az ise  veya 3000TL'den çoksa %12 kar verilir.
#    - Diğer şartlarda % 6 kar verilir

# Sistemde ceza oranları şu şekilde belirlenmektedir;
#  1. ay için;
#     - Müşteri emekli ise %2 ceza verilir.
#    - Müşteri çalışıyor ve kadın ise %3 ceza verilir.
#   - Müşteri çalışıyor ve erkek ise %4 ceza verilir.

#    2. ay için;
#        - Müşteri emekli değil ise % 5
#       - Müşteri emekli ise % 3

#  3. ay için;
#      - Müşteri kadın değil ise veya emekli değil ise % 6
#      - Müşteri kadın ise ve emekli ise % 4

# Sizden istenen;
#
# Bir while döngüsü kurarak her ay müşterinin çıkmak isteyip istemeyeceğini sormanız ve müşteri çıkmak istemediği
# sürece hesaplamalara devam etmenizdir.