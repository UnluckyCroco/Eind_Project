from tkinter import *
from tkinter.messagebox import showwarning

def toonHoofdmenu():
    reg.pack_forget()
    naamframe.pack_forget()
    infomenu.pack_forget()
    menu2.pack_forget()
    hoofdmenu.pack()

def toonReg():
    hoofdmenu.pack_forget()
    reg.pack()


def toonLogin1():
    hoofdmenu.pack_forget()
    naamframe.pack()

def toonLoginFrame():
    menu2.pack_forget()
    naamframe.pack()

def toonMenu2():
    naamframe.pack_forget()
    menu2.pack()

def toonInfoIedereen():
    hoofdmenu.pack_forget()
    infomenu.pack()

def clicked():
    bericht = 'De ingevulde gegevens kloppen niet'
    showwarning(title='popup', message=bericht)

def fiets_registreren():
        if telfield.get().isdigit():  #TELEFOON
            digit = telfield.get()
        else:
            digit = ' '
        if telfield.get() is not digit:
            showwarning(title='Telefoon', message='Telefoonnummer mag alleen nummers bevatten')

        if len(telfield.get()) is not 8:
            showwarning(title='Telefoon', message='Telefoonnummer moet 8 nummers bevatten')

        if ovrfield.get().isdigit():  #OV
            nummer = ovrfield.get()
        else:
            nummer = ' '
        if ovrfield.get() is not nummer:
            showwarning(title='OV', message='OV mag alleen nummers bevatten')

        if len(ovrfield.get()) is not 4:
            showwarning(title='OV', message='Telefoonnummer moet 4 nummers bevatten')

        if len(wwrfield.get()) < 6:
            showwarning(title='Wachtwoord', message='Het wachtwoord moet minstens 4 karakters bevatten')

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
        return toonHoofdmenu()


def login():
    file = open('Gegevens', 'r')
    lines = file.readlines()
    for line in lines:
        y = line.strip('\n')
        z = y.split(';')
        if naamfield.get() == z[0]:
            if ovfield.get() == z[4]:
                if wwfield.get() == z[2]:
                    file.close()
                    f1 = open('Ingelogd', 'a')
                    f1.write(line)
                    f1.close()
                    return toonMenu2()
    clicked()

def informatieIedereen():
    bezet = 0
    regel = open('Stallen.txt', 'r')
    for line in regel.readlines():
       bezet += 1
    regel.close()
    if bezet < 701:
       zin = 'Er zijn', bezet, 'plaatsen vrij.'
    else:
       zin = 'Er zijn geen plaatsen meer vrij, excuzes voor het ongemak.'
    return zin



root = Tk()
root.geometry('1920x1080')

#code hoe hoofdmenu eruit ziet
hoofdmenu = Frame(master=root)
hoofdmenu.pack(fill='both', expand=True)

logingobutton = Button(master=hoofdmenu, text='Inloggen', command=toonLogin1,
                   bg='lightgreen', relief=SOLID, font='Calibri',
                   width=40)
logingobutton.place(relx=0.5, rely=0.5, anchor=SW)

infobutton = Button(master=hoofdmenu, text='Informatie', command=toonInfoIedereen,
                   bg='lightgreen', relief=SOLID, font='Calibri',
                   width=40)
infobutton.place(relx=0.5, rely=0.5, anchor=NE)

quitbutton = Button(master=hoofdmenu, text='Afsluiten', command=quit,
                    bg='red', relief=SOLID, font='Calibri',
                    width=40)
quitbutton.place(relx=0.5, rely=0.5, anchor=NW)

#code hoe registreren eruit ziet
reg = Frame(master=root)
reg.pack(fill='both', expand=True)

vnaamfield = Entry(master=reg)
vnaamfield.pack(padx=20, pady=20)

anaamfield = Entry(master=reg)
anaamfield.pack(padx=20, pady=20)

telfield = Entry(master=reg)
telfield.pack(padx=20, pady=20)

ovrfield = Entry(master=reg)
ovrfield.pack(padx=20, pady=20)

wwrfield = Entry(master=reg)
wwrfield.pack(padx=20, pady=20)

registrerenbutton = Button(master=reg, text='Registreren', command=print('ja'),
                     bg='lightgreen', relief=SOLID, font='Calibri',
                     width=40)
registrerenbutton.place(relx=0.5, rely=0.5, anchor=SE)

quitbutton = Button(master=reg, text='Afsluiten', command=quit,
                    bg='red', relief=SOLID, font='Calibri',
                    width=30)
quitbutton.place(relx=0.5, rely=0.5, anchor=SW)


#code hoe loginscherm eruit ziet
naamframe = Frame(master=root)
naamframe.pack(fill="both", expand=True)
naamfield = Entry(master=naamframe)
naamfield.pack(padx=20, pady=20)

wwfield = Entry(master=naamframe)
wwfield.pack(padx=20, pady=20)

ovfield = Entry(master=naamframe)
ovfield.pack(padx=20, pady=20)

loginbutton = Button(master=naamframe, text='Inloggen', command=login,
                     bg='lightgreen', relief=SOLID, font='Calibri',
                     width=40)
loginbutton.place(relx=0.5, rely=0.5, anchor=SE)

quitbutton = Button(master=naamframe, text='Afsluiten', command=quit,
                    bg='red', relief=SOLID, font='Calibri',
                    width=30)
quitbutton.place(relx=0.5, rely=0.5, anchor=SW)

#code hoe informatie menu eruit ziet
infomenu = Frame(master=root, bg = 'blue')
infomenu.pack(fill="both", expand=True)
helezin = 'Om OV-fietsenstalling te gebruiken heeft u een geldige OV-chipkaart en telefoonnummer nodig. Er zijn geen stallingskosten, een fiets huren kost €240 per uur.', informatieIedereen(),' Fijne dag veder.'
label_naam = Label(infomenu, text=helezin)
quitbutton = Button(master=infomenu, text='Afsluiten', command=quit,
                    bg='red', relief=SOLID, font='Calibri',
                    width=30)
quitbutton.place(relx=0.5, rely=0.5, anchor=SW)



#code hoe Menu2 eruit ziet
menu2 = Frame(master=root)
menu2.pack(fill="both", expand=True)
backbutton = Button(master=menu2, text='<', command=toonLoginFrame)
backbutton.pack(pady=20)

toonHoofdmenu()
#root.option_add('*font', ('Calibri', 30, 'bold'))
#root.title('Login')
root.mainloop()