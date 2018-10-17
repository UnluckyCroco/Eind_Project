
def fiets_ophalen():

    readfile = open('Stallen.txt', 'r')
    lines = readfile.readlines()

    ov = input('Geef de laatste 4 cijfers van je OV kaart: ')

    for x in lines:
        zin = x.split(';')
        nodig = zin[0]
        if nodig == ov:
            print('je fietsen stalling is:', zin[2], 'en het staat open.')


    from NS_Fietsen_Stalling import inlog_menu
    print(inlog_menu())