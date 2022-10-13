import inspect
import tkinter
from math import floor
from tkinter import *
from PIL import ImageTk, Image

from utils import log


class View(Tk):
    def __init__(self, callback):
        Tk.__init__(self)
        self.callback = callback

        wWidth, wHeight = 800, 800

        self.canvas = Canvas(self, width=wWidth, height=wHeight)
        self.canvas.pack()
        width, height = wWidth * 0.9, wHeight * 0.9
        self.img = ImageTk.PhotoImage(Image.open(callback).resize((int(width), int(height)), Image.ANTIALIAS))
        self.canvas.create_image(20, 20, anchor=NW, image=self.img)
        self.btn = tkinter.Button(master=self, text="Nächstes Bild", command=self.callback)
        self.btn.place(x=100, y=600, width=150)

        log.l(inspect.currentframe(), "init view")

