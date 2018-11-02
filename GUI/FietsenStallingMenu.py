from .test import Window
from tkinter import *
from tkinter.messagebox import showwarning, showinfo
import random
import qrcode


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




if __name__ == "__main__":
    window = Window(None)
    window.geometry('1920x1080')
    window.title('Home')
    window.configure(bg='yellow')
    window.mainloop()






