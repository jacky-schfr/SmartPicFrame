import inspect

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from model.FrameConfig import FrameConfig
from model.JsonManager import JsonManager
from model.PictureManager import PictureManager
from model.time_manager.PictureTimeManager import PictureTimeManager
from model.time_manager.TimeState import TimeState
from model.time_manager.TouchDurationTimeManager import TouchDurationTimeManager
from utils import Log
from view.QSmartFrameView import QSmartFrameView


class Controller(object):
    def __init__(self):
        Log.l(inspect.currentframe(), "init controller")
        self.fc = FrameConfig()
        self.jm = JsonManager()

        #TODO @jacky: counter und getImage() können in den PictureManager.py eingebaut werden.
        self.counter = 0

        self.pictureManager = PictureManager()
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
        self.view.arrowBtn.btn.clicked.connect(self.nextPicture)
        self.view.arrowBtnL.btn.clicked.connect(self.backwardImage)
        self.view.pauseBtn.btn.clicked.connect(self.pauseImage)
        self.view.playBtn.btn.clicked.connect(self.pauseImage)

        self.view.dev.btnClose.clicked.connect(self.updateSettings)

        self.view.messageBtn.btn.clicked.connect(self.toggleMessage)
        self.view.messageOpen.btn.clicked.connect(self.toggleMessage)

        self.view.arrowBtn.btn.clicked.connect(self.startTouchTimer)
        self.view.arrowBtnL.btn.clicked.connect(self.startTouchTimer)
        self.view.pauseBtn.btn.clicked.connect(self.startTouchTimer)
        self.view.playBtn.btn.clicked.connect(self.startTouchTimer)
        self.view.touchFrame.mousePressEvent = self.startTouchTimer

        '''
        Controller logic
        '''
        self.nextPicture(self)

        '''
        Update FrameConfig from Json file
        '''
        self.jm.readJsonFile()
        self.jm.writeJsonFile()

        self.view.touchVisibility()
        self.updateScreen()

    def nextPicture(self, event):
        Log.l(inspect.currentframe(), "nextPicture")
        self.forwardImage()

    def forwardImage(self):
        self.counter = self.pictureManager.getCounterValue(self.counter, "r")
        self.setImage(self.getImage())

    def backwardImage(self, event):
        self.counter = self.pictureManager.getCounterValue(self.counter, "l")
        self.setImage(self.getImage())

    def pauseImage(self, event):
        self.fc.pause = not self.fc.pause

        if TimeState.started:
            if self.fc.pause:
                self.pictureTimer.quitLoopTimer()
                self.view.pauseBtn.btn.hide()
                self.view.playBtn.btn.show()
            else:
                self.startPictureTimer()
                self.view.playBtn.btn.hide()
                self.view.pauseBtn.btn.show()

    def getImage(self):
        Log.l(inspect.currentframe(), "getImage")
        temp = self.pictureManager.images[self.counter]
        img = temp.file
        Log.d(inspect.currentframe(), "image: " + str(img))
        return img

    def setImage(self, param):
        Log.l(inspect.currentframe(), "setImage")
        self.view.messageVisibility()
        resizedPix = QPixmap(param).scaled(self.fc.width, self.fc.height, Qt.KeepAspectRatio)

        self.view.image.setPixmap(resizedPix)
        message = self.pictureManager.images[self.counter].message
        if message == "":
            self.view.messageBtn.btn.hide()
            self.view.messageOpen.btn.hide()
            self.view.msg.hide()
        else:
            self.view.msg.setText(message)
            self.view.msg.adjustSize()
            self.fc.msgHeight = self.view.msg.height()
            self.view.messageMove()

    def updateScreen(self):
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
        self.view.messageMove()

    def pictureLoopCallback(self):
        Log.d(inspect.currentframe(), "pictureLoopCallback")
        self.forwardImage()

    def touchDurationCallback(self):
        Log.d(inspect.currentframe(), "touchDurationCallback")
        match self.touchTimer.state:
            case TimeState.started:
                self.fc.isTouch = True
            case TimeState.stopped:
                self.fc.isTouch = False
        self.view.touchVisibility()

    def startTouchTimer(self, event):
        self.touchTimer.startTouchTimer(self.fc.touchDurationTime)

    def startPictureTimer(self):
        self.pictureTimer.startLoopTimer(self.fc.pictureTime)

    def updateSettings(self, event):
        self.view.hideDevMode()
        self.fc.toggleFullScreen(self.view.dev.btnFullScreen.isChecked())
        self.fc.updateConfig(path=self.view.dev.getPath(), pictureTime=self.view.dev.getPictureTime())
        self.jm.writeJsonFile()
        self.updateScreen()

    def toggleMessage(self, event):
        self.fc.showMessage = not self.fc.showMessage
        self.view.messageVisibility()
