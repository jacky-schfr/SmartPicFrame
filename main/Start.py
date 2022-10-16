import inspect

from controller.Controller import Controller
from utils import Log


if __name__ == "__main__":
    Log.l(inspect.currentframe(), "init main")
    c = Controller()

