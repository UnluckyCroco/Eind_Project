
def fiets_ophalen():

    readfile = open('Stallen.txt', 'r')
    lines = readfile.readlines()

    ov = input('\033[34mGeef de laatste 4 cijfers van je OV kaart: \033[0m')

    for x in lines:
        zin = x.split(';')
        nodig = zin[0]
        if nodig == ov:
            print('\033[32mje fietsen stalling is:', zin[2], 'en het staat open.\033[0m')
            print(' ')


    from Code.NS_Fietsen_Stalling import inlog_menu
    inlog_menu()