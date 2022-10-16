import inspect

from PIL import ImageTk, Image, ImageOps

from model.FrameConfig import FrameConfig
from model.PictureManager import Model
from utils import Log
from view.SmartFrameView import SmartFrameView


class Controller(object):
    def __init__(self):
        Log.l(inspect.currentframe(), "init controller")
        self.fc = FrameConfig()

        self.counter = 0
        self.isDevMode = False

        self.model = Model()
        self.view = SmartFrameView()

        '''
        SmartPicFrame screen control
        '''
        self.view.btn.bind("<Button>", self.updateImage)
        self.view.btnDev.bind("<Button>", lambda event, isDevMode=True: self.setDevMode(isDevMode))

        '''
        Develop screen control
        '''
        self.view.dev.btnFullScreen.bind("<Button>", self.setFullScreen)
        self.view.dev.btnClose.bind("<Button>", lambda event, isDevMode=False: self.setDevMode(isDevMode))

        '''
        Controller logic
        '''
        self.updateImage(self)
        self.setDevMode(False)

        self.view.mainloop()

    def updateImage(self, event):
        Log.l(inspect.currentframe(), "updateImage")
        self.setImage(self.getImage())
        if self.counter < len(self.model.images) - 1:
            self.counter += 1
        else:
            self.counter = 0

    def getImage(self):
        Log.l(inspect.currentframe(), "getImage")
        temp = self.model.images[self.counter]
        img = temp.file
        Log.d(inspect.currentframe(), "image: " + str(img))
        return img

    def setImage(self, param):
        Log.l(inspect.currentframe(), "setImage")
        temp = Image.open(param)
        temp = ImageOps.contain(temp, (self.fc.width, self.fc.height))
        img = ImageTk.PhotoImage(temp)
        self.view.label.configure(image=img)
        self.view.label.image = img
        message = self.model.images[self.counter].message
        self.view.msg.config(text=message)

    def setDevMode(self, isDevMode):
        Log.l(inspect.currentframe(), "setDevMode: " + str(isDevMode))
        self.isDevMode = not self.isDevMode
        if isDevMode:
            self.view.dev.frame.place_configure(x=0 + + self.view.dev.offset / 2)
        else:
            self.view.dev.frame.place_configure(x=self.fc.width)

    def setFullScreen(self, event):
        self.fc.isFullScreen = not self.fc.isFullScreen
        if self.fc.isFullScreen:
            self.view.attributes("-fullscreen", True)
            self.fc.width = self.view.winfo_width()
            self.fc.height = self.view.winfo_height()
        else:
            self.view.attributes("-fullscreen", False)
            self.fc.width = 1280
            self.fc.height = 720

        # Update UI
        self.view.update()
        self.view.dev.update()
