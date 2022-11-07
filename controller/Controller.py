import inspect

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from model.FrameConfig import FrameConfig
from model.PictureManager import Model
from model.time_manager.PictureTimeManager import PictureTimeManager
from model.time_manager.TimeState import TimeState
from model.time_manager.TouchDurationTimeManager import TouchDurationTimeManager
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
        Timer
        '''
        self.touchTimer = TouchDurationTimeManager(self.touchDurationCallback)
        self.pictureTimer = PictureTimeManager(self.pictureLoopCallback)
        self.startPictureTimer()

        '''
        SmartPicFrame screen control
        '''
        self.view.arrowBtn.clicked.connect(self.nextPicture)
        self.view.arrowBtnL.clicked.connect(self.backwardImage)
        self.view.btnDev.clicked.connect(self.view.showDevMode)

        self.view.dev.btnFullScreen.clicked.connect(self.toggleFullScreen)
        self.view.dev.btnClose.clicked.connect(self.updateSettings)

        self.view.btnTouch.clicked.connect(self.startTouchTimer)

        '''
        Controller logic
        '''
        self.nextPicture(self)

    def nextPicture(self, event):
        Log.l(inspect.currentframe(), "nextPicture")
        self.forwardImage()

    def forwardImage(self):
        Log.l(inspect.currentframe(), "updateImage")
        self.counter = self.model.getCounterValue(self.counter, "r")
        self.setImage(self.getImage())

    def backwardImage(self, event):
        self.counter = self.model.getCounterValue(self.counter, "l")
        self.setImage(self.getImage())

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
            self.fc.width = self.fc.w
            self.fc.height = self.fc.h
        else:
            self.view.showMaximized()
            self.view.showNormal()
            self.fc.width = 1280
            self.fc.height = 720

        self.view.dev.setPosition()
        self.view.setPosition()

    def pictureLoopCallback(self):
        Log.d(inspect.currentframe(), "pictureLoopCallback")
        self.forwardImage()

    def touchDurationCallback(self):
        Log.d(inspect.currentframe(), "touchDurationCallback")
        match self.touchTimer.state:
            case TimeState.started:
                self.view.touchLabel.show()
            case TimeState.stopped:
                self.view.touchLabel.hide()

    def startTouchTimer(self, event):
        self.touchTimer.startTouchTimer(self.fc.touchDurationTime)

    def startPictureTimer(self):
        self.pictureTimer.startLoopTimer(self.fc.pictureTime)

    def updateSettings(self, event):
        self.view.hideDevMode()
        self.fc.updateConfig(pictureTime=self.view.dev.getPictureTime())
        self.startPictureTimer()
