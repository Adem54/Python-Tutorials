liste = ['K', 'o', 'd', 'l', 'a', 'm', 'a', 'k']
print(liste)
# Liste içindeki bir elemanı değiştirmek
liste[3] = "s"
print(liste)
# listede bir elemanın index ini bulmak
s_index = liste.index("s")
print(s_index)
# listede belirlediğmiz bir indexe eleman eklemek
liste.insert((s_index + 1), "t")  # 4.index e "t" elemanını eklemiş oluyoruz
print(liste)
# istediğimiz bir elemnı direk silmek
liste.remove("k")
print(liste)
# listede bir elemanın yerini değiştirmek  dinamik bir şekilde değiştirmek nasıl olur bakalım
# mesela biz herzaman m yerine r gelsin dersek
liste[liste.index("m")] = "r"
print(liste)
# listeden son elemanı silmek
silinen_eleman = liste.pop()  # dikkat edelim biz burayı bir değişkene atıp yazdırırsak silinen elemanı döndürecektir
print(silinen_eleman)
print(liste)
# listenin sonuna eleman eklemek
liste.append("d")
liste.append("a")
print(liste)
