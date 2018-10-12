def nieuw_wachtwoord():
    ww = input('Wat moet het nieuwe wachtwoord zijn?: ')
    if len(ww) < 6:
        print('Het nieuwe wachtwoord moet minstens 6 karakters zijn!')
    else:
        infile = open('wachtwoorden', 'r')
        write = infile.readlines()

        print('Het wachtwoord is veranderd.')
nieuw_wachtwoord()