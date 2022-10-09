import inspect
from tkinter import *

from utils import log


class fullScreenMode:

    def __init__(self):
        log.l(inspect.currentframe(), "init window")

        self.window = Tk(className="SmartPicFrame")
        self.window.geometry("1280x768")

        self.toggle_btn = Button(text="FullScreen-Mode", width=12, relief="raised", command=lambda: self.toggle(self.toggle_btn))
        self.toggle_btn.pack(pady=5)

        log.w(inspect.currentframe(), "not good")
        self.window.mainloop()

    def toggle(self, toggle: Button):
        if toggle.config('relief')[-1] == 'sunken':
            log.d(inspect.currentframe(), "full screen mode: False")

            toggle.config(relief="raised")
            self.window.attributes("-fullscreen", False)
        else:
            log.d(inspect.currentframe(), "full screen mode: True")

            toggle.config(relief="sunken")
            self.window.attributes("-fullscreen", True)
