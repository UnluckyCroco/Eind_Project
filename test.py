from tkinter import *
from tkinter.messagebox import showwarning, showinfo


class Window(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.geometry("1920x1080")

        self.regibutton = Button(master=self.parent, text='Registreren', command=self.Regi,
                                 bg='lightgreen', relief=SOLID, font='Calibri',
                                 width=40)
        self.regibutton.place(relx=0.5, rely=0.5, anchor=SE)

        self.logingobutton = Button(master=self, text='Inloggen',
                               bg='lightgreen', relief=SOLID, font='Calibri',
                               width=40)
        self.logingobutton.place(relx=0.5, rely=0.5, anchor=SW)

        self.infobutton = Button(master=self, text='Informatie', command=self.zien,
                            bg='lightgreen', relief=SOLID, font='Calibri',
                            width=40)
        self.infobutton.place(relx=0.5, rely=0.5, anchor=NE)

        self.quitbutton = Button(master=self, text='Afsluiten', command=quit,
                            bg='red', relief=SOLID, font='Calibri',
                            width=40)
        self.quitbutton.place(relx=0.5, rely=0.5, anchor=NW)

    def regi(self):
        if self.telfield.get() and self.ovrfield.get() and self.vnaamfield.get() and self.anaamfield.get() and self.wwrfield.get() == '':
            return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        if self.vnaamfield.get() == '':
            return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        if self.anaamfield.get() == '':
            return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        telefoon =self.telfield.get()
        if telefoon == '':
            return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        elif telefoon.isdigit():  # TELEFOON
            digit = telefoon
        else:
            digit = ' '
        if telefoon is not digit:
            return showwarning(title='Telefoon', message='Telefoonnummer mag alleen nummers bevatten')

        if len(telefoon) is not 8:
            return showwarning(title='Telefoon', message='Telefoonnummer moet 8 nummers bevatten')

        ov = self.ovrfield.get()
        if ov == '':
            return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        elif ov.isdigit():  # OV
            nummer = ov
        else:
            nummer = ' '
        if ov is not nummer:
            return showwarning(title='OV', message='OV mag alleen nummers bevatten')

        if len(ov) is not 4:
            return showwarning(title='OV', message='Telefoonnummer moet 4 nummers bevatten')

        ww = self.wwrfield.get()
        if ww == '':
            return showwarning(title='Leeg', message='Vul alle velden in alstublieft')

        elif len(ww) < 6:
            return showwarning(title='Wachtwoord', message='Het wachtwoord moet minstens 6 karakters bevatten')
        else:
            onnodig = 'onnodig'

        ww2 = self.wwr2field.get()
        if ww2 == '':
            return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        elif self.wwrfield.get() != self.wwr2field.get():
            return showwarning(title='Wachtwoord', message='De wachtwoorden zijn niet gelijk ')
        else:
            onnodig = 'onnodig'

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
        return self.top.destroy(), self.initialize()

    def Regi(self):
        self.destroy()
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

        self.wwrfield = Entry(master=self.top)
        self.wwrfield.grid(row=4, column=21, pady=20)

        self.wwr2field = Entry(master=self.top)
        self.wwr2field.grid(row=5, column=21, pady=20)

        self.registrerenbutton = Button(self.top, text='Registreren', command=self.regi,
                                   bg='lightgreen', relief=SOLID, font='Calibri',
                                   width=40)
        self.registrerenbutton.place(relx=0.5, rely=0.5, anchor=SE)

        self.quitbutton = Button(master=self.top, text='Afsluiten', command=quit,
                                 bg='red', relief=SOLID, font='Calibri',
                                 width=40)
        self.quitbutton.place(relx=0.5, rely=0.5, anchor=SW)



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

    def zien(self):
        vrij = 'Om OV-fietsenstalling te gebruiken heeft u een geldige OV-chipkaart en telefoonnummer nodig. Er zijn geen stallingskosten, een fiets huren kost €240 per uur. Plaatsen vrij: '
        vrij2 = self.informatieIedereen()
        vrij3 = str(vrij)+ str(vrij2)
        print(vrij3)
        showinfo(title='Informatie Algemeen', message=vrij3)



if __name__ == "__main__":
    window = Window(None)

    window.title("Home")

    window.mainloop()