import inspect
from tkinter import *
from PIL import ImageTk, Image

from utils import log


class View(Tk):
    def __init__(self, callback):
        Tk.__init__(self)
        self.callback = callback

        self.canvas = Canvas(self, width=800, height=800)
        self.canvas.pack()
        self.img = ImageTk.PhotoImage(Image.open(callback))
        self.canvas.create_image(20, 20, anchor=NW, image=self.img)

        log.l(inspect.currentframe(), "init view")

