import inspect

from controller.controller import Controller
from utils import log
from playground.fullScreenMode import fullScreenMode


if __name__ == "__main__":
    c = Controller()
    log.l(inspect.currentframe(), "init main")
