from tkinter import *
from tkinter.messagebox import showinfo

def hulpqr(self):
    self.top.withdraw()
    self.top = Toplevel()
    self.top.title("Registreren")
    self.top.geometry("1920x1080")

    self.qrhulp = Button(master=self.top, text='Hulp QR', command=self.infoalgemeen,
                                bg='lightgreen', relief=SOLID, font='Calibri',
                                width=40)
    self.qrhulp.place(relx=0.5, rely=0.5, anchor=NE)

    def qr_hulp(self):
        hulp = 'Om een QR te scannen moet u een QR of Barcode scanner downloaden op uw smartphone. Na het scannen krijgt u de code te zien, bewaar deze om later je fiets weer op te kunnen halen. '
        showinfo(title='Hulp QR code.', message=hulp)