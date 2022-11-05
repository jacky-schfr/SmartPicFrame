import inspect

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QWidget, QVBoxLayout, QLabel, QPushButton, QGraphicsColorizeEffect

from model.FrameConfig import FrameConfig
from utils import Log


class QDevelopView:
    def __init__(self, parentSelf):
        super().__init__()
        Log.l(inspect.currentframe(), "init develop screen")

        self.fc = FrameConfig()

        self.offset = 50

        self.frame = QFrame(parentSelf)
        self.frame.setObjectName("mainFrame")
        self.frame.setStyleSheet('QWidget#mainFrame { border: 1px solid grey; background-color: rgba(0, 0, 0, 220) }')

        self.title = QLabel(self.frame)
        self.title.setText("Develop")
        color_effect = QGraphicsColorizeEffect()
        color_effect.setColor(Qt.white)
        self.title.setGraphicsEffect(color_effect)
        self.title.setFont(QFont('Arial', 24))
        self.title.setFixedSize(250, 50)

        self.btnFullScreen = QPushButton(self.frame)
        self.btnFullScreen.setText("Vollbild an/aus")

        self.btnClose = QPushButton(self.frame)
        self.btnClose.setText("Schließen")

        self.setPosition()

    def setPosition(self):
        self.frame.setGeometry(self.offset, self.offset, self.fc.width - self.offset * 2, self.fc.height - self.offset * 2)
        self.title.move(int(self.fc.width / 2 - self.title.width() / 2), 100)
        self.btnFullScreen.move(20, self.fc.height - self.offset - 200)
        self.btnClose.move(20, self.fc.height - self.offset - 150)
