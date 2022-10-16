import inspect
import tkinter
from tkinter import *

from model.FrameConfig import FrameConfig
from utils import Log
from view.DevelopView import DevelopView


class SmartFrameView(Tk):
    def __init__(self):
        Tk.__init__(self)
        Log.l(inspect.currentframe(), "init smartFrame screen")

        self.fc = FrameConfig()

        self.geometry(str(self.fc.width) + "x" + str(self.fc.height))
        self.title("Gallery")
        self.configure(bg="BLACK")

        self.label = Label(self, image="")
        self.label.pack()

        self.msg = Label(self, text="", fg="WHITE", bg="BLACK", padx=5, pady=5)
        self.msg.place(x=self.fc.width - 350, y=self.fc.height - 50, width=300)

        self.btn = tkinter.Button(master=self, text="Nächstes Bild")
        self.btn.place(x=50, y=self.fc.height - 50, width=150)

        self.btnDev = tkinter.Button(master=self, text="Dev")
        self.btnDev.place(x=250, y=self.fc.height - 50, width=150)

        '''
        Develop screen
        '''
        self.dev = DevelopView(self)

    def update(self):
        self.msg.place_configure(x=self.fc.width - 350, y=self.fc.height - 50)
        self.btn.place_configure(y=self.fc.height - 50)
        self.btnDev.place_configure(y=self.fc.height - 50)

