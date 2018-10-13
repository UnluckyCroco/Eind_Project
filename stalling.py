naam = input("Wat is uw fietsnummer(zie de sticker op uw fiets)?: ")

def fiets_stallen():
    read = open('Gegevens', 'r')
    write = open('stalling_text.txt', 'a')
    infile = read.readlines()
    outfile = write.write

    for infiles in infile:
        zin = infiles.split(';')
        info = zin[0]
        if info == naam:
            dag = input('Hoeveelste is het vandaag (dd/mm/yy)?: ')
            klok = input('Hoe laat is het (uur:minuut)?: ')
            outfile('\n' + dag + ';' + klok)
            return 'Alstublieft, u kunt uw fiets nu veilig stallen'
    return 'Dit nummer is niet geregistreerd'

print(fiets_stallen())
