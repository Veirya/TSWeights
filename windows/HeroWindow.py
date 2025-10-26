# Class for the Window where Heroes will be entered

import tkinter as tk
from frames.HeroDataFrame import HeroDataFrame
from frames.NewHeroFrame import NewHeroFrame
from frames.CSDFrame import CSDFrame

class HeroWindow(tk.Toplevel):
    def __init__(self, master, hero=None):
        self.bg = master.cget('bg')
        super().__init__(master, bg=self.bg)

        # Modal setup
        self.transient(master)
        self.title("Enter Hero Data")
        self.grab_set()

        # Setup the children
        self.enterHeroFrame = NewHeroFrame(self, hero) if hero is not None else HeroDataFrame(self)
        self.csdFrame = CSDFrame(self)
        self.line = tk.Frame(self, bg=self.bg, height=2, bd=2, relief=tk.SOLID)
        self.enterHeroFrame.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.line.grid(row=1, column=0, padx=0, pady=0, sticky='news')
        self.csdFrame.grid(row=2, column=0, padx=5, pady=5, sticky="se")

        # Setup the tab order
        self.enterHeroFrame.lift()
        self.csdFrame.lift()
    # end def

    # Have the HeroDataFrame clear the fields to the defaults.
    def clear_data(self):
        self.enterHeroFrame.clear_data()
    # end def

    # Request the data from the HeroDataFrame. Do nothing if it returns False, only destroy if it is None.
    def save_data(self):
        heroData = self.enterHeroFrame.fetch_data()
        if heroData == False: return
        # To avoid a possible circular import, assume that the master is a HomeFrame
        # whose master is the app
        if heroData is not None: self.master.master._tsw_app.save_hero(heroData)
        self.destroy()
    # end def
# end class