from tkinter import *


class fullScreenMode:

    def __init__(self):
        print("init window")

        self.window = Tk(className="SmartPicFrame")
        self.window.geometry("1280x768")

        self.toggle_btn = Button(text="FullScreen-Mode", width=12, relief="raised", command=lambda: self.toggle(self.toggle_btn))
        self.toggle_btn.pack(pady=5)

        self.window.mainloop()

    def toggle(self, toggle: Button):
        if toggle.config('relief')[-1] == 'sunken':
            toggle.config(relief="raised")
            self.window.attributes("-fullscreen", False)
        else:
            toggle.config(relief="sunken")
            self.window.attributes("-fullscreen", True)
