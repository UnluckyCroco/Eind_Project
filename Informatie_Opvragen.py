def informatieEigenaar():
    gegevens = open('Gegevens', 'r')

    vnaam = input('Geef je naam: ')
    anaam = input('Geef je tussenvoegsels en je achternaam: ')
    tele = input('Geef uw telefoonnummer: 06-: ')

    i = False

    for gegeven in gegevens.readlines():
        gegevens_split = gegeven.split(";")
        telefoon = gegevens_split[3]
        voornaam = gegevens_split[0]
        achternaam = gegevens_split[1]
        if vnaam == voornaam and anaam == achternaam and tele == telefoon:
            i = True

    if i:
        print('Je  ', )
    else:
        print('Er is een fout in je gegevens.')

    gegevens.close()

def informatieAlgemeen():
    print('1: Zijn er stallingen vrij?')
    print('2: Wat heb ik nodig om te registreren?') #moet code nog schrijven hiervoor
    print('3: Meer informatie over OV fiets.') # ook hiervoor

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
            print('1. Een geldig OV kaart.')
            print('2. Je naam geven.')
            print('3. ')

informatieEigenaar()






