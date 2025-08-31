# Class for a frame containing a single TS comp team

import tkinter as tk
from tkinter.font import Font as tkFont
from frames.TeamHeroFrame import TeamHeroFrame
from frames.ExtraTeamFrame import ExtraTeamFrame

class TeamFrame(tk.Frame):
    def __init__(self, master, number, has_extra=False):
        super().__init__(master, bd=1, relief='solid', bg=master.cget('bg'))
        self.extraNumber = 2 if number == 1 else number

        # Initialize Children
        self.hero1 = TeamHeroFrame(self, 1)
        self.hero2 = TeamHeroFrame(self, 2)
        self.hero3 = TeamHeroFrame(self, 3)
        self.hero4 = TeamHeroFrame(self, 4)
        self.hero5 = TeamHeroFrame(self, 5)
        if has_extra: self.extraFrame = ExtraTeamFrame(self, self.extraNumber)

        # Lay them out in the grid
        self.hero1.grid(row=0, column=0, sticky='news')
        self.hero2.grid(row=1, column=0, sticky='news')
        self.hero3.grid(row=2, column=0, sticky='news')
        self.hero4.grid(row=3, column=0, sticky='news')
        self.hero5.grid(row=4, column=0, sticky='news')
        if has_extra: self.extraFrame.grid(row=5, column=0, sticky='news')
    # end def
# end class