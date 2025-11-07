
# lists (mutable) - listák (módosítható)
# több érték tárolására alkalmas

#szintaktika
lista1= []
print(lista1)
#érték felvitele már létező listába
#java-val ellentétben itt nem csak egyféle típusú adat kerülhet bele a tömbbe
#pl: belekerülhet int és string is egy listába

lista1.append(100)
lista1.append(102)
lista1.append(103)
lista1.append(104)
lista1.append(105)

print(lista1)

lista1.append("Eniko")
lista1.append("Aniko")
lista1.append("Eniko")
print(lista1)

#Listaelem törlése
lista1.remove("Eniko")
print(lista1)

#Lista teljes törlése
#lista1.clear()

#Listába beszúrás (elemszám: méret-1 tehát 0-tól van a számolás)
lista1.insert(5,"Bozsi")
print(lista1)

#Lista elemeinek megfordítása
lista1.reverse()
print(lista1)

#Lista elemeinek növekvő sorrenbe helyezése (csak számokat vagy csak betűket tartalmazó listák esetén működik)
lista2 = [15, 8, 78, 23, 1, 65, 184]
lista2.sort()
print(lista2)

lista3 = ['Xena', 'Bozsi', 'Vica', 'Eni', 'Ildi']
lista3.sort()
print(lista3)

#Lista elemszámának lekérdezése

print('A harmadik lista elemeinek száma:',len(lista3))