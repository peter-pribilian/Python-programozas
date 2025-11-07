
jelszo = 'kisuborka'
#bemenet billentyüzetről
bemenet = input('Mi a jelszo?')

proba=0
while bemenet != jelszo:
    proba+=1
    if proba==3:
        print('Rendszer lezárva!')
        break
    print('Rossz jelszó, próbáld újra')
    bemenet = input('Mi a jelszo? ')

if bemenet == jelszo:
    print('Hozzáférés engedélyezve!')






