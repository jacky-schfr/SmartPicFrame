import inspect
import os

from model.FrameConfig import FrameConfig
from model.Picture import Picture

from utils import Log


class PictureManager:
    def __init__(self):
        self.fc = FrameConfig()

        self.counter = 0
        self.images = []

        self.createImageList()

    def createImageList(self):
        if os.path.exists(self.fc.path):
            for file in os.listdir(self.fc.path):
                img = Picture(self.fc.path + file)
                self.images.append(img)
            if not self.images:
                self.images.append(Picture('defaultImage/defaultImg.png'))
        else:
            self.images.append(Picture('defaultImage/defaultImg.png'))

        Log.d(inspect.currentframe(), "defaultImage: " + str(self.images))

    def setCounterValue(self, param):
        if param == "r":
            if self.counter < len(self.images) - 1:
                self.counter += 1
            else:
                self.counter = 0
        else:
            if self.counter > 0:
                self.counter -= 1
            else:
                self.counter = len(self.images) - 1

    def getImage(self):
        Log.l(inspect.currentframe(), "getImage")
        temp = self.images[self.counter]
        img = temp.file
        Log.d(inspect.currentframe(), "image: " + str(img))
        return img
