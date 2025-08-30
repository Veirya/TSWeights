# Class for the Window where Heroes will be entered

import tkinter as tk
from tkinter.font import Font as tkFont
from frames.HeroDataFrame import HeroDataFrame
from frames.CSDFrame import CSDFrame

class HeroWindow(tk.Toplevel):
    def __init__(self, master):
        self.bg = master.cget('bg')
        super().__init__(master, bg=self.bg)

        # Modal setup
        self.transient(master)
        self.title("Enter Hero Data")
        self.grab_set()

        # Setup the children
        self.enterHeroFrame = HeroDataFrame(self)
        self.csdFrame = CSDFrame(self)
        self.line = tk.Frame(self, bg=self.bg, height=2, bd=2, relief=tk.SOLID)
        self.enterHeroFrame.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.line.grid(row=1, column=0, padx=0, pady=0, sticky='news')
        self.csdFrame.grid(row=2, column=0, padx=5, pady=5, sticky="se")
    # end def

    # Have the HeroDataFrame clear the fields to the defaults.
    def clear_data(self):
        self.enterHeroFrame.clear_data()
    # end def

    # Request the data from the HeroDataFrame. Do nothing if it returns False.
    def save_data(self):
        heroData = self.enterHeroFrame.fetch_data()
        if not heroData: return
        # TODO: walk up to the App and call it's save_hero function
        print(heroData.to_row())
        self.destroy()
    # end def
# end class