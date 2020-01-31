meyveler = ["elma", "muz", "portakal", "mandalina"]
print(meyveler)

if "portakal" in meyveler:
    print(meyveler.index("portakal"))

if "elma" in meyveler:
    print(meyveler.index("elma"))

print("---------------------------------------------------")

meyveler1 = ["elma", "muz", "portakal", "mandalina"]
print(meyveler1)

for eleman in meyveler1:
    if eleman == "portakal" or eleman == "elma":
        print(meyveler1.index(eleman))
