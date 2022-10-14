import inspect
import tkinter
from tkinter import *
from PIL import ImageTk, Image

from utils import log


class View(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.width = 1300
        self.height = 700

        self.geometry(str(self.width)+"x"+str(self.height))
        self.title("Gallery")
        self.configure(bg="BLACK")

        self.label = Label(self, image="")
        self.label.pack()

        self.msg = Label(self, text="", fg="WHITE", bg="BLACK", padx=5, pady=5)
        self.msg.place(x=self.width-350, y=self.height-50, width=300)

        self.btn = tkinter.Button(master=self, text="Nächstes Bild")
        self.btn.place(x=50, y=self.height-50, width=150)

        log.l(inspect.currentframe(), "init view")
