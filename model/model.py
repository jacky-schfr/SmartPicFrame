import inspect
import os
import shutil

from utils import log


class Model(object):

    path = "/home/jacky/Bilder/"

    images = []

    for file in os.listdir(path):
        images.append('images/' + file)
        if os.path.exists('images/'+file):
            log.l(inspect.currentframe(), "no new image")
            continue
        else:
            # use Json file instead of list to gave propper data. ???
            # or picture/ image class
            shutil.copy(os.path.join(path, file), 'images')
            log.l(inspect.currentframe(), "new image added")

    print(images)



