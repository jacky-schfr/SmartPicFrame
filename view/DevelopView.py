import inspect
import tkinter

from model.FrameConfig import FrameConfig
from utils import Log


class DevelopView(object):
    def __init__(self, master):
        Log.l(inspect.currentframe(), "init develop screen")

        self.fc = FrameConfig()

        self.offset = 200

        self.frame = tkinter.Frame(master, bg="black", highlightbackground="grey", highlightthickness=2)
        self.frame.place(x=self.fc.width, y=0 + self.offset / 2, width=self.fc.width - self.offset, height=self.fc.height - self.offset)

        self.label = tkinter.Label(self.frame, text="Develop", bg="black", fg="white")
        self.label.place(x=(self.fc.width - self.offset) / 2 - 75, y=50, width=150)

        self.btnFullScreen = tkinter.Button(self.frame, text="Vollbild an/aus")
        self.btnFullScreen.place(x=50, y=self.fc.height - 350, width=150)

        self.btnClose = tkinter.Button(self.frame, text="Schließen")
        self.btnClose.place(x=50, y=self.fc.height - 250, width=150)

    def update(self):
        self.frame.place_configure(width=self.fc.width - self.offset, height=self.fc.height - self.offset)
        self.label.place_configure(x=(self.fc.width - self.offset) / 2 - 75)
        self.btnFullScreen.place_configure(y=self.fc.height - 350)
        self.btnClose.place_configure(y=self.fc.height - 250)
