from PyQt5.QtWidgets import QApplication


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
        self.width = 1280
        self.height = 720

        self.desktop = QApplication.desktop()
        self.rect = self.desktop.screenGeometry()
        self.h = self.rect.height()
        self.w = self.rect.width()

        '''
        Timer configurations
        '''
        self.touchDurationTime = 4
        self.pictureTime = 3
        self.pause = False

        '''
        Touch config
        '''
        self.isTouch = False

    def updateConfig(self, pictureTime):
        self.pictureTime = pictureTime
