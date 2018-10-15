def inloggen():
    while True:
        naam = input('Voornaam: ')
        ov = input('Laatste 4 cijfers van uw ov: ')
        wachtwoord = input('Wachtwoord: ')
        file = open('Gegevens','r')
        lines = file.readlines()
        for line in lines:
            y = line.strip('\n')
            z = y.split(';')
            if naam == z[0]:
                if ov == z[4]:
                    if wachtwoord == z[2]:
                        file.close()
                        f1 = open('Ingelogd','a')
                        f1.write(line)
                        f1.close()
                        return'\033[1;32;0mInlog Succesvol\033[1;0;0m'

        print('\033[1;31;0mDeze combinatie is incorrect. Ga terug naar menu om te registeren of probeer opnieuw.\033[1;0;0m')
        while True:
            reg = input('\033[1;34;0mTyp Menu of Opnieuw: \033[1;0;0m')
            if reg == 'Menu':
                reg = ' '
                from NS_Fietsen_Stalling import inlog_menu
                print(inlog_menu())
            if reg == 'Opnieuw':
                break
            else:
                print('Foute input.')

print(inloggen())