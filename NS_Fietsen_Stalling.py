def inlog_menu():
    print('1: Registreren')
    print('2: Inloggen')
    optie = int(input('Kies een optie: '))
    if optie == 1:
        print('\n')
        from Registreren import fiets_registreren
        return fiets_registreren
    elif optie == 2:
        print('\n')
        from Inloggen import inloggen
        return inloggen
    else:
        exit()

inlog_menu()
