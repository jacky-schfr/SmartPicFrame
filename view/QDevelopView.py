import inspect

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QWidget, QVBoxLayout, QLabel, QPushButton, QGraphicsColorizeEffect, QHBoxLayout, \
    QLineEdit

from model.FrameConfig import FrameConfig
from utils import Log


class QDevelopView:
    def __init__(self, parentSelf):
        super().__init__()
        Log.l(inspect.currentframe(), "init develop screen")

        self.fc = FrameConfig()

        self.offset = 50
        ''' Guide-Lines '''
        self.guideLine1 = None
        self.guideLine2 = None

        self.frame = QFrame(parentSelf)
        self.frame.setObjectName("mainFrame")
        self.frame.setStyleSheet('QWidget#mainFrame { border: 1px solid grey; background-color: rgba(0, 0, 0, 220) }')

        self.title = QLabel(self.frame)
        self.title.setText("Einstellungen")
        self.title.setGraphicsEffect(self.getColorEffect())
        self.title.setFont(QFont('Arial', 24))
        self.title.setFixedSize(250, 50)

        self.pathName = QLabel(self.frame)
        self.pathName.setText("Verzeichnis (Bilder):")
        self.pathName.setGraphicsEffect(self.getColorEffect())
        self.pathName.setFont(QFont('Arial', 12))
        self.pathLine = QLineEdit(self.frame)
        self.pathLine.resize(500, 24)

        self.durationName = QLabel(self.frame)
        self.durationName.setText("Anzeigedauer:")
        self.durationName.setGraphicsEffect(self.getColorEffect())
        self.durationName.setFont(QFont('Arial', 12))
        self.durationLine = QLineEdit(self.frame)
        self.durationLine.resize(200, 24)
        self.durationUnit = QLabel(self.frame)
        self.durationUnit.setText("in Sekunden")
        self.durationUnit.setGraphicsEffect(self.getColorEffect())
        self.durationUnit.setFont(QFont('Arial', 12))

        self.seminoName = QLabel(self.frame)
        self.seminoName.setText("Semino-Modus:")
        self.seminoName.setGraphicsEffect(self.getColorEffect())
        self.seminoName.setFont(QFont('Arial', 12))
        self.btnSemino = QPushButton(self.frame)
        self.btnSemino.setText("an/aus")

        self.fullScreenName = QLabel(self.frame)
        self.fullScreenName.setText("Vollbild:")
        self.fullScreenName.setGraphicsEffect(self.getColorEffect())
        self.fullScreenName.setFont(QFont('Arial', 12))
        self.btnFullScreen = QPushButton(self.frame)
        self.btnFullScreen.setText("an/aus")

        self.btnClose = QPushButton(self.frame)
        self.btnClose.setText("Schließen")

        self.setPosition()

    def setPosition(self):
        self.guideLine1 = int(self.getRelativePos(30))
        self.guideLine2 = int(self.getRelativePos(80))

        self.frame.setGeometry(self.offset, self.offset, self.fc.width - self.offset * 2, self.fc.height - self.offset * 2)

        self.title.move(int(self.fc.width / 2 - self.title.width() / 2 - self.offset), 100)

        self.pathName.move(20, self.guideLine1)
        self.pathLine.move(250, self.guideLine1)

        self.durationName.move(20, self.guideLine1 + 30)
        self.durationLine.move(250, self.guideLine1 + 30)
        self.durationUnit.move(460, self.guideLine1 + 30)

        self.seminoName.move(20, self.guideLine1 + 100)
        self.btnSemino.move(250, self.guideLine1 + 100)

        self.fullScreenName.move(20, self.guideLine1 + 130)
        self.btnFullScreen.move(250, self.guideLine1 + 130)

        self.btnClose.move(int(self.fc.width / 2 - self.btnClose.width() / 2 - self.offset), self.guideLine2)

    def getColorEffect(self):
        color_effect = QGraphicsColorizeEffect()
        color_effect.setColor(Qt.white)
        return color_effect

    def getRelativePos(self, percent):
        return (self.fc.height - self.offset * 2) / 100 * percent
