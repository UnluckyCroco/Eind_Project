import random
def fiets_registreren():
    vnaam = input('Geef uw voornaam: ')
    anaam = input('Geef uw tussenvoegsels en achternaam: ')

    telefoon = input('Geef uw telefoonnummer: 06-')  #telefoon
    if telefoon.isdigit():  #checkt als telefoon wel uit nummers bestaat
        digit = telefoon
    else:
        digit = 'niks'
    while telefoon is not digit:
        print('Telefoon nummer mag alleen cijfers bevatten')
        telefoon = input('Geef uw telefoonnummer: 06-')
        if telefoon.isdigit():
            digit = telefoon
        else:
            digit = 'niks'

    while len(telefoon) is not 8: #checkt of het tefeloonnummer 8 tekens lang is
        print('Telefoon nummer moet 8 cijfers bevatten')
        telefoon = input('Geef uw telefoonnummer: 06-')

    ov = input('Geef de laatste 4 nummers van uw ov-chipkaar: ') #OV-chipkaart
    if ov.isdigit():  #checkt als ov wel uit nummers bestaat
        nummer = ov
    else:
        nummer = 'niks'
    while ov is not nummer:
        print('OV nummer mag alleen cijfers bevatten')
        telefoon = input('Geef de laatste 4 nummers van uw OV-chipkaart: ')
        if ov.isdigit():
            nummer = ov
        else:
            nummer = 'nikskhk'

    while len(ov) is not 4: #checkt of het ov 4 tekens lang is
        print('OV nummer moet 4 cijfers bevatten')
        telefoon = input('Geef de laatse 4 nummers van uw OV-chipkaart: ')

    for x in range(1):
         rnummer = random.randint(1,701)  #maakt een random nummer aan
         infile = open('Gegevens', 'r')
         regels = infile.readlines()
         for regel in regels:
          zin = regel.split(';')
          nummer = zin[0]
          if rnummer == nummer :  #checkt als het random nummer niet al bezet is
            Random = True
          else:
            Random = False
          while Random:
            fiets_registreren()
          with open('Gegevens', 'a') as f:
             f.write('\n')
             f.write(str(rnummer))
             f.write(';')
             f.write(vnaam)
             f.write(';')
             f.write(anaam)
             f.write(';')
             f.write(telefoon)
         return rnummer



print('Uw nummer is:', fiets_registreren())


#def fiets_stallen():

#def fiets_ophalen():

#def informatie():