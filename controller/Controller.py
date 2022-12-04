import inspect

import dateutil.utils
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from model.FrameConfig import FrameConfig
from model.JsonManager import JsonManager
from model.PictureManager import PictureManager
from model.time_manager.PictureTimeManager import PictureTimeManager
from model.time_manager.TimeState import TimeState
from model.time_manager.TouchDurationTimeManager import TouchDurationTimeManager
from model.time_manager.UpdateListTimeManager import UpdateListTimeManager
from utils import Log
from view.QSmartFrameView import QSmartFrameView


class Controller(object):
    def __init__(self):
        Log.l(inspect.currentframe(), "init controller")
        self.fc = FrameConfig()
        self.jm = JsonManager()

        self.pictureManager = PictureManager()
        self.view = QSmartFrameView()

        '''
        Timer
        '''
        self.updateListTimer = UpdateListTimeManager(self.updateListCallback)
        self.touchTimer = TouchDurationTimeManager(self.touchDurationCallback)
        self.pictureTimer = PictureTimeManager(self.pictureLoopCallback)
        self.startUpdateListTimer()
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

        self.lastUpdate()

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
        self.pictureManager.setCounterValue("r")
        self.setImage(self.pictureManager.getImage())

    def backwardImage(self, event):
        self.pictureManager.setCounterValue("l")
        self.setImage(self.pictureManager.getImage())

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

    def setImage(self, image):
        Log.l(inspect.currentframe(), "setImage")
        self.view.messageVisibility()
        bgPix= QPixmap(image).scaled(self.fc.width, self.fc.height, Qt.KeepAspectRatioByExpanding)
        resizedPix = QPixmap(image).scaled(self.fc.width, self.fc.height, Qt.KeepAspectRatio)

        self.view.image.setPixmap(resizedPix)
        self.view.bgImage.setPixmap(bgPix)
        message = self.pictureManager.images[self.pictureManager.counter].message
        self.imageCounter()
        self.view.imgCount.adjustSize()
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

    def updateListCallback(self):
        Log.d(inspect.currentframe(), "updateListCallback")

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

    def startUpdateListTimer(self):
        self.updateListTimer.startUpdateListTimer()

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

    def lastUpdate(self):
        self.fc.lastUpdate = str(dateutil.utils.today().strftime("%d.%m.%Y"))
        self.view.lastDate.setText("Aktueller Stand:   " + self.fc.lastUpdate)

    def imageCounter(self):
        pic = self.pictureManager.counter
        if pic == 0:
            pic = len(self.pictureManager.images)
        self.view.imgCount.setText(str(pic) + " / " + str(len(self.pictureManager.images)))
