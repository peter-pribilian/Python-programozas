# Listák folytatása

# Lista indexelése - Meghatározott indexű elem lekérdezése a listából
lista1 = ['Xena', 'Bozsi', 'Vica', 'Eni', 'Ildi']

print(lista1[0])
print(lista1[2])

#Lista szeletelése, felbontása (fontos infó: a második értéket úgy kell venni hogy: érték-1)
print (lista1[0:2])
print (lista1[2:4])
#Lista kiírása bizonyos indextől a végéig
print (lista1[2:])
#Lista utolsó elemének kiírása
print (lista1[-1])

# Többdimenziós listák
#           0       1       2
lista2 = [[1,2,3],[4,5,6],[7,8,9]]
# A lentinél visszaadja a harmadik tömbrész második elemét
print (lista2[2][1])
print (lista2[0][1])

# Lista tartomány beállítása
tartomany=range(100) #0-tól 99-ig
print(list(tartomany))




