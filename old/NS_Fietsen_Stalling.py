from old.Registreren import fiets_registreren
from old.Inloggen import inloggen
from old.Informatie_Opvragen import informatieIedereen, informatieEigenaar
from old.Terugbrengen import fiets_terugbrengen
from old.Fiets_Ophalen import fiets_ophalen
from old.Huren import fiets_huren

print('\033[33m - Welkom bij de NS fietsenstalling!\033[0m')
print('\033[35m - Registreer u bij de fietsenstalling of log in met een bestaand account.\033[0m')
print('\033[31m - Mocht u een typ fout maken, typ dan STOP.\033[0m\n')
def inlog_menu():
    while True:
        print('\033[34m1: Registreren')
        print('2: Inloggen')
        print('3: Informatie')
        print('4: Afsluiten\033[0m')
        optie = input('\033[36mKies een optie: \033[0m')
        if optie == str(1):
            print(fiets_registreren())
        elif optie == str(2):
            return inloggen()
        elif optie == str(3):
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
            from old.Fiets_Stallen import fiets_stallen
            print(fiets_stallen())
        elif optie == str(2):
            print(fiets_huren())
        elif optie == str(3):
            print(fiets_ophalen())
        elif optie == str(4):
            print(fiets_terugbrengen())
        elif optie == str(5):
            print(informatieEigenaar())
        elif optie == str(6):
            f1 = open('Ingelogd', 'w')
            f1.write('')
            f1.close()
            print('\033[1;32;0mU bent nu uitgelogd.\033[1;0;0m')
            inlog_menu()
        elif optie == 'STOP':
            continue
        else:
            print('\033[31mOngeldige invoer\033[0m')

keuze_menu()