import inspect

from utils import log


class Picture(object):
    def __init__(self, file):
        self.file = file
        self.message = ""
        self.readMessage()

    def readMessage(self):
        log.l(inspect.currentframe(), "readMessage")
        if "_m_" in self.file:
            temp = self.file.split("_m_")
            temp = temp[1].split(".")
            self.message = temp[0]
