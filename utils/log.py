import inspect
import pathlib
from types import FrameType
from termcolor import colored


def d(frame: FrameType, message):
    path = pathlib.PurePath(inspect.getframeinfo(frame).filename)
    frameInfo = path.name, inspect.getframeinfo(frame).lineno
    print(colored("debug\t", "blue"), message, "\t", colored(frameInfo, "blue"))


def w(frame: FrameType, message):
    path = pathlib.PurePath(inspect.getframeinfo(frame).filename)
    frameInfo = path.name, inspect.getframeinfo(frame).lineno
    print(colored("warning\t", "yellow"), message, "\t", colored(frameInfo, "yellow"))
