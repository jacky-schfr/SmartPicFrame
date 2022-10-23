import inspect

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from model.FrameConfig import FrameConfig
from model.PictureManager import Model
from utils import Log
from view.QSmartFrameView import QSmartFrameView


class Controller(object):
    def __init__(self):
        Log.l(inspect.currentframe(), "init controller")
        self.fc = FrameConfig()

        self.counter = 0
        self.isDevMode = False

        self.model = Model()
        self.view = QSmartFrameView()

        '''
        SmartPicFrame screen control
        '''
        self.view.btn.clicked.connect(self.updateImage)
        self.view.btnDev.clicked.connect(self.view.showDevMode)

        self.view.dev.btnFullScreen.clicked.connect(self.toggleFullScreen)
        self.view.dev.btnClose.clicked.connect(self.view.hideDevMode)

        '''
        Controller logic
        '''
        self.updateImage(self)

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
        resizedPix = QPixmap(param).scaled(self.fc.width, self.fc.height, Qt.KeepAspectRatio)
        self.view.image.setPixmap(resizedPix)
        message = self.model.images[self.counter].message
        if message == "":
            self.view.msg.hide()
        else:
            self.view.msg.show()
            self.view.msg.setText(message)
            self.view.msg.adjustSize()

    def toggleFullScreen(self, event):
        self.fc.isFullScreen = not self.fc.isFullScreen
        if self.fc.isFullScreen:
            self.view.showFullScreen()
            self.fc.width = self.view.width()
            self.fc.height = self.view.height()
        else:
            self.view.showNormal()
            self.fc.width = 1280
            self.fc.height = 720

        self.view.dev.setPosition()
        self.view.setPosition()
