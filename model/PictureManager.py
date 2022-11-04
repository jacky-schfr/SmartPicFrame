import inspect
import os
import shutil
from model.Picture import Picture

from utils import Log


class Model(object):

    # path = "/home/jacky/Bilder/"
    path = r"C:\Users\marce\Pictures\SmartPicFrameImages"

    images = []

    if os.path.exists(path):
        for file in os.listdir(path):
            img = Picture('images/' + file)
            images.append(img)
            if os.path.exists('images/'+file):
                Log.l(inspect.currentframe(), "no new image")
                continue
            else:
                shutil.copy(os.path.join(path, file), 'images')
                Log.l(inspect.currentframe(), "new image added")
    else:
        for file in os.listdir('images/'):
            img = Picture('images/'+file)
            images.append(img)

    Log.d(inspect.currentframe(), "images: " + str(images))

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

