def inlog_menu():
    print('1: Registreren')
    print('2: Inloggen')
    optie = int(input('Kies een optie: '))
    if optie == 1:
        from Registreren import fiets_registreren
        return fiets_registreren
    elif optie == 2:
        from Inloggen import inloggen
        return inloggen
    else:
        exit()

inlog_menu()

def keuze_menu():
    print('\033[1;35;0mTEST\033[1;0;0m')
keuze_menu()