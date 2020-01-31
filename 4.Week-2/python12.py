liste = ['K', 'o', 'd', 'l', 'a', 'm', 'a', 'k']

liste[3] = 's' # 3.sıradaki elemanını kaldırır ve yeni elemanı ekler
liste.insert(liste.index('s') +1, 't')
liste.remove('k')
liste[liste.index('m')] = 'r'
liste.pop()
liste.append('d')
liste.append('a')
print(liste)
