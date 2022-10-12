import inspect
import os

from utils import log


class Model(object):

    path = "/home/jacky/Bilder/"

    files = []

    for file in os.listdir(path):
        files.append(path + file)
    log.l(inspect.currentframe(), "created image file list")

