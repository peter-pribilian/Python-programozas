
#fájlok beolvasása
#fájl beolvasás után mindig zárjuk le a close() függvénnyel a fájlt

#file = open('mondasok.txt', 'r', encoding = 'utf-8')

#for sor in file:
 #   print(sor.strip()) # a strip eltünteti a felesleges helyközöket
#
# line = file.readline() #előre be kell olvasni egy sort
# while line: #amint eléri az utolsó sor végét a line változó egy nulla mutatót ad vissza így a while ciklus kilép
#     print(line.strip())
#     line=file.readline()


#file.close()
# with kulcsszó: kontext manager, ennél nem kell lezárni a fájlt
# magától lezárja a fájlt a folyamatok végén
# ha külön mappában helyezem el a beolvasandó fájlt, akkor az útvonalat jelezni kell
with open('mondasok.txt', 'r', encoding='utf8') as file:
    sor=file.readline()

    while sor:
        print(sor.strip())
        sor=file.readline()

#fontos: van readline helyett readlines is, ami azt csinálja hogy listába rakja a sorokat
# és beolvassa a '\n' karaktereket a fájlból

with open('mondasok.txt', 'r', encoding='utf8') as file:
    sor=file.readlines()
    print(sor)

#read, egyszerre beolvassa az egész fájlt
with open('mondasok.txt', 'r', encoding='utf8') as file:
    sor = file.read()
    print(sor)
