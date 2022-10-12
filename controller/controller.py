import inspect

from model.model import Model
from utils import log
from view.view import View


class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View(self.run())
        self.view.mainloop()

        log.l(inspect.currentframe(), "init controller")

    def run(self):
        i = 1
        return self.model.files[i]

