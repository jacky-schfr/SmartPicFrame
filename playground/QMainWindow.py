from PyQt5.QtWidgets import *


class QMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the title
        self.setWindowTitle("Color")

        # setting  the geometry of window
        self.setGeometry(0, 0, 400, 300)

        self.label = QLabel("back", self)
        self.label.setStyleSheet("border: 3px solid blue; background-color: red;")
        self.label.move(100, 100)

        self.label_2 = QLabel('front', self)
        self.label_2.move(140, 90)
        self.label_2.setStyleSheet("border: 3px solid blue; background-color: rgba(0, 255, 255, 90);")

        # show all the widgets
        self.show()
