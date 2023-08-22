import platform


class FrameConfig(object):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(FrameConfig, cls).__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):
        if self.__initialized: return
        self.__initialized = True

        '''
        SmartPicFrame configurations
        '''
        self.isFullScreen = False
        self.isSemino = False

        self.width = 1280
        self.height = 720

        self.h = 0
        self.w = 0

        '''
        Directory config
        '''
        if platform.system() == "Windows":
            picturePath = r"C:/Users/marce/Desktop/Synchronisierter Ordner/"  # Windows path
        else:
            picturePath = "/home/jacky/Dropbox/Synchronisierter Ordner/"  # Linux path
        self.path = picturePath

        '''
        Timer configurations
        '''
        self.touchDurationTime = 7
        self.pictureTime = 600
        self.pause = False

        '''
        Touch config
        '''
        self.isTouch = False

        '''
        Message config
        '''
        self.showMessage = True
        self.msgHeight = 0

        self.lastUpdate = "WIP"

    def updateConfig(self, path, pictureTime):
        self.path = path
        self.pictureTime = pictureTime

    def toggleFullScreen(self, state):
        if state:
            self.isFullScreen = True
        else:
            self.isFullScreen = False

    def toggleSeminoMode(self):
        self.isSemino = not self.isSemino
