import inspect
import sys

from PyQt5.QtWidgets import QApplication
from controller.Controller import Controller
from playground.QMainWindow import QMainWindow
from utils import Log

if __name__ == "__main__":
    Log.l(inspect.currentframe(), "init main")

    '''
    # create pyqt5 app
    App = QApplication(sys.argv)
    window = QMainWindow()
    sys.exit(App.exec())
    '''

    c = Controller()
