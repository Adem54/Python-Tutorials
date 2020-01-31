# for döngüsü daha çok belli bir liste yada serinin her elemanı için bir kod parçası çalıştırmak için kullanılır.

# Aşağıdaki örnekte range fonksiyon 0'dan 10 kadar olan sayılardan bir liste oluşturur
i = 0
while i <= 9:
    print("Daha çok çalışacağım, söz!")
    i = i + 1
for sayi in range(20):
    print(sayi)

for sayi in range(10):
    print("Daha çok çalışacağım, söz!")
