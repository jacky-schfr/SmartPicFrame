from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
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

        self.btn = QPushButton(self)
        self.btn.setText("Nächstes Bild")

        self.btnDev = QPushButton(self)
        self.btnDev.setText("Dev Mode")

        self.dev = QDevelopView()
        self.setCentralWidget(self.dev)
        self.dev.hide()

        self.setPosition()

        self.show()

    def setPosition(self):
        self.setGeometry(0, 0, self.fc.width, self.fc.height)

        self.msg.move(self.fc.width - 200, self.fc.height - 70)
        self.btn.move(20, self.fc.height - 70)
        self.btnDev.move(130, self.fc.height - 70)

    def showDevMode(self):
        self.dev.show()

    def hideDevMode(self):
        self.dev.hide()

