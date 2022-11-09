import inspect

from utils import Log


class Picture(object):
    def __init__(self, file):
        self.file = file
        self.message = ""
        self.readMessage()

    def readMessage(self):
        Log.l(inspect.currentframe(), "readMessage")
        if "_m_" in self.file:
            temp = self.file.split("_m_")
            if ".JPG" in temp[1]:
                temp = temp[1].split(".JPG")
            if ".jpg" in temp[1]:
                temp = temp[1].split(".jpg")
            if ".PNG" in temp[1]:
                temp = temp[1].split(".PNG")
            if ".png" in temp[1]:
                temp = temp[1].split(".png")
            self.message = temp[0]
