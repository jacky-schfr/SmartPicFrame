from PyQt5.QtCore import Qt, QSize, QEvent
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

from model.FrameConfig import FrameConfig
from view.QTransparentButtonView import TransparentButton
from view.QDevelopView import QDevelopView


class QSmartFrameView(QMainWindow):

    def __init__(self):
        super().__init__()

        self.fc = FrameConfig()

        self.setWindowTitle("SmartPicFrame")
        self.setObjectName("main")
        self.setStyleSheet("QMainWindow#main {background-color:'BLACK';}")

        self.image = QLabel(self)
        self.image.setAlignment(Qt.AlignCenter)
        self.pixmap = QPixmap("")
        self.image.setPixmap(self.pixmap)


        '''
        Touch Layer / Frame
        '''
        self.touchFrame = QLabel(self)

        '''
        Initialize Buttons
        '''
        self.msg = QLabel(self)
        self.msg.setStyleSheet("color:'WHITE'; background-color: hsva(0, 0, 0, 60%); font: large 'Arial'; font-size: 50px;")
        self.msg.setFixedWidth(700)
        self.msg.setAlignment(Qt.AlignLeft)
        self.msg.setWordWrap(True)

        self.pauseBtn = TransparentButton(self, 'graphics/pauseBtn.png')
        self.playBtn = TransparentButton(self, 'graphics/playBtn.png')
        self.playBtn.btn.hide()
        self.arrowBtn = TransparentButton(self, 'graphics/arrowButtonTmp.png')
        self.arrowBtnL = TransparentButton(self, 'graphics/arrowButtonTmpL.png')
        self.messageBtn = TransparentButton(self, 'graphics/messageBtn.png')
        self.messageOpen = TransparentButton (self, 'graphics/messageOpen.png')
        self.messageOpen.btn.setIconSize(QSize(200, 200))
        self.messageBtn.btn.hide()

        '''
        QDevelopView
        '''
        self.dev = QDevelopView(self)
        self.dev.frame.hide()

        self.setPosition()

        self.show()

    def setPosition(self):
        self.setGeometry(0, 0, self.fc.width, self.fc.height)

        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)

        self.arrowBtn.btn.move(self.fc.width - 200, int(self.fc.height/2)-100)
        self.arrowBtnL.btn.move(50, int(self.fc.height/2)-100)
        self.pauseBtn.btn.move(int(self.fc.width/2)-100, int(self.fc.height/2)-100)
        self.playBtn.btn.move(int(self.fc.width / 2) - 100, int(self.fc.height / 2) - 100)
        self.messageBtn.btn.move(self.fc.width - 200, self.fc.height - 175)
        self.messageOpen.btn.move(self.fc.width - 200, self.fc.height - 200)
        self.move(qtRectangle.topLeft())

        self.touchFrame.resize(self.fc.width, self.fc.height)
        self.image.resize(self.fc.width, self.fc.height)

    def showDevMode(self):
        self.dev.setValues()
        self.dev.frame.show()

    def hideDevMode(self):
        self.dev.frame.hide()

    def touchVisibility(self):
        if not self.fc.isTouch:
            self.arrowBtn.btn.hide()
            self.arrowBtnL.btn.hide()
            self.pauseBtn.btn.hide()
            self.playBtn.btn.hide()
        else:
            self.arrowBtn.btn.show()
            self.arrowBtnL.btn.show()
            if self.fc.pause:
                self.playBtn.btn.show()
            else:
                self.pauseBtn.btn.show()

    def messageVisibility(self):
        if self.fc.showMessage:
            self.messageBtn.btn.hide()
            self.messageOpen.btn.show()
            self.msg.show()
        else:
            self.messageBtn.btn.show()
            self.messageOpen.btn.hide()
            self.msg.hide()

    def messageMove(self):
        self.msg.move(int(self.fc.width/2 - self.msg.width()/2), int(self.fc.height - self.fc.msgHeight - 50))

    def keyPressEvent(self, event):
        if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Escape:
            self.showDevMode()

