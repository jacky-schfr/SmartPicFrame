import inspect
import pathlib
from datetime import datetime
from types import FrameType
from termcolor import colored


""" Message Log Class

    :method l - log
    :method d - debug
    :method w - warning """


def l(frame: FrameType, message):
    print(getTimeStamp(), "\t", colored(formatString("log", 10), "green"), formatString(getLink(frame), 70), message)


def d(frame: FrameType, message):
    print(getTimeStamp(), "\t", colored(formatString("debug", 10), "blue"), formatString(getLink(frame), 70), message)


def w(frame: FrameType, message):
    print(getTimeStamp(), "\t", colored(formatString("warning", 10), "yellow"), formatString(getLink(frame), 70), message)


def getLink(frame: FrameType):
    path = pathlib.PurePath(inspect.getframeinfo(frame).filename)
    line = inspect.getframeinfo(frame).lineno
    parts = path.parts

    string = f'(File "{parts[-2] + "/" + parts[-1]}", line {max(line, 1)})'
    return string


def formatString(name: str, lenght: int):
    for i in range(lenght - len(name)):
        name += " "
    return name


def getTimeStamp():
    current_time = datetime.now()
    time_stamp = current_time.timestamp()
    date_time = datetime.fromtimestamp(time_stamp)
    return date_time
