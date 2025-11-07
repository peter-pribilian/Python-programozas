
a=10
b=20
# függvények, lehet paraméteres és paraméter nélküli is
# lehet visszatérési értéke: return utasítás, de ez csak értéket ad vissza
# ha ki akarjuk iratni akkor vagy változóba kell kimenteni a függvény visszatérési értékét, vagy ki kell printelni a függvényt

def osszeadas1():
    print(a+b)
#default paraméter: a függvény definícióban van definiálva és értéket is itt kap
def osszeadas2(a,b,c=4):
    return a+b+c
#változó számú paraméterek jelölése: *args
# tetszőleges lehet az elnevezése, az "args" csak névkonvenció
def osszeadas3(*args):
    return sum(args)

def udvozlesek(*args):
    koszones = 'Ennyi féle köszönés létezik: '
    for k in args:
        koszones +=k
        koszones +=", "
    print(koszones[0:len(koszones)-2])

osszeadas1()
#print(osszeadas2(45,25))
osszeg=osszeadas2(45,22)
print(osszeg)
print('------')
print(osszeadas3(10,23,44,55))

udvozlesek('hali', 'cső', 'csákó')
