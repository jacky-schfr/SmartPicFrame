from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import *
from model.FrameConfig import FrameConfig
from view.QDevelopView import QDevelopView


class QSmartFrameView(QMainWindow):

    def __init__(self):
        super().__init__()

        self.fc = FrameConfig()

        self.setWindowTitle("Gallery")
        self.setGeometry(0, 0, self.fc.width, self.fc.height)
        self.setObjectName("main")
        self.setStyleSheet("QWidget#main {background-color:'BLACK';}")

        self.image = QLabel(self)
        self.image.resize(self.fc.width, self.fc.height,)
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
        QDevelopView
        '''
        self.dev = QDevelopView()
        self.setCentralWidget(self.dev)
        self.dev.hide()

        self.setPosition()

        self.show()

    def setPosition(self):
        self.setGeometry(0, 0, self.fc.width, self.fc.height)

        self.msg.move(self.fc.width - 200, self.fc.height - 70)
        self.btnDev.move(130, self.fc.height - 70)
        self.arrowBtn.move(self.fc.width - 200, int(self.fc.height/2)-50)
        self.arrowBtnL.move(100, int(self.fc.height/2)-50)

    def showDevMode(self):
        self.dev.show()

    def hideDevMode(self):
        self.dev.hide()

