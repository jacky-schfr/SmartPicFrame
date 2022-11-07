from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import *
from PyQt5.uic.properties import QtCore

from model.FrameConfig import FrameConfig
from view.QDevelopView import QDevelopView


class QSmartFrameView(QMainWindow):

    def __init__(self):
        super().__init__()

        self.fc = FrameConfig()

        self.setWindowTitle("Gallery")
        self.setObjectName("main")
        self.setStyleSheet("QWidget#main {background-color:'BLACK';}")

        self.image = QLabel(self)
        self.image.setAlignment(Qt.AlignCenter)
        self.pixmap = QPixmap("")
        self.image.setPixmap(self.pixmap)

        self.msg = QLabel("", self)
        self.msg.setStyleSheet("border: 4px solid white; border-radius: 4px; color:'WHITE';")

        '''
        Initialize Buttons
        '''
        self.btnDev = QPushButton(self)
        self.btnDev.setText("Dev Mode")

        self.pauseBtn = QPushButton(self)
        self.pauseBtn.setObjectName("arrowBtn")
        self.pauseBtn.setIconSize(QSize(150, 150))
        self.pauseBtn.setIcon(QIcon('graphics/pauseBtn.png'))
        self.pauseBtn.adjustSize()
        self.pauseBtn.setFlat(True)
        self.pauseBtn.setStyleSheet("QPushButton#arrowBtn {background-color: transparent}")

        self.playBtn = QPushButton(self)
        self.playBtn.setObjectName("arrowBtn")
        self.playBtn.setIconSize(QSize(150, 150))
        self.playBtn.setIcon(QIcon('graphics/playBtn.png'))
        self.playBtn.adjustSize()
        self.playBtn.setFlat(True)
        self.playBtn.setStyleSheet("QPushButton#arrowBtn {background-color: transparent}")
        self.playBtn.hide()

        self.arrowBtn = QPushButton(self)
        self.arrowBtn.setObjectName("arrowBtn")
        self.arrowBtn.setIconSize(QSize(150, 150))
        self.arrowBtn.setIcon(QIcon('graphics/arrowButtonTmp.png'))
        self.arrowBtn.adjustSize()
        self.arrowBtn.setFlat(True)
        self.arrowBtn.setStyleSheet("QPushButton#arrowBtn {background-color: transparent}")

        self.arrowBtnL = QPushButton(self)
        self.arrowBtnL.setObjectName("arrowBtn")
        self.arrowBtnL.setIconSize(QSize(150, 150))
        self.arrowBtnL.setIcon(QIcon('graphics/arrowButtonTmpL.png'))
        self.arrowBtnL.adjustSize()
        self.arrowBtnL.setFlat(True)
        self.arrowBtnL.setStyleSheet("QPushButton#arrowBtn {background-color: transparent}")

        '''
        Touch Functions
        '''
        self.btnTouch = QPushButton(self)
        self.btnTouch.setText("Touch on screen")
        self.btnTouch.adjustSize()

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

        self.image.resize(self.fc.width, self.fc.height, )

        self.msg.move(self.fc.width - 200, self.fc.height - 70)
        self.btnDev.move(130, self.fc.height - 70)
        self.arrowBtn.move(self.fc.width - 200, int(self.fc.height/2)-100)
        self.arrowBtnL.move(50, int(self.fc.height/2)-100)
        self.pauseBtn.move(int(self.fc.width/2)-100, int(self.fc.height/2)-100)
        self.playBtn.move(int(self.fc.width / 2) - 100, int(self.fc.height / 2) - 100)

        self.btnTouch.move(130, self.fc.height - 120)

    def showDevMode(self):
        self.dev.setValues()
        self.dev.frame.show()

    def hideDevMode(self):
        self.dev.frame.hide()

    def touchVisibility(self):
        if not self.fc.isTouch:
            self.arrowBtn.hide()
            self.arrowBtnL.hide()
            self.pauseBtn.hide()
            self.playBtn.hide()
        else:
            self.arrowBtn.show()
            self.arrowBtnL.show()
            if self.fc.pause:
                self.playBtn.show()
            else:
                self.pauseBtn.show()


