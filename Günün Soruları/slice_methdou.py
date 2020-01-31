a = [10, 12, 13, 17, 19, 21, 24, 27, 31, 34]
print(a[:2])
# add 1 number
# a[:0] = [30]

# add two numbers
# a[:0] = [40, 50]
# print(a)
b = a[:]  # Bir listenin kopyasını almak içi kullanırız
print(b)
# Normalde parmetre olarak 3 eleman alır a[star,stop,step] şekllindedir ve star başlangıç indisi stop duracağı
# indis ve step ise adım sayısnı gösterir
a[3:5:1] = ["Kemal"]  # 3.indise kadar olan elemanları yazıyor sonra 3.indise Kemal i yazar sonra da
# ama 3.indisten sonra 5.indise kadar olan elemanları yazmaz 5.indisten itibaren elemanları yazmaya devam eder
a[3:3:1] = ["Kemal"]  # bu şekilde de "Kemal" elemanı ekstra liste içerisine ekliyor çünkü 3.indise kadar elemanları
# alıyor daha sonra elemanımız ekliyor ve sonrasında tekrardan 3.indsten başlayarak devam ediyor ve bu şekilde
# listemizin içerisine listeden eleman silmeden elemean eklemiş oluruz
print(a)
print(a[3:5:1])  # 3.indisten alarak  başla 5.indise kadar 5 dahil değil 1 er 1er al yaz demek

a[0:3]  # demek 0.indisten 3 dahil değil 3 e kadar a listesinin elemnlarını alır
a[3:]  # 3.indisten başlar ve a listesinin elemanlarının 3.indisten başlayarak listenin sonuna kadar alır
a[:2]  # Burda da 2.indise kadar elemanları alır 2.indis dahill değil yani a nın 0 ve 1.indisini alır
b = a[:]  # Bir listenin kopyasını almak içi kullanırız

x = [2, 6, 9, 7, 12, 14, 16]
# Dikkat edersek burda biz x listesinden bir elemanı silmiş oluyoruz aslında
first_list = x[:2]
second_list = x[3:]
print(first_list + second_list)
