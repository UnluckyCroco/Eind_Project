def fiets_registreren():
        vnaam = input('Geef uw voornaam: ')
        if vnaam == 'STOP':
            fiets_registreren()

        anaam = input('Geef uw tussenvoegsels en achternaam: ')
        if anaam == 'STOP':
            fiets_registreren()

        telefoon = input('Geef uw telefoonnummer: 06-')  #telefoon
        if telefoon.isdigit():  #checkt als telefoon wel uit nummers bestaat
            digit = telefoon
        elif telefoon == 'STOP':
            fiets_registreren()
        else:
            digit = ' '
        while telefoon is not digit:
            print('Telefoon nummer mag alleen cijfers bevatten')
            telefoon = input('Geef uw telefoonnummer: 06-')
            if telefoon.isdigit():
                digit = telefoon
            elif telefoon == 'STOP':
                fiets_registreren()
            else:
                digit = ' '

        while len(telefoon) is not 8: #checkt of het tefeloonnummer 8 tekens lang is
            print('Telefoon nummer moet 8 cijfers bevatten')
            telefoon = input('Geef uw telefoonnummer: 06-')
            if telefoon == 'STOP':
                fiets_registreren()

        ov = input('Geef de laatste 4 nummers van uw ov-chipkaar: ') #OV-chipkaart
        if ov.isdigit():  #checkt als ov wel uit nummers bestaat
            nummer = ov
        elif ov == 'STOP':
            fiets_registreren()
        else:
            nummer = ' '
        while ov is not nummer:
            print('OV nummer mag alleen cijfers bevatten')
            ov = input('Geef de laatste 4 nummers van uw OV-chipkaart: ')
            if ov.isdigit():
                nummer = ov
            elif ov == 'STOP':
                fiets_registreren()
            else:
                nummer = ' '

        while len(ov) is not 4: #checkt of het ov 4 tekens lang is
            print('OV nummer moet 4 cijfers bevatten')
            ov = input('Geef de laatse 4 nummers van uw OV-chipkaart: ')
            if ov == 'STOP':
                fiets_registreren()

        ww = input('Geef een wachtwoord (minimaal 6 karakters): ')
        if ww == 'STOP':
            fiets_registreren()

        while len(ww) < 6:
            print('Het nieuwe wachtwoord moet minstens 6 karakters zijn')
            ww = input('Geef een wachtwoord (minimaal 6 karakters): ')
            if ww == 'STOP':
                fiets_registreren()

        with open('Gegevens', 'a') as f:

                 f.write(vnaam)
                 f.write(';')
                 f.write(anaam)
                 f.write(';')
                 f.write(ww)               # ik heb ww hier moeten verplaatsen zodat mijn code kan functioneren.
                 f.write(';')
                 f.write(telefoon)
                 f.write(';')
                 f.write(ov)
                 f.write(';')
                 f.write('\n')
        return 'Uw gegevens zijn geregistreerd'


print(fiets_registreren())

from NS_Fietsen_Stalling import inlog_menu
print(inlog_menu())