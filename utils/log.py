import inspect
import pathlib
from datetime import datetime
from types import FrameType
from termcolor import colored


"""
Message Log Class

:method l - log
:method d - debug
:method w - warning
"""


def l(frame: FrameType, message):
    frameInfoFormatted = formatFrame(frame)
    print(getTimeStamp(), "\t", colored(formatString("log", 10), "green"), colored(frameInfoFormatted, "green"), message)


def d(frame: FrameType, message):
    frameInfoFormatted = formatFrame(frame)
    print(getTimeStamp(), "\t", colored(formatString("debug", 10), "blue"), colored(frameInfoFormatted, "blue"), message)


def w(frame: FrameType, message):
    frameInfoFormatted = formatFrame(frame)
    print(getTimeStamp(), "\t", colored(formatString("warning", 10), "yellow"), colored(frameInfoFormatted, "yellow"), message)


def formatFrame(frame: FrameType):
    path = pathlib.PurePath(inspect.getframeinfo(frame).filename)
    frameInfo = path.name, inspect.getframeinfo(frame).lineno
    frameInfoFormatted = formatString(str(frameInfo), 50)
    return frameInfoFormatted


def formatString(name: str, lenght: int):
    for i in range(lenght - len(name)):
        name += " "
    return name


def getTimeStamp():
    current_time = datetime.now()
    time_stamp = current_time.timestamp()
    date_time = datetime.fromtimestamp(time_stamp)
    return date_time
