print('\033[33m - Welkom bij de NS fietsenstalling!\033[0m')
print('\033[35m - Registreer u bij de fietsenstalling of log in met een bestaand account.\033[0m')
print('\033[31m - Mocht u een typ fout maken, typ dan STOP.\033[0m')
def inlog_menu():
    while True:
        print('\033[34m1: Registreren')
        print('2: Inloggen')
        print('3: Informatie')
        print('4: Afsluiten\033[0m')
        optie = input('\033[36mKies een optie: \033[0m')
        if optie == str(1):
            from Registreren import fiets_registreren
            print(fiets_registreren())
        elif optie == str(2):
            from Inloggen import inloggen
            return inloggen
        elif optie == str(3):
            from Informatie_Opvragen import informatieIedereen
            print(informatieIedereen())
        elif optie == str(4):
            print('\033[31mProgramma sluit af.\033[0m')
            exit()
        elif optie == 'STOP':
            continue
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
            from Fiets_Stallen import fiets_stallen
            print(fiets_stallen())
        elif optie == str(2):
            from Huren import fiets_huren
            print(fiets_huren())
        elif optie == str(3):
            from Fiets_Ophalen import fiets_ophalen
            print(fiets_ophalen())
        elif optie == str(4):
            from Terugbrengen import fiets_terugbrengen
            print(fiets_terugbrengen())
        elif optie == str(5):
            from Informatie_Opvragen import informatieEigenaar
            print(informatieEigenaar())
        elif optie == str(6):
            print('\033[1;32;0mU bent nu uitgelogd.\033[1;0;0m')
            inlog_menu()
        elif optie == 'STOP':
            continue
        else:
            print('\033[31mOngeldige invoer\033[0m')

keuze_menu()