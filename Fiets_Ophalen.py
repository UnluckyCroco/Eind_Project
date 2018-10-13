def fiets_ophalen():
    readfile = open('Gegevens', 'r')

    while True:
        inlogvn = input('Geef je voornaam: ')
        inlogan = input('Geef je tussenvoegsel en je achternaam: ')
        inlogww = input('Geef je wachtwoord: ')

        i = False

        for gegeven in readfile.readlines():
            gegevens_split = gegeven.split(";")
            wachtwoord = gegevens_split[2]
            voornaam = gegevens_split[0]
            achternaam = gegevens_split[1]
            if inlogvn == voornaam and inlogan == achternaam and inlogww == wachtwoord:
                i = True

        if i:
            print('Je fiets is vrij.')
            break
        else:
            print('Er is een fout in je gegevens.')

fiets_ophalen()