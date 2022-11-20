import inspect
import threading
import time

from utils import Log


def worker(arg, callback):
    while not arg["stop"]:
        Log.l(inspect.currentframe(), "worker thread update")
        callback()
        time.sleep(3)


class UpdateListTimeManager:
    def __init__(self, callback):
        self.info = {"stop": False}
        self.thread = threading.Thread(target=worker, args=(self.info, callback))

    def startUpdateListTimer(self):
        self.thread.start()
