import random
from time import*


def times():
    ''
    localtime(time())
    ''
    return(asctime(localtime(time())))

naam = input("Wat zijn de laatste 4 cijfers van uw OV kaart?: ")

def fiets_stallen():
    read = open('Gegevens', 'r')
    write = open('Stallen.txt', 'a')
    infile = read.readlines()
    outfile = write.write

    for infiles in infile:
        zin = infiles.split(';')
        info = zin[4]
        if info == naam:


            for x in range(1):
                rnummer = random.randint(1,701)  #maakt een random nummer aan
                infile = open('Stallen.txt', 'r')
                regels = infile.readlines()
                for regel in regels:
                    zin = regel.split(';')
                    nummer = zin[0]
                    if nummer == nummer :  #checkt als het random nummer niet al bezet is
                     Random = True
                    else:
                     Random = False
                    if Random:
                     fiets_stallen()
            outfile('\n' + naam + '; ' + str(times()) + '; ' + str(nummer))

            return 'Alstublieft, u kunt uw fiets nu veilig stallen'
    return 'Dit nummer is niet geregistreerd'