from PyQt5.QtCore import Qt
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

        self.msg = QLabel("", self)
        self.msg.setStyleSheet("border: 4px solid white; border-radius: 4px; color:'WHITE';")

        '''
        Touch Layer / Frame
        '''
        self.touchFrame = QLabel(self)
        self.touchFrame.setFixedSize(self.fc.width, self.fc.height)

        '''
        Initialize Buttons
        '''
        self.btnDev = QPushButton(self)
        self.btnDev.setText("Dev Mode")

        self.pauseBtn = TransparentButton(self, 'graphics/pauseBtn.png')
        self.playBtn = TransparentButton(self, 'graphics/playBtn.png')
        self.playBtn.btn.hide()
        self.arrowBtn = TransparentButton(self, 'graphics/arrowButtonTmp.png')
        self.arrowBtnL = TransparentButton(self, 'graphics/arrowButtonTmpL.png')

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
        self.move(qtRectangle.topLeft())

        self.image.resize(self.fc.width, self.fc.height)

        self.msg.move(self.fc.width - 200, self.fc.height - 70)
        self.btnDev.move(130, self.fc.height - 70)
        self.arrowBtn.btn.move(self.fc.width - 200, int(self.fc.height/2)-100)
        self.arrowBtnL.btn.move(50, int(self.fc.height/2)-100)
        self.pauseBtn.btn.move(int(self.fc.width/2)-100, int(self.fc.height/2)-100)
        self.playBtn.btn.move(int(self.fc.width / 2) - 100, int(self.fc.height / 2) - 100)


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


