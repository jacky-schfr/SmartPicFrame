from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton


class TransparentButton:
    def __init__(self, parentSelf, icon):

        self.btn = QPushButton(parentSelf)

        self.btn.setObjectName("Btn")
        self.btn.setIconSize(QSize(150, 150))
        self.btn.setIcon(QIcon(icon))
        self.btn.adjustSize()
        self.btn.setFlat(True)
        self.btn.setStyleSheet("QPushButton#Btn {background-color: transparent}")


