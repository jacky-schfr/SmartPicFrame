import inspect
import sys

from PyQt5.QtWidgets import QApplication
from controller.Controller import Controller
# from playground.QMainWindow import QMainWindow
from model.FrameConfig import FrameConfig
from utils import Log

if __name__ == "__main__":
    Log.l(inspect.currentframe(), "init main")

    fc = FrameConfig()

    # create pyqt5 app
    App = QApplication(sys.argv)

    rect = App.desktop().screenGeometry()
    fc.h = rect.height()
    fc.w = rect.width()

    window = Controller()
    sys.exit(App.exec())
