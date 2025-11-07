
# logikai operátorok

# and or not -nincs karakteres megadás mint java-ban, pl &&

szam1=2
szam2=4
#       True                True
print(szam1 < szam2 and szam1 == 2)

print(szam1 < szam2 and szam1 == 3)
print(szam1 < szam2 or szam1 == 3 or 5 > 6)

#       true                not false   = True
print(szam1 < szam2 and not szam1 == 3 )