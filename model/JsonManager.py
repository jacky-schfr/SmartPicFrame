import json
from collections import namedtuple
from dataclasses import dataclass

from model.FrameConfig import FrameConfig


def customConfigDecoder(configDict):
    return namedtuple('X', configDict.keys())(*configDict.values())


class JsonManager:
    def __init__(self):
        self.fc = FrameConfig()

    def readJsonFile(self):
        with open('frame_config.json', 'r') as openfile:
            json_object = json.loads(openfile.read(), object_hook=customConfigDecoder)
            self.fc.isFullScreen = json_object.isFullScreen
            self.fc.pictureTime = json_object.pictureTime

    def writeJsonFile(self):
        config = Config(self.fc.isFullScreen, self.fc.pictureTime)
        jsonConfig = json.dumps(config.__dict__)
        with open("frame_config.json", "w") as outfile:
            outfile.write(jsonConfig)


@dataclass
class Config:
    isFullScreen: bool
    pictureTime: int
