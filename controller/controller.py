import inspect
import os

from PIL import ImageTk, Image, ImageOps

from model.model import Model
from utils import log
from view.view import View


class Controller(object):
    def __init__(self):
        self.counter = 0

        self.model = Model()
        self.view = View()
        self.view.btn.bind("<Button>", self.updateImage)

        self.updateImage(self)
        self.view.mainloop()

        log.l(inspect.currentframe(), "init controller")

    def updateImage(self, event):
        log.l(inspect.currentframe(), "updateImage")
        self.setImage(self.getImage())
        if self.counter < len(self.model.images)-1:
            self.counter += 1
        else:
            self.counter = 0


    def getImage(self):
        log.l(inspect.currentframe(), "getImage")
        temp = self.model.images[self.counter]
        img = temp.file
        log.d(inspect.currentframe(), img)
        return img

    def setImage(self, param):
        log.d(inspect.currentframe(), param)
        log.l(inspect.currentframe(), "setImage")
        temp = Image.open(param)
        temp = ImageOps.contain(temp, (self.view.width, self.view.height))
        img = ImageTk.PhotoImage(temp)
        self.view.label.configure(image=img)
        self.view.label.image = img
        message = self.model.images[self.counter].message
        self.view.msg.config(text=message)
