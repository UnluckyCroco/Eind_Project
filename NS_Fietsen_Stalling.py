def inlog_menu():
    print('\033[33mWelkom bij de NS fietsenstalling!\033[0m')
    while True:
        print('\033[34m1: Registreren')
        print('2: Inloggen')
        print('3: Informatie')
        print('4: Afsluiten\033[0m')
        optie = input('\033[36mKies een optie: \033[0m')
        if optie == str(1):
            from Registreren import fiets_registreren
            return fiets_registreren
        elif optie == str(2):
            from Inloggen import inloggen
            return inloggen
        elif optie == str(3):
            from Informatie_Opvragen import informatieIedereen
            return informatieIedereen()
        elif optie == str(4):
            print('\033[31mProgramma sluit af.\033[0m')
            exit()
        else:
            print('\033[31mOngeldige invoer\033[0m')

inlog_menu()

def keuze_menu():
    while True:
        print('\033[34m1: Fiets stallen')
        print('2: Fiets huren')
        print('3: Fiets ophalen')
        print('4: Fiets terugbrengen')
        print('5: Informatie')
        print('6: Uitloggen\033[0m')
        optie = input('Kies een optie: ')
        if optie == str(1):
            from Registreren import fiets_registreren
            return fiets_registreren
        elif optie == str(2):
            from Inloggen import inloggen
            return inloggen
        elif optie == str(3):
            from Fiets_Ophalen import fiets_ophalen
            return fiets_ophalen()
        elif optie == str(4):
            print('ok')
        elif optie == str(5):
            from Informatie_Opvragen import informatieEigenaar
            return informatieEigenaar()
        elif optie == str(6):
            break
        else:
            print('\033[31mOngeldige invoer\033[0m')
    #terug naar inlog_menu
keuze_menu()