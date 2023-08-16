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

        self.updateImageList()

    def updateImageList(self):
        self.images = self.createImageList()

    def createImageList(self):
        tempImages = []
        if os.path.exists(self.fc.path) and len(os.listdir(self.fc.path)) > 0:
            Log.l(inspect.currentframe(), "pictures in dir.: " + str(len(os.listdir(self.fc.path))))
            for file in os.listdir(self.fc.path):
                img = Picture(file)
                tempImages.append(img)
        return tempImages

    def setCounterValue(self, direction="default"):
        if direction == "r":
            if self.counter < len(self.images) - 1:
                self.counter += 1
            else:
                self.counter = 0
        elif direction == "l":
            if self.counter > 0:
                self.counter -= 1
            else:
                self.counter = len(self.images) - 1
        elif direction == "default":
            self.counter = 1

    def getImageFromList(self):
        if len(self.images) == 0:
            return 'defaultImage/defaultImg.png'
        else:
            temp = self.images[self.counter]
            return self.fc.path + temp.file

    def getImage(self, direction):
        Log.l(inspect.currentframe(), "getImage")

        # Set the counter for the next picture
        self.setCounterValue(direction)

        img = self.getImageFromList()

        # Check if picture exists
        if not os.path.exists(img):
            Log.d(inspect.currentframe(), "Picture not exist, reload images")
            self.setCounterValue()
            self.updateImageList()
            img = self.getImageFromList()

        Log.d(inspect.currentframe(), "image: " + str(img))
        return img

    def checkListUpdate(self):
        refImageList = self.createImageList()
        result = False
        if len(self.images) == len(refImageList) and not len(self.images) == 0:
            for picture in self.images:
                for refPicture in refImageList:
                    if picture.file == refPicture.file:
                        result = True
                        break
                    else:
                        result = False
                if not result:
                    break
            return result
        else:
            return result
