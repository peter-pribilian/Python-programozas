
#variable scope - változók láthatósága és élettartama
#léteznek globális és lokális változók is

#function scope, module scope, class scope
a=78
#function scope példa
def test():
   # global változónév, globálissá tudunk tenni lokális változót a "global" kulcsszóval
    a=12 # az "a" és "b" változók lokálisak, csak a függvényen belül érhetők el, kivülről nem láthatóak vagy érhetőek el, így nem írhatóak felül
    b=15 # amint a függvény lefut, az "a" és "b" törlődik a memóriából
    print(a+b)

test()
print(a)
#module scope
#az egész modulon (fájlon) belül elérhető,

#érdekes jelenség:
# a for loopban lévő i változónak törlődnie kellene a ciklus lefutása után
# de mégis lehet használni utána is pl print parancsban
# a globális névtérben úgymond átfolyik és használható lesz
# if, while, for ciklusoknál is megjelenik
# ennek kiküszöbölésére a legjobb megoldás az ha egy függvényben deklaráljuk a ciklust

def test2():
    for i in range(5):
        b=54
        pass
    print(i)
    print(b)

test2()
def test3():
    if True:
        c=78

    print(c)