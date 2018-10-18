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
                        print('\033[32mInlog Succesvol\033[0m')
                        return '\033[32mInlog Succesvol\033[0m'


        print('\033[31mDeze combinatie is incorrect. Ga terug naar menu om te registeren of probeer opnieuw.\033[0m')
        while True:
            reg = input('\033[34mTyp Menu of Opnieuw: \033[0m')
            if reg == 'Menu':
                reg = ' '
            if reg == 'Opnieuw':
                break
            else:
                print('Foute input.')

# from NS_Fietsen_Stalling import keuze_menu
# print(keuze_menu())