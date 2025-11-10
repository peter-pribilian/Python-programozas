
#beépített függvények- a python beépített függvényei

#abszolútérték
print(abs(-78))

#enumerate, két értéket ad vissza, az egyik az index, a másik az érték
nevek1 = ['Xena','Bozsi','Vica','Eni','Ildi','Zsuzsi','Evi',10]

for index, nev in enumerate(nevek1):
    print(index,nev)

#float,lényeg az hogy float típusúvá konvertálja a megadott értéket stringként is adhatunk meg számot benne ''-k között
#lásd kényszerű típuskonverzió
print(float(10))

#hex, visszaadja egy szám hexadecimális értékét
print(hex(125))

#input, bevitel billentyűzetről
#osszeg =input ('Adj összeget: ')

#int,  átalakítja int típusúvá a megadott értéket
print(int(12.33))

#len, sztringhossz illetve karakterhossz lekérdezésére használatos
print(len(nevek1))
print(len('Hello,hogy vagy'))

#max, visszaadja a maximális értéket egy beadott argumentumlistából
print(max(10,22,1))

#min, visszaadja a mini értéket egy beadott argumentumlistából
print(min(10,22,1))

#pow, hatványozás
print(2**10)
print(pow(2,10))

#range, határérték megadására szolgál
print(list(range(50,100)))
print(list(range(50,100, 2))) #itt a range(kezdőérték, végérték, léptetőindex)

#reversed, fordytott lista kiírása
print(reversed(nevek1))

#round, egész értékre felkerekítésre és lekerekítésnél használjuk, 0.50-nál lefele kerekít, 0.51-nél már fel
print(round(12.51))
print(round(12.5137373, 4)) #megadhatjuk hogy mennyi tizedesjegyig kerekítsen

#str, stringgé konvertálhatunk értékeket

#sum, összegzés, mindig listát vagy Tuple-t vár paraméternek
print('Az összeg: ',+sum([1,2,3,4,5,6,7,8,9,10]))

