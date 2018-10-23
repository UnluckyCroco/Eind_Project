from tkinter import *
from tkinter.messagebox import showwarning, showinfo
import time
import random
from time import*


class Window(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def exit(self):
        self.top.withdraw()
        if __name__ == "__main__":
            window = Window(None)
            window.geometry('1920x1080')
            window.title('Home')
            window.mainloop()

    def initialize(self):
        self.regibutton = Button(master=self, text='Registreren', command=self.Regi,
                                 bg='lightgreen', relief=SOLID, font='Calibri',
                                 width=40)
        self.regibutton.place(relx=0.5, rely=0.5, anchor=SE)

        self.logingobutton = Button(master=self, text='Inloggen', command=self.inloggen,
                               bg='lightgreen', relief=SOLID, font='Calibri',
                               width=40)
        self.logingobutton.place(relx=0.5, rely=0.5, anchor=SW)

        self.infobutton = Button(master=self, text='Informatie', command=self.infoalgemeen,
                            bg='lightgreen', relief=SOLID, font='Calibri',
                            width=40)
        self.infobutton.place(relx=0.5, rely=0.5, anchor=NE)

        self.quitbutton = Button(master=self, text='Afsluiten', command=quit,
                            bg='red', relief=SOLID, font='Calibri',
                            width=40)
        self.quitbutton.place(relx=0.5, rely=0.5, anchor=NW)

    def regi(self):
        if self.telfield.get() == '':
            return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        if self.ovrfield.get() == '':
            return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        if self.vnaamfield.get() == '':
            return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        if self.anaamfield.get()  == '':
            return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        if self.wwrfield.get() == '':
            return showwarning(title='Leeg', message='Vul alle velden in alstublieft')

        telefoon =self.telfield.get()
        if telefoon.isdigit():  # TELEFOON
            digit = telefoon
        else:
            digit = ' '
        if telefoon is not digit:
            return showwarning(title='Telefoon', message='Telefoonnummer mag alleen nummers bevatten')

        if len(telefoon) is not 8:
            return showwarning(title='Telefoon', message='Telefoonnummer moet 8 nummers bevatten')

        ov = self.ovrfield.get()
        if ov.isdigit():  # OV
            nummer = ov
        else:
            nummer = ' '
        if ov is not nummer:
            return showwarning(title='OV', message='OV mag alleen nummers bevatten')

        if len(ov) is not 4:
            return showwarning(title='OV', message='Telefoonnummer moet 4 nummers bevatten')

        ww = self.wwrfield.get()
        if len(ww) < 6:
            return showwarning(title='Wachtwoord', message='Het wachtwoord moet minstens 6 karakters bevatten')

        if self.wwrfield.get() != self.wwr2field.get():
            return showwarning(title='Wachtwoord', message='De wachtwoorden zijn niet gelijk ')

        with open('Gegevens', 'a') as f:

            f.write(self.vnaamfield.get())
            f.write(';')
            f.write(self.anaamfield.get())
            f.write(';')
            f.write(self.wwrfield.get())
            f.write(';')
            f.write(self.telfield.get())
            f.write(';')
            f.write(self.ovrfield.get())
            f.write(';')
            f.write('\n')
            f.close()
        return self.exit()

    def Regi(self):
        self.withdraw()
        self.top = Toplevel()
        self.top.title("Registreren")
        self.top.geometry("1920x1080")

        self.label = Label(self.top, text='Voornaam')
        self.label.grid(row=0, column=20, ipadx=170, sticky=W)
        self.label.config(font=("Calibri", 16))

        self.label = Label(self.top, text='Achternaam')
        self.label.grid(row=1, column=20, ipadx=170, sticky=W)
        self.label.config(font=("Calibri", 16))

        self.label = Label(self.top, text='Telefoonnummer(06-)')
        self.label.grid(row=2, column=20, ipadx=170, sticky=W)
        self.label.config(font=("Calibri", 16))

        self.label = Label(self.top, text='Laatste 4 cijfers van uw OV')
        self.label.grid(row=3, column=20, ipadx=170, sticky=W)
        self.label.config(font=("Calibri", 16))

        self.label = Label(self.top, text='Wachtwoord (minimaal 6 karakters)')
        self.label.grid(row=4, column=20, ipadx=170, sticky=W)
        self.label.config(font=("Calibri", 16))
        self.label = Label(self.top, text='Wachtwoord opnieuw')
        self.label.grid(row=5, column=20, ipadx=170, sticky=W)
        self.label.config(font=("Calibri", 16))

        self.vnaamfield = Entry(master=self.top)
        self.vnaamfield.grid(row=0, column=21, pady=20)

        self.anaamfield = Entry(master=self.top)
        self.anaamfield.grid(row=1, column=21, pady=20)

        self.telfield = Entry(master=self.top)
        self.telfield.grid(row=2, column=21, pady=20)

        self.ovrfield = Entry(master=self.top)
        self.ovrfield.grid(row=3, column=21, pady=20)

        self.wwrfield = Entry(master=self.top, show='*')
        self.wwrfield.grid(row=4, column=21, pady=20)

        self.wwr2field = Entry(master=self.top, show='*')
        self.wwr2field.grid(row=5, column=21, pady=20)

        self.registrerenbutton = Button(self.top, text='Registreren', command=self.regi,
                                   bg='lightgreen', relief=SOLID, font='Calibri',
                                   width=40)
        self.registrerenbutton.grid(row=6, column=20, sticky=E)

        self.terugbutton = Button(self.top, text='Terug', command=self.exit,
                                   bg='lightgreen', relief=SOLID, font='Calibri',
                                   width=40)
        self.terugbutton.grid(row=6, column=21, sticky=E)

        self.quitbutton = Button(master=self.top, text='Afsluiten', command=quit,
                                 bg='red', relief=SOLID, font='Calibri',
                                 width=40)
        self.quitbutton.grid(row=6, column=22)


    def informatieIedereen(self):
        bezet = 0
        regel = open('Stallen.txt', 'r')
        for line in regel.readlines():
            bezet += 1
        regel.close()
        if bezet < 701:
            vrij = 701 - bezet

        else:
            vrij = 0
        return vrij

    def infoalgemeen(self):
        vrij = 'Om OV-fietsenstalling te gebruiken heeft u een geldige OV-chipkaart en telefoonnummer nodig. Er zijn geen stallingskosten, een fiets huren kost €0.80 per uur. Plaatsen vrij: '
        vrij2 = self.informatieIedereen()
        vrij3 = str(vrij)+ str(vrij2)
        showinfo(title='Informatie Algemeen', message=vrij3)

    def clicked(self):
        bericht = 'De ingevulde gegevens kloppen niet'
        showwarning(title='popup', message=bericht)

    def login(self):
        if self.naamfield.get() == '':
           return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        if self.ovfield.get() == '':
           return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        if self.wwfield.get() == '':
           return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        file = open('Gegevens', 'r')
        lines = file.readlines()
        for line in lines:
            y = line.strip('\n')
            z = y.split(';')
            if self.naamfield.get() == z[0]:
                if self.ovfield.get() == z[4]:
                    if self.wwfield.get() == z[2]:
                        file.close()
                        f1 = open('Ingelogd', 'w')
                        f1.write(line)
                        f1.close()
                        return self.menu2()
        self.clicked()

    def inloggen(self):
        self.withdraw()
        self.top = Toplevel()
        self.top.title("Inloggen")
        self.top.geometry("1920x1080")

        self.label = Label(self.top, text='Voornaam')
        self.label.grid(row=0, column=20, ipadx=170, sticky=W)
        self.label.config(font=("Calibri", 16))

        self.label = Label(self.top, text='Wachtwoord')
        self.label.grid(row=1, column=20, ipadx=170, sticky=W)
        self.label.config(font=("Calibri", 16))

        self.label = Label(self.top, text='Laatste 4 nummers van uw OV')
        self.label.grid(row=2, column=20, ipadx=170, sticky=W)
        self.label.config(font=("Calibri", 16))

        self.naamfield = Entry(master=self.top)
        self.naamfield.grid(row=0, column=21, pady=20)

        self.wwfield = Entry(master=self.top, show='*')
        self.wwfield.grid(row=1, column=21, pady=20)

        self.ovfield = Entry(master=self.top)
        self.ovfield.grid(row=2, column=21, pady=20)

        self.loginbutton = Button(master=self.top, text='Inloggen', command=self.login,
                                  bg='lightgreen', relief=SOLID, font='Calibri',
                                  width=40)
        self.loginbutton.grid(row=6, column=20, sticky=E)

        self.terugbutton = Button(self.top, text='Terug', command=self.exit,
                                  bg='lightgreen', relief=SOLID, font='Calibri',
                                  width=40)
        self.terugbutton.grid(row=6, column=21, sticky=E)

        self.quitbutton = Button(master=self.top, text='Afsluiten', command=quit,
                                 bg='red', relief=SOLID, font='Calibri',
                                 width=30)
        self.quitbutton.grid(row=6, column=22, sticky=E)

    def menu2(self):
        self.top.withdraw()
        self.top = Toplevel()
        self.top.title("Inloggen")
        self.top.geometry("1920x1080")

        self.stallenbutton = Button(master=self.top, text='Fiets Stallen', command=self.fiets_stallen,
                                    bg='lightgreen', relief=SOLID, font='Calibri',
                                    width=40)
        self.stallenbutton.place(relx=0.34, rely=0.5, anchor=SE)

        self.ophalenbutton = Button(master=self.top, text='Fiets Ophalen', command=self.login,
                                    bg='lightgreen', relief=SOLID, font='Calibri',
                                    width=40)
        self.ophalenbutton.place(relx=0.34, rely=0.5, anchor=SW)

        self.hurenbutton = Button(master=self.top, text='Fiets Huren', command=self.login,
                                  bg='lightgreen', relief=SOLID, font='Calibri',
                                  width=40)
        self.hurenbutton.place(relx=0.6, rely=0.5, anchor=SW)

        self.terugbrengenbutton = Button(master=self.top, text='Huurfiets Terugbrengen', command=self.login,
                                         bg='lightgreen', relief=SOLID, font='Calibri',
                                         width=40)
        self.terugbrengenbutton.place(relx=0.34, rely=0.5, anchor=NE)

        self.informatiebutton = Button(master=self.top, text='Informatie', command=self.InfoEigenaar,
                                       bg='lightgreen', relief=SOLID, font='Calibri',
                                       width=40)
        self.informatiebutton.place(relx=0.34, rely=0.5, anchor=NW)

        self.hulpqrbutton = Button(master=self.top, text='Hulp QR', command=self.QRHulpPopup,
                                       bg='lightgreen', relief=SOLID, font='Calibri',
                                       width=40)
        self.hulpqrbutton.place(relx=0.47, rely=0.6, anchor=S)

        self.uitloggenbutton = Button(self.top, text='Uitloggen', command=self.exit,
                                      bg='red', relief=SOLID, font='Calibri',
                                      width=40)
        self.uitloggenbutton.place(relx=0.6, rely=0.5, anchor=NW)

    def times(self):
        ''
        localtime(time())
        ''
        return (asctime(localtime(time())))


    def toonStallen(self):
        stallenbericht = 'U kunt u fiets veilig stallen op plek: ' + str(self.rnummer)
        showinfo(title='Stallen', message=stallenbericht)

    def warning(self):
        stallenbericht = 'U heeft u fiets al veilig gestald op plek: ' + str(self.rnummer)
        showinfo(title='Stallen', message=stallenbericht)

    def fiets_stallen(self):
        read = open('Ingelogd', 'r')
        read1 = open('Stallen.txt', 'r')
        write = open('Stallen.txt', 'a')
        infile = read.readlines()
        infile1 = read1.readlines()
        outfile = write.write

        for infiles1 in infile1:
            zin1 = infiles1.split(';')
            self.info1 = zin1[1]

            for infiles in infile:
                zin = infiles.split(';')
                self.info = zin[4]

                if self.info == self.info1:
                    return self.warning()

                for x in range(1):
                    self.rnummer = random.randint(1, 701)
                    infile = open('Stallen.txt', 'r')
                    regels = infile.readlines()
                    for regel in regels:
                        zin = regel.split(';')
                        nummer = zin[2]
                        ov = zin[1]
                        if nummer == self.rnummer:
                            self.fiets_stallen()
                        if ov == self.info:
                            self.warning()
                    self.stallen = (str(self.times()) + '; ' + self.info + '; ' + str(self.rnummer) + '\n')
                    outfile(self.stallen)
        return self.toonStallen()

    def regel_verwijderen(self):
        lijst = []
        file = open('Huurgegevens', 'r')
        regels = file.readlines()
        file.close()

        infile = open('Ingelogd', 'r')
        ilines = infile.readlines()
        for iline in ilines:
            inlog = iline.split(';')
        infile.close()

        for regel in regels:  # voegt elke regel toe die niet gelijk is aan de teruggebrachde fiets aan een lijst, die hij later terug het bestand in zet
            x = regel.split(';')
            counter = 0
            if inlog[0] == x[0] and inlog[1] == x[1] and inlog[4].strip('\n') == x[2]:
                counter += 1
            if counter == 0:
                lijst.append(regel)
        file.close()
        wfile = open('Huurgegevens', 'w')
        for gegevens in range(len(lijst)):
            wfile.write(lijst[gegevens])

    def fiets_terugbrengen(self):
        gelukt = 0
        dag = 86400  # in seconden
        jaar = 31536000

        terugfile = open('Huurgegevens', 'r')
        linest = terugfile.readlines()
        terugfile.close()

        infile = open('Ingelogd', 'r')
        ilines = infile.readlines()
        for iline in ilines:
            inlog = iline.split(';')
        infile.close()

        for linet in linest:
            y = linet.split(';')

            if inlog[0] == y[0] and inlog[1] == y[1] and inlog[4].strip('\n') == y[2]:
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

                print('U heeft de fiets gehuurd sinds',
                      '{}:{}:{} {}/{}/{}'.format(datumstartH, datumstartM, datumstartS, datumstartd, datumstartm,
                                                 datumstartY), 'en de fiets terug gebracht op', tijddatum)
                total = int(datumstartH) * 3600 + int(datumstartM) * 60 + int(datumstartS) + int(
                    datumstartd) * dag + int(datumstartm) / 12 * jaar + int(datumstartY) * jaar
                totalt = int(tijdHt) * 3600 + int(tijdMt) * 60 + int(tijdSt) + int(datumdt) * dag + int(
                    datummt) / 12 * jaar + int(datumYt) * jaar

                gehuurdtijdtotal = totalt - total
                gehuurdtijd = gehuurdtijdtotal
                totalY = gehuurdtijd // (jaar)  # hier en onder berekent hij per tijd hoelang de fiets gehuurd is
                if totalY == 1:
                    jaren = 'jaar'
                else:
                    jaren = 'jaren'
                gehuurdtijd = gehuurdtijd - totalY * jaar
                totalm = gehuurdtijd // (jaar / 12)
                if totalm == 1:
                    maanden = 'maand'
                else:
                    maanden = 'maanden'
                gehuurdtijd = gehuurdtijd - totalm * jaar / 12
                totald = gehuurdtijd // (dag)
                if totald == 1:
                    dagen = 'dag'
                else:
                    dagen = 'dagen'
                gehuurdtijd = gehuurdtijd - totald * dag
                totalH = gehuurdtijd // (3600)
                if totalH == 1:
                    uren = 'uur'
                else:
                    uren = 'uren'
                gehuurdtijd = gehuurdtijd - totalH * 3600
                totalM = gehuurdtijd // (60)
                if totalM == 1:
                    minuten = 'minuut'
                else:
                    minuten = 'minuten'
                gehuurdtijd = gehuurdtijd - totalM * 60
                totalS = gehuurdtijd
                if totalS == 1:
                    seconden = 'seconde'
                else:
                    seconden = 'seconden'

                prijs = gehuurdtijdtotal // (60 * 15) * 0.2 + 1  # elke 15 minuten + 20 cent en standaard 1 euro

                regel_verwijderen()

                # return 'U heeft de fiets voor', int(totalY), jaren, int(totalm), maanden, int(totald), dagen, int(totalH), uren, int(totalM), minuten, int(totalS), seconden, 'gehuurd, dat kost u', str(prijs), 'euro.'
                return 'U heeft de fiets voor {} {}, {} {}, {} {}, {} {}, {} {} en {} {} gehuurd, dat kost u {} euro'.format(
                    int(totalY), jaren, int(totalm), maanden, int(totald), dagen, int(totalH), uren, int(totalM),
                    minuten, int(totalS), seconden, str(prijs))

        if gelukt != 1:
            return 'U heeft geen fiets gehuurd'

    def infopopup(self):
        self.infotext = (
                    'Geregistreerde naam: ' + self.naam + self.achternaam + '\n' + 'Geregisteerd wachtwoord: ' + self.ww + '\n' + 'Geregisteerd telefoon nummer: ' + self.tel + '\n' + 'Geregisteerde OV:' + self.ov)
        showinfo(title='Stallen', message=self.infotext)

    def InfoEigenaar(self):
            gegevens = open('Ingelogd', 'r')
            gegeven = gegevens.readlines()
            for item in gegeven:
                regel = item.split(';')
                self.naam = regel[0]
                self.achternaam = regel[1]
                self.ww = regel[2]
                self.tel = regel[3]
                self.ov = regel[4]
                self.infopopup()

    def QRHulpPopup(self):
        self.infotext = (
                    'Om een QR te scannen moet u een QR of Barcode scanner downloaden op uw smartphone. Na het scannen krijgt u de code te zien, bewaar deze om later je fiets weer op te kunnen halen.')
        showinfo(title='Hulp QR', message=self.infotext)

if __name__ == "__main__":
    window = Window(None)
    window.geometry('1920x1080')
    window.title('Home')
    window.mainloop()

