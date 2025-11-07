
# if utasítások, feltételek
# ugyanúgy mint a while és for ciklusoknál, az if törzsét is a sorbehúzások jelzik
# lehetséges if elágazások beágyazása, van elif és else ág
# többszörös feltételes ágak esetén csak egyet hajt végre, az utána következőket ignorálja
if False:
    print('igaz')

eletkor = 17

if eletkor<18:
    if eletkor>=16:
        print("Egy kis sört megihatsz.")
    else:
        print("Se cigi, se pia!")
elif eletkor>=18 and eletkor<30:
    print("Jo bulizast!")
elif eletkor>=30 and eletkor<65:
    print("Munka és család.")
else:
    print("Nyugdíjas élet, meg onokák")