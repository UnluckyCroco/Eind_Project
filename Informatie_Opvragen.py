import csv
def informatieEigenaar():
    gegevens = open('Gegevens', 'r')
    gegeven = gegevens.readlines()
    name = input('Vul naam in: ')

    for item in gegeven:
        regel = item.split(';')
        naam = regel[0]
        achternaam = regel[1]
        ww = regel[2]
        tel = regel[3]
        ov = regel[4]
        if naam == name:
            print('\033[32mGeregistreerde naam: \033[0m', naam, achternaam)
            print('\033[32mGeregistreerde wachtwoord: \033[0m', ww)
            print('\033[32mGeregistreerde telefoon nummer: \033[0m', tel)
            print('\033[32mGeregistreerde OV: \033[0m', ov)



    gegevens.close()

def informatieIedereen():
    print('\033[32m1: Zijn er stallingen vrij?')
    print('2: Wat heb ik nodig om te registreren?') #moet code nog schrijven hiervoor
    print('3: Meer informatie over OV fiets.\033[0m') # ook hiervoor

    bezet = 0

    while True:
        regel = open('Gegevens', 'r')
        keuze3 = int(input('Kies een optie: '))

        if keuze3 == 1:   # als je voor optie 1 kiest.
            for line in regel.readlines():
                bezet += 1

            if bezet < 701:
                print('Ja, er zijn ', 701 - bezet, ' stallingen vrij.\n')
                regel.close()

            else:
                print('Er zijn geen stallingen beschikbaar.')
            break

        elif keuze3 == 2:  #als je voor optie 2 kiest.
            print('1. De laatste 4 nummers van je OV kaart.')
            print('2. Je naam geven.')
            print('3. ')







