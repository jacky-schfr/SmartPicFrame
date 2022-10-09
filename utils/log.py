import inspect
import pathlib
from types import FrameType
from termcolor import colored


def l(frame: FrameType, message):
    path = pathlib.PurePath(inspect.getframeinfo(frame).filename)
    frameInfo = path.name, inspect.getframeinfo(frame).lineno
    frameInfoFormatted = formatString(str(frameInfo), 50)
    print(colored(formatString("log", 10), "green"), colored(frameInfoFormatted, "green"), message)


def d(frame: FrameType, message):
    path = pathlib.PurePath(inspect.getframeinfo(frame).filename)
    frameInfo = path.name, inspect.getframeinfo(frame).lineno
    frameInfoFormatted = formatString(str(frameInfo), 50)
    print(colored(formatString("debug", 10), "blue"), colored(frameInfoFormatted, "blue"), message)


def w(frame: FrameType, message):
    path = pathlib.PurePath(inspect.getframeinfo(frame).filename)
    frameInfo = path.name, inspect.getframeinfo(frame).lineno
    frameInfoFormatted = formatString(str(frameInfo), 50)
    print(colored(formatString("warning", 10), "yellow"), colored(frameInfoFormatted, "yellow"), message)


def formatString(name: str, lenght: int):
    for i in range(lenght - len(name)):
        name += " "
    return name
