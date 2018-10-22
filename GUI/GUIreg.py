from tkinter import *
from tkinter.messagebox import showwarning


def regi():
        if telfield.get() and ovrfield.get() and vnaamfield.get() and anaamfield.get() and wwrfield.get() == '':
            return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        if vnaamfield.get() == '':
            return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        if anaamfield.get() == '':
            return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        telefoon = telfield.get()
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

        ov = ovrfield.get()
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

        ww = wwrfield.get()
        if ww == '':
            return showwarning(title='Leeg', message='Vul alle velden in alstublieft')

        elif len(ww) < 6:
             return showwarning(title='Wachtwoord', message='Het wachtwoord moet minstens 6 karakters bevatten')
        else:
            onnodig = 'onnodig'

        ww2 = wwr2field.get()
        if ww2 == '':
            return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        elif wwrfield.get() != wwr2field.get():
            return showwarning(title='Wachtwoord', message='De wachtwoorden zijn niet gelijk ')
        else:
            onnodig = 'onnodig'

        with open('Gegevens', 'a') as f:

            f.write(vnaamfield.get())
            f.write(';')
            f.write(anaamfield.get())
            f.write(';')
            f.write(wwrfield.get())
            f.write(';')
            f.write(telfield.get())
            f.write(';')
            f.write(ovrfield.get())
            f.write(';')
            f.write('\n')

root = Tk()
root.geometry('1920x1080')
reg = Frame(master=root)
reg.pack(fill='both', expand=True)

label = Label(reg, text='Voornaam')
label.grid(row=0, column=20, ipadx=170, sticky=W)
label.config(font=("Calibri", 16))

label = Label(reg, text='Achternaam')
label.grid(row=1, column=20, ipadx=170, sticky=W)
label.config(font=("Calibri", 16))

label = Label(reg, text='Telefoonnummer(06-)')
label.grid(row=2, column=20, ipadx=170, sticky=W)
label.config(font=("Calibri", 16))

label = Label(reg, text='Laatste 4 cijfers van uw OV')
label.grid(row=3, column=20, ipadx=170, sticky=W)
label.config(font=("Calibri", 16))

label = Label(reg, text='Wachtwoord (minimaal 6 karakters)')
label.grid(row=4, column=20, ipadx=170, sticky=W)
label.config(font=("Calibri", 16))
label = Label(reg, text='Wachtwoord opnieuw')
label.grid(row=5, column=20, ipadx=170, sticky=W)
label.config(font=("Calibri", 16))

vnaamfield = Entry(master=reg)
vnaamfield.grid(row=0, column=21, pady=20)

anaamfield = Entry(master=reg)
anaamfield.grid(row=1, column=21, pady=20)

telfield = Entry(master=reg)
telfield.grid(row=2, column=21, pady=20)

ovrfield = Entry(master=reg)
ovrfield.grid(row=3, column=21, pady=20)

wwrfield = Entry(master=reg)
wwrfield.grid(row=4, column=21, pady=20)

wwr2field = Entry(master=reg)
wwr2field.grid(row=5, column=21, pady=20)

registrerenbutton = Button(reg, text='Registreren', command=regi,
                                  bg='lightgreen', relief=SOLID, font='Calibri',
                                  width=40)
registrerenbutton.place(relx=0.5, rely=0.5, anchor=SE)

quitbutton = Button(master=reg, text='Afsluiten', command=quit,
                        bg='red', relief=SOLID, font='Calibri',
                        width=30)
quitbutton.place(relx=0.5, rely=0.5, anchor=SW)
root.mainloop()
