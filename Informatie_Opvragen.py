def informatie():
    print('1: Ik heb een fiets in de fietsenstalling.')
    print('2: Ik wil informatie over de fietsenstalling.')

    while True:
        keuze1 = int(input('Kies een optie: '))
        if keuze1 == 1:
            informatieEigenaar()
            break
        elif keuze1 == 2:
            informatieIedereen()
            break
        else:
            print('Foutmelding! Kies optie 1 of 2 alsjeblieft:')

def informatieEigenaar():
    gegevens = open('Gegevens', 'r')
    print('1: Ik heb mijn stalling nummer vergeten.') # heb geen idee wat mensen nog meer zou willen weten..

    while True:
        keuze2 = int(input('Kies een optie: '))

        if keuze2 == 1:

            vnaam = input('Geef je naam: ')
            anaam = input('Geef je tussenvoegsels en je achternaam: ')

            i = False

            for gegeven in gegevens.readlines():
                gegevens_split = gegeven.split(";")
                nummer = gegevens_split[0]
                voornaam = gegevens_split[1]
                achternaam = gegevens_split[2]
                if vnaam == voornaam and anaam == achternaam:
                    i = True

            if i:
                print('Je stalling nummer is: ', nummer) # het probleem hier is dat het programma altijd de laatste stallingnummer print. :(
                break
            else:
                print('Er is een fout in je gegevens.')

            gegevens.close()

def informatieIedereen():
    print('1: Zijn er stallingen vrij?')
    print('2: Wat heb ik nodig om te registreren?') #moet code nog schrijven hiervoor
    print('3: Meer informatie over OV fiets.') # ook hiervoor

    bezet = 0

    while True:
        regel = open('Gegevens', 'r')
        keuze3 = int(input('Kies een optie: '))

        if keuze3 == 1:
            for line in regel.readlines():
                bezet += 1

            if bezet < 701:
                print('Ja, er zijn ', 701 - bezet, ' stallingen vrij.\n')
                regel.close()

            else:
                print('Er zijn geen stallingen beschikbaar.')
            break
informatie()







