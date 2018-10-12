def inlog_wachtwoord():
    ov = input('Wat zijn de laatste 4 cijfers van uw ov kaart?: ')
    ww = input('Wat is uw wachtwoord: ')
    if len(ww) < 6:
        print('Het nieuwe wachtwoord moet minstens 6 karakters zijn!')
    if ov.isdigit():  # checkt als ov wel uit nummers bestaat
        nummer = ov
    else:
        nummer = 'niks'
    while ov is not nummer:
        print('OV nummer mag alleen cijfers bevatten')
        ov = input('Geef de laatste 4 nummers van uw OV-chipkaart: ')
        if ov.isdigit():
            nummer = ov
        else:
            nummer = 'nikskhk'
    while len(ov) is not 4:  # checkt of het ov 4 tekens lang is
        print('OV nummer moet 4 cijfers bevatten')
        ov = input('Geef de laatse 4 nummers van uw OV-chipkaart: ')

    infile = open('Wachtwoorden.txt', 'r')
    lines = infile.readlines()
    with open('Wachtwoorden.txt', 'a') as f:
        if len(lines) != 0:
            f.write('\n')
        f.write(ov)
        f.write(';')
        f.write(ww)
inlog_wachtwoord()