import inspect

from PyQt5.QtCore import QTimer
from utils import Log


class PictureTimeManager:
    def __init__(self, callback):
        self.callback = callback
        self.__timer = QTimer()

    def startLoopTimer(self, duration):
        Log.d(inspect.currentframe(), "start loop timer")
        if self.__timer:
            self.__timer.stop()
            self.__timer.deleteLater()
        # TODO: fix the deleteLater timer issue
        self.__timer = QTimer()
        self.__timer.timeout.connect(lambda: self.callback())
        self.__timer.start(duration * 1000)

    def quitLoopTimer(self):
        Log.d(inspect.currentframe(), "stop loop timer")
        if self.__timer:
            self.__timer.stop()
