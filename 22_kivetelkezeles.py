
# exception handling (error handling) - kivételkezelés (hibakezelés)
# hiba keletkezésekor a program futása megszakad, a hiba utáni parancsok nem fognak lefutni
#try - except blokkokban adjuk meg, ilyen megadásakor a program végrehajtása nem fog
# csak egy except blokk futhat le egy try-except szerkezetben
#

# lista1=[23,33,43]
#
#
# try:
#     print(bla)
#     #print(lista1[3])
#     #print(1 / 0)
# except NameError as e:
#     print(e, ' - nem létező változó!')
# except IndexError as e:
#     print(e, ' - tartományon kívüli index!')
# except ZeroDivisionError as e:
#     print(e, ' - nullával osztás nem értelmezett!')
#
#
#
#
# print('A program vége!')
#
#
# lista = ['1','2','3', None, '4', '', '5', True, 'Bozsi', '12.64']
#
# for i in lista:
#     try:
#         print(int(i)*2)
#     except: #ha nem tudja lekezelni a kivételt, akkor a continue miatt ugrik a kövi iterációra
#         continue


try:
    #ha a try le tud futni, akkor lefut az "else" és "finally" is
    #ha a try nem tud lefutni, tehát valamelyik except fut le, akkor az "else" nem fut le, de a "finally" igen
    print('bla')
except: #bármennyi except lehet
    print('nem jo valtozo nev')
else: #csak egy lehet
    print('az else')
finally: #csak egy lehet, a finally, ha meg van adva, mindig lefut
    print('Try vege!')


