import inspect
import os
import shutil
from model.Picture import Picture

from utils import Log


class Model(object):

    #path = "/home/jacky/Bilder/"
    path = r"C:\Users\marce\Pictures\SmartPicFrameImages"

    images = []

    for file in os.listdir(path):
        img = Picture('images/' + file)
        images.append(img)
        if os.path.exists('images/'+file):
            Log.l(inspect.currentframe(), "no new image")
            continue
        else:
            # use Json file instead of list to gave propper data. ???
            # or picture/ image class
            shutil.copy(os.path.join(path, file), 'images')
            Log.l(inspect.currentframe(), "new image added")

    Log.d(inspect.currentframe(), "images: " + str(images))
