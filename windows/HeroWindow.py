# Class for the Window where Heroes will be entered

import tkinter as tk
from tkinter.font import Font as tkFont
from frames.HeroDataFrame import HeroDataFrame
from frames.CSDFrame import CSDFrame

class HeroWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master, bg=master.cget('bg'))

        # Modal setup
        self.transient(master)
        self.grab_set()

        # Setup the children
        self.enterHeroFrame = HeroDataFrame(self)
        self.csdFrame = CSDFrame(self)
        self.enterHeroFrame.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.csdFrame.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    # end def
# end class