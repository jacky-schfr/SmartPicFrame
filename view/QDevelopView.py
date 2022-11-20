import inspect

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QLabel, QPushButton, QGraphicsColorizeEffect, QLineEdit

from model.FrameConfig import FrameConfig
from utils import Log


def getColorEffect():
    color_effect = QGraphicsColorizeEffect()
    color_effect.setColor(Qt.white)
    return color_effect


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
        self.title.setGraphicsEffect(getColorEffect())
        self.title.setFont(QFont('Arial', 24))
        self.title.setFixedSize(250, 50)

        self.pathName = QLabel(self.frame)
        self.pathName.setText("Verzeichnis (Bilder):")
        self.pathName.setGraphicsEffect(getColorEffect())
        self.pathName.setFont(QFont('Arial', 12))
        self.pathLine = QLineEdit(self.frame)
        self.pathLine.resize(700, 24)
        self.pathLine.setFont(QFont('Arial', 10))

        self.durationName = QLabel(self.frame)
        self.durationName.setText("Anzeigedauer:")
        self.durationName.setGraphicsEffect(getColorEffect())
        self.durationName.setFont(QFont('Arial', 12))
        self.durationLine = QLineEdit(self.frame)
        self.durationLine.resize(200, 24)
        self.durationLine.setFont(QFont('Arial', 10))
        self.durationUnit = QLabel(self.frame)
        self.durationUnit.setText("in Sekunden")
        self.durationUnit.setGraphicsEffect(getColorEffect())
        self.durationUnit.setFont(QFont('Arial', 12))

        self.seminoName = QLabel(self.frame)
        self.seminoName.setText("Semino-Modus:")
        self.seminoName.setGraphicsEffect(getColorEffect())
        self.seminoName.setFont(QFont('Arial', 12))
        self.btnSemino = QPushButton(self.frame)
        self.btnSemino.setCheckable(True)
        self.btnSemino.clicked.connect(self.__toggleBtnSemino)

        self.fullScreenName = QLabel(self.frame)
        self.fullScreenName.setText("Vollbild:")
        self.fullScreenName.setGraphicsEffect(getColorEffect())
        self.fullScreenName.setFont(QFont('Arial', 12))
        self.btnFullScreen = QPushButton(self.frame)
        self.btnFullScreen.setCheckable(True)
        self.btnFullScreen.clicked.connect(self.__toggleBtnFullScreen)

        self.btnClose = QPushButton(self.frame)
        self.btnClose.setText("Speichern/Schließen")

        self.__toggleBtnFullScreen()
        self.__toggleBtnSemino()
        self.setPosition()
        self.setValues()

    def setPosition(self):
        self.guideLine1 = int(self.__getRelativePos(30))
        self.guideLine2 = int(self.__getRelativePos(80))

        self.frame.setGeometry(self.offset, self.offset, self.fc.width - self.offset * 2,
                               self.fc.height - self.offset * 2)

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

    def setValues(self):
        self.pathLine.setText(self.fc.path)
        self.durationLine.setText(str(self.fc.pictureTime))
        self.btnFullScreen.setChecked(self.fc.isFullScreen)

        self.__toggleBtnFullScreen()
        self.__toggleBtnSemino()

    def getPath(self):
        return self.pathLine.text()

    def getPictureTime(self):
        return int(self.durationLine.text())

    def __toggleBtnFullScreen(self):
        if self.btnFullScreen.isChecked():
            self.btnFullScreen.setText("An")
        else:
            self.btnFullScreen.setText("Aus")

    def __toggleBtnSemino(self):
        if self.btnSemino.isChecked():
            self.btnSemino.setText("An")
        else:
            self.btnSemino.setText("Aus")

    def __getRelativePos(self, percent):
        return (self.fc.height - self.offset * 2) / 100 * percent
