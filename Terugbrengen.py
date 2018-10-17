import time


def regel_verwijderen():
    lijst = []
    file = open('Huurgegevens', 'r')
    regels = file.readlines()
    file.close()

    infile = open('Ingelogd', 'r')
    ilines = infile.readlines()
    for iline in ilines:
        inlog = iline.split(';')
        inlogz = inlog[4].strip('\n')
    infile.close()

    for regel in regels:
        x = regel.split(';')
        counter = 0
        if not inlog[0] == x[0]:
            counter += 1
        if not inlog[1] == x[1]:
            counter += 1
        if not inlogz == x[2]:
            counter += 1
        if counter > 0:
            lijst.append(regel)
    file.close()
    wfile = open('Huurgegevens','w')
    for gegevens in range(len(lijst)):
        wfile.write(lijst[gegevens])



def fiets_terugbrengen():
    gelukt = 0
    dag = 86400
    jaar = 31536000

    terugfile = open('Huurgegevens', 'r')
    linest = terugfile.readlines()

    infile = open('Ingelogd', 'r')
    ilines = infile.readlines()
    for iline in ilines:
        inlog = iline.split(';')
        inlogz = inlog[4].strip('\n')
    infile.close()

    for linet in linest:
        y = linet.split(';')

        if inlog[0] in y:
            if inlog[1] in y:
                if inlogz in y:
                    datumstartH = y[3]
                    datumstartM = y[4]
                    datumstartS = y[5]
                    datumstartd = y[6]
                    datumstartm = y[7]
                    datumstartY = y[8].strip('\n')

                    tijdHt = time.strftime('%H')  # uren;tijdsbepaling van nu
                    tijdMt = time.strftime('%M')  # minuten
                    tijdSt = time.strftime('%S')  # seconden
                    datumdt = time.strftime('%d')  # dag
                    datummt = time.strftime('%m')  # maand
                    datumYt = time.strftime('%Y')  # jaar

                    tijddatum = tijdHt + ':' + tijdMt + ':' + tijdSt + ' ' + datumdt + '/' + datummt + '/' + datumYt
                    print('U heeft de fiets gehuurd sinds','{}:{}:{} {}/{}/{}'.format(datumstartH,datumstartM,datumstartS,datumstartd,datumstartm,datumstartY),'en de fiets terug gebracht op', tijddatum)
                    total = int(datumstartH)*3600 + int(datumstartM)*60 + int(datumstartS) + int(datumstartd)*dag + int(datumstartm)/12*jaar + int(datumstartY)*jaar
                    totalt = int(tijdHt)*3600 + int(tijdMt)*60 + int(tijdSt) + int(datumdt)*dag + int(datummt)/12*jaar + int(datumYt)*jaar

                    gehuurdtijdtotal = totalt - total
                    gehuurdtijd = gehuurdtijdtotal
                    totalY = gehuurdtijd // (jaar)                       # hier en onder berekent hij per tijd hoelang de fiets gehuurd is
                    if totalY == 1:
                        jaren = 'jaar,'
                    else:
                        jaren = 'jaren,'
                    gehuurdtijd = gehuurdtijd - totalY * jaar
                    totalm = gehuurdtijd // (jaar / 12)
                    if totalm == 1:
                        maanden = 'maand,'
                    else:
                        maanden = 'maanden,'
                    gehuurdtijd = gehuurdtijd - totalm * jaar / 12
                    totald = gehuurdtijd // (dag)
                    if totald == 1:
                        dagen = 'dag,'
                    else:
                        dagen = 'dagen,'
                    gehuurdtijd = gehuurdtijd - totald * dag
                    totalH = gehuurdtijd // (3600)
                    if totalH == 1:
                        uren = 'uur,'
                    else:
                        uren = 'uren,'
                    gehuurdtijd = gehuurdtijd - totalH * 3600
                    totalM = gehuurdtijd // (60)
                    if totalM == 1:
                        minuten = 'minuut,'
                    else:
                        minuten = 'minuten,'
                    gehuurdtijd = gehuurdtijd - totalM * 60
                    totalS = gehuurdtijd
                    if totalS == 1:
                        seconden = 'seconde'
                    else:
                        seconden = 'seconden'

                    prijs = gehuurdtijdtotal//(60*15)*0.2 + 1           # elke 15 minuten + 20 cent en standaard 1 euro
                    print('U heeft de fiets voor',int(totalY),jaren,int(totalm),maanden,int(totald),dagen,int(totalH),uren,int(totalM),minuten,int(totalS),seconden,'gehuurd, dat kost u',str(prijs),'euro.')

                    regel_verwijderen()

                    gelukt = 1                          # voor de "geen fiets gehuurd" dinges
    if gelukt != 1:
        print('U heeft geen fiets gehuurd')
    terugfile.close()

fiets_terugbrengen()