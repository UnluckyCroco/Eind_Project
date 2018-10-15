import time
def huren(vnaam):
    checkhuur = 0
    file = open('Huurgegevens', 'r')
    lines = file.readlines()

    for line in lines:
        x = line.split(';')
        if checkhuur == 0:
            if vnaam in x:
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
        huurfile.write(vnaam + ';' + str(tijdH) + ';' + str(tijdM) + ';' + str(tijdS) + ';' + str(datumd) + ';' + str(datumm) + ';' + str(datumY) + '\n')
    huurfile.close()

def terugbrengen(vnaam):
    gelukt = 0
    totalY = 0
    totalm = 0
    totald = 0
    totalH = 0
    totalM = 0
    totalS = 0
    dag = 86400
    jaar = 31536000

    terugfile = open('Huurgegevens', 'r')
    linest = terugfile.readlines()

    for linet in linest:
        y = linet.split(';')

        if vnaam in y:
            datumstartH = y[1]
            datumstartM = y[2]
            datumstartS = y[3]
            datumstartd = y[4]
            datumstartm = y[5]
            datumstartY = y[6].strip('\n')

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
            # insert delete gegevens

            # writefile = open('Huurgegevens','w')
            # linesw = writefile.readlines()
            # for linew in linesw:
            #     naam = linew.split(';')
            #     if vnaam == naam[0]:
            #         writefile.writelines('end')
            #         print(naam)
            # writefile.close()

            gelukt = 1                          # voor de "geen fiets gehuurd" dinges
    if gelukt != 1:
        print('U heeft geen fiets gehuurd')
    terugfile.close()
ikik = input('?\n')
if ikik == 'H':
    vnaam = input('Naam\n')
    huren(vnaam)
else:
    vnaam = input('Naam\n')
    terugbrengen(vnaam)