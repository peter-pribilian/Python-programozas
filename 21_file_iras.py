
# 'r' - read (olvasás)
# 'w' - write (írás)
# 'a' - append (hozzáfűzés, mellékel)

# ha az open() fgv-el olyan fájlra hivatkozunk ami nem létezik, akkor létrehozza
# ha az open() fgv-el olyan fájlra hivatkozunk ami már létezik, akkor felülírja


# with open('mondasok.txt', 'r', encoding='utf8') as infile:
#     with open('out.txt', 'w', encoding='utf-8') as outfile:
#         szoveg ='Egy jó szalonna, kalbász, meg egy jó sör, bármikor jöhet.'
#         file.write(szoveg)
#         print(szoveg)

#kiolvassa a mondasok.txt tartalmát és átmásolja az out.txt fájlba
with open('mondasok.txt', 'r', encoding='utf8') as infile:
    with open('out.txt', 'w', encoding='utf-8') as outfile:
        sor=infile.readline()

        while (sor):
            outfile.write(sor)
            sor=infile.readline()

#hozzáadja a fájl végéhez az új sort
with open('out.txt', 'a', encoding='utf8') as file:
    uj_sor='\nNem akarásnak nyögés a vége.'
    file.write(uj_sor)