import inspect

from utils import log
from playground.fullScreenMode import fullScreenMode

if __name__ == "__main__":
    log.l(inspect.currentframe(), "init main")

    fullScreenMode()
