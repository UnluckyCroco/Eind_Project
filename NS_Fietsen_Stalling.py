def inlog_menu():
    print('1: Registreren')
    print('2: Inloggen')
    optie = int(input('Kies een optie: '))
    if optie == 1:
        from Registreren import fiets_registreren
        print(fiets_registreren())
    else:
        exit()

inlog_menu()
