
# pass, continue és break kulcsszavak
# a break és continue parancsokat ciklusokban használhatjuk
# a pass-t bárhova berakhatjuk pl: ciklusokban,  feltételekben, függvényekben
# pass: placeholder (helyettesítő) jelzőnek használhatjuk, olyan esetben amikor nem
# tudjuk még hogy mi kerüljön bele a ciklus törzsébe, csak azt tudjuk, hogy szükség lesz a ciklusra
# if, while , for ciklusok esetén használhatjuk
#while True:
#    pass


#break hatására kilép az aktuális ciklusból és a végrehajtás áthelyezi a cikluson kivülre
for i in range(10):
    if i==5:
        break
    print(i)
print("------------------------")
szam=0
while True:
    print(szam)
    if szam==5:
        break
    szam+=1

#continue hatására skippel minden olyan parancsot ami a continue után van a ciklusban és átugrik a következő iterációra
print("------------------------")
for i in range(10):
    if i==5:
        continue
    print(i)
print("------------------------")
# 20-nál alacsonyabb páratlan számok kiíratása
szamlalo=0
while True:
    szamlalo+=1
    if szamlalo % 2==0:
        continue
    print(szamlalo)
    if szamlalo>20:
        break