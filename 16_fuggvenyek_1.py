
#függvények
nevek1 = ['Xena','Bozsi','Vica','Eni','Ildi','Zsuzsi','Evi',10]
nevek2 = ['Pityu','Ati','Peti','Bence','Feri']

#függvény definíció
def nev_printer(nev_lista):
    for nev in nev_lista:
        if isinstance(nev,str):   #isinstance(nev, str) -> megkérdezi, hogy a "nev" változó tartalma string-e
            print(nev.upper())
        else:
            print('Nem string típus, hanem: '+str(type(nev)))   # str(type(nev)) -> visszaadja a típusát a "nev" változónak

#függvény hívása
nev_printer(nevek1)
nev_printer(nevek2)