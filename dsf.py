from tkinter import *
#from GUIinloggen import toonHoofdmenu

#class Display:

def informatieIedereen():
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

def zien():
    root = Tk()
    root.geometry('1920x1080')
    vrij = informatieIedereen()
    infomenu = Frame(master=root, bg='blue')
    infomenu.pack(fill="both", expand=True)
    label_zin = Label(infomenu, text='Om OV-fietsenstalling te gebruiken heeft u een geldige OV-chipkaart\n '
                                     'en telefoonnummer nodig. Er zijn geen stallingskosten, een fiets huren\n'
                                     'kost €240 per uur. Plaatsen vrij: ', bg='blue', anchor=SE)
    label_vrij = Label(infomenu, text=informatieIedereen(), bg='blue')
    label_zin.pack()
    label_vrij.pack()
    quitbutton = Button(master=infomenu, text='Afsluiten', command=quit,
                            bg='red', relief=SOLID, font='Calibri',
                            width=30)
    quitbutton.place(relx=0.5, rely=0.5, anchor=SW)

    terugbutton = Button(master=infomenu, text='Terug', command=print('yes'),
                             bg='lightgreen', relief=SOLID, font='Calibri',
                            width=30)
    terugbutton.place(relx=0.5, rely=0.5, anchor=SE)
    root.mainloop()

zien()



