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
    print('2: Wat heb ik nodig om te registreren?')
    print('3: Meer informatie over OV fiets.')
    print('4: Terug naar vorige scherm.\033[0m')

    bezet = 0

    while True:
        regel = open('Stallen.txt', 'r')
        keuze3 = int(input('\033[36mKies een optie: \033[0m'))

        if keuze3 == 1:   # als je voor optie 1 kiest.
            for line in regel.readlines():
                bezet += 1

            if bezet < 701:
                print('\033[32mJa, er zijn', 701 - bezet, 'stallingen vrij.\033[0m\n')
                regel.close()

            else:
                print('\033[31mEr zijn geen stallingen beschikbaar.\033[0m')


        elif keuze3 == 2:  #als je voor optie 2 kiest.
            print('\033[32m- De laatste 4 nummers van je OV kaart.')
            print('- Je naam geven.')
            print('- Geldige telefoon nummer\033[0m')


        elif keuze3 == 3:
            print('\033[32m- Uw kunt een fiets huren als je in bezit ben van een geldige OV kaart.')
            print('- Het kost uw €240,- per uur.\033[0m')


        elif keuze3 == 4:
            from NS_Fietsen_Stalling.py import inlog_menu








