import inspect

from PyQt5.QtCore import QTimer

from model.time_manager.TimeState import TimeState
from utils import Log


class TouchDurationTimeManager:
    def __init__(self, callback):
        self.callback = callback
        self.state = TimeState.none
        self.__timer = QTimer()

    def startTouchTimer(self, time):
        Log.d(inspect.currentframe(), "start touch timer")
        self.state = TimeState.started
        self.callback()
        if self.__timer:
            self.__timer.stop()
            self.__timer.deleteLater()
        self.__timer = QTimer()
        self.__timer.timeout.connect(lambda: self.quitTouchTimer())
        self.__timer.setSingleShot(True)
        self.__timer.start(time)

    def quitTouchTimer(self):
        Log.d(inspect.currentframe(), "stop touch timer")
        self.state = TimeState.stopped
        self.callback()