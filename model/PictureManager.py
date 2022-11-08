import inspect
import os
import platform
from model.Picture import Picture

from utils import Log


class Model(object):
    if platform.system() == "Windows":
        path = r"C:/Users/marce/Cookies/Desktop/DropboxDB/Dropbox/Synchronisierter Ordner/"  # Windows path
    else:
        path = "/home/jacky/Dropbox/Synchronisierter Ordner/"  # Linux path

    images = []

    if os.path.exists(path):
        for file in os.listdir(path):
            img = Picture(path + file)
            images.append(img)
        if not images:
            images.append(Picture('defaultImage/defaultImg.png'))
    else:
        images.append(Picture('defaultImage/defaultImg.png'))

    Log.d(inspect.currentframe(), "defaultImage: " + str(images))

    def getCounterValue(self, counter, param):
        if param == "r":
            if counter < len(self.images) - 1:
                counter += 1
            else:
                counter = 0
        else:
            if counter > 0:
                counter -= 1
            else:
                counter = len(self.images) - 1
        return counter
