from tkinter import *

#class Hoofdmenu:
    #def __init__(self, Hoofdmenu):
root = Tk()
root.geometry("1920x1080")
C = Canvas(root, bg='yellow', height = 1080, width = 1920)
bg = 'yellow'
filename = PhotoImage(file = "Fietsen.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


registreren = Button(master=root,
                     text='Registreren',
                     overrelief=RAISED,
                     background='darkblue',
                     foreground='white',
                     font='calibri',
                     height=3,
                     width=20,
                     relief=SOLID,
                     border = 1,
                     command = print('kaas'),
                     )
registreren.place(relx=0.5, rely=0.5, anchor= SE)

inloggen = Button(master=root,
                  text='Inloggen',
                  overrelief=RAISED,
                  background='darkblue',
                  foreground='white',
                  font='calibri',
                  height=3,
                  width=20,
                  relief=SOLID,
                  border = 1,
                  )
inloggen.place(relx=0.5, rely=0.5, anchor=SW)

informatie = Button(master=root,
                    text='Informatie',
                    overrelief = RAISED,
                    background = 'darkblue',
                    foreground = 'white',
                    font = 'calibri',
                    height = 3,
                    width = 20,
                    relief = SOLID,
                    border = 1,
                    )
informatie.place(relx=0.5, rely=0.5, anchor= NE)

afsluiten = Button(master=root,
                   text='Afsluiten',
                   overrelief=RAISED,
                   background= 'Darkblue',
                   foreground='white',
                   font='calibri',
                   height=3,
                   width=20,
                   relief= SOLID,
                   border = 1,
                   )
afsluiten.place(relx=0.5, rely=0.5, anchor= NW)
C.pack()

root.mainloop()

