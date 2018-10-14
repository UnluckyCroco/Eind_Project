def inloggen():
    while True:
        naam = input('Voornaam: ')
        ov = input('Laatste 4 cijfers van uw ov: ')
        wachtwoord = input('Wachtwoord: ')
        x = open('Gegevens','r')
        lines = x.readlines()
        for line in lines:
            y = line.strip('\n')
            z = y.split(';')
            if naam == z[0]:
                if ov == z[4]:
                    if wachtwoord == z[2]:
                        return'test'

        print('Deze combinatie is incorrect.')
        while True:
            reg = input('Typ Menu of Opnieuw: ')
            if reg == 'Menu':
                reg = ' '
                from NS_Fietsen_Stalling import inlog_menu
                print(inlog_menu())
            if reg == 'Opnieuw':
                break
            else:
                print('Foute input.')

print(inloggen())