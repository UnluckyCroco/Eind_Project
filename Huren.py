import time
def fiets_huren():
    infile = open('Ingelogd','r')
    ilines = infile.readlines()
    for iline in ilines:
        inlog = iline.split(';')
    checkhuur = 0

    file = open('Huurgegevens', 'r')
    lines = file.readlines()
    file.close()

    for line in lines:                                  # checked of dezelfde gegevens in 'Ingelogd' ook staan in 'Huurgegevens', zoja, dan betekend het dat er al een fiets is gehuurd
        x = line.split(';')
        if checkhuur == 0 and inlog[0] == x[0] and inlog[1] == x[1] and inlog[4].strip('\n') == x[2]:
            print('U heeft al een fiets gehuurd')
            checkhuur = 1
    if checkhuur == 0:
        tijdH = time.strftime('%H')  # uren
        tijdM = time.strftime('%M')  # minuten
        tijdS = time.strftime('%S')  # seconden
        datumd = time.strftime('%d')  # dag
        datumm = time.strftime('%m')  # maand
        datumY = time.strftime('%Y')  # jaar
        tijddatum = tijdH + ':' + tijdM + ':' + tijdS + ' ' + datumd + '/' + datumm + '/' + datumY
        print('De fiets is gehuurd vanaf', tijddatum)
        huurfile = open('Huurgegevens', 'a')
        huurfile.write(inlog[0] + ';' + inlog[1] + ';' + inlog[4].strip('\n') + ';' + str(tijdH) + ';' + str(tijdM) + ';' + str(tijdS) + ';' + str(datumd) + ';' + str(datumm) + ';' + str(datumY) + '\n')
        huurfile.close()


fiets_huren()