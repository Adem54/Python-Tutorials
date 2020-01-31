list = [-5, 2, 2, -3, 4, 0, 5, 1, 4, 1, -3, 2, -1, 4, 1, 5, 4, -1, 5, -5, -5, -3, -2, 4, 2, -2, -3, 2, 5, 0, -4]
# liste içindeki en büyük sayıyı nasıl buluruz
new_eleman = 0
for elem in list:
    if new_eleman < elem:
        new_eleman = elem

print(new_eleman)
