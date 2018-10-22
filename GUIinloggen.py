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

def toonLoginFrame():, vrij3
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

root = Tk()
root.geometry('1920x1080')

#code hoe loginscherm eruit ziet
naamframe = Frame(master=root)
naamframe.pack(fill="both", expand=True)
naamfield = Entry(master=naamframe)
naamfield.pack(padx=20, pady=20, ipadx=100, ipady=10)

wwfield = Entry(master=naamframe)
wwfield.pack(padx=20, pady=20, ipadx=100, ipady=10)

ovfield = Entry(master=naamframe)
ovfield.pack(padx=20, pady=20, ipadx=100, ipady=10)

loginbutton = Button(master=naamframe, text='Inloggen', command=login,
                     bg='lightgreen', relief=SOLID, font='Calibri',
                     width=40)
loginbutton.place(relx=0.5, rely=0.5, anchor=SE)

quitbutton = Button(master=naamframe, text='Afsluiten', command=quit,
                    bg='red', relief=SOLID, font='Calibri',
                    width=30)
quitbutton.place(relx=0.5, rely=0.5, anchor=SW)

#code hoe Menu2 eruit ziet
menu2 = Frame(master=root)
menu2.pack(fill="both", expand=True)
backbutton = Button(master=menu2, text='<', command=toonLoginFrame)
backbutton.pack(pady=20)

toonHoofdmenu()
