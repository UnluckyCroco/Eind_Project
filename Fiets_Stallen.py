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
        info = zin[0]
        if info == naam:

            outfile('\n'+ naam + '; ' + str(times())+ ';' + str(times()))
            return 'Alstublieft, u kunt uw fiets nu veilig stallen'
    return 'Dit nummer is niet geregistreerd'

print(fiets_stallen())

