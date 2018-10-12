def nieuw_wachtwoord():
    ov_nummer = input('Wat zijn de laatste 4 cijfers van uw ov kaart?: ')
    ww = input('Wat moet het nieuwe wachtwoord zijn?: ')
    if len(ww) < 6:
        print('Het nieuwe wachtwoord moet minstens 6 karakters zijn!')
    else:
        infile = open('Wachtwoorden', 'r')
        write = infile.readlines()

        print('Het wachtwoord is veranderd.')
nieuw_wachtwoord()