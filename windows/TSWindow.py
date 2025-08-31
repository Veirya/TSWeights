# Class for entering an entire TS comp into the database

import tkinter as tk
from tkinter import ttk
from tkinter.font import Font as tkFont
from frames.CSDFrame import CSDFrame
from frames.TeamFrame import TeamFrame
from Hero import Hero

class TSWindow(tk.Toplevel):
    def __init__(self, master):
        self.bg = master.cget('bg')
        super().__init__(master, bg=self.bg)
        self.lblFont = tkFont(size=20, weight='bold')
        self.descVar = tk.StringVar(value="Enter the heroes for each team in the specified TS debuff comp.\nSubs are optional.")

        # Modal setup
        self.transient(master)
        self.title("Enter TS Comp")
        self.grab_set()

        # Setup the children
        self.typeFrame = tk.Frame(self, bd=1, relief='solid', bg=self.bg)
        self.typeLbl = tk.Label(self.typeFrame, text="TS Debuff:", height=2, font=self.lblFont, bg=self.bg)
        self.typeField = ttk.Combobox(self.typeFrame, height=1, values=list(Hero.WEIGHT_MAP.keys()), font=tkFont(size=18))
        self.descLbl = tk.Label(self, height=1, textvariable=self.descVar, font=self.lblFont, bg=self.bg)
        self.team1Lbl = tk.Label(self, height=1, text="Team 1", font=self.lblFont, bg=self.bg)
        self.team2Lbl = tk.Label(self, height=1, text="Team 2", font=self.lblFont, bg=self.bg)
        self.team3Lbl = tk.Label(self, height=1, text="Team 3", font=self.lblFont, bg=self.bg)
        self.team4Lbl = tk.Label(self, height=1, text="Team 4", font=self.lblFont, bg=self.bg)
        self.team1 = TeamFrame(self, 1, has_extra=True)
        self.team2 = TeamFrame(self, 2, has_extra=True)
        self.team3 = TeamFrame(self, 3, has_extra=True)
        self.team4 = TeamFrame(self, 4, has_extra=True)
        self.team5Lbl = tk.Label(self, height=1, text="Team 5", font=self.lblFont, bg=self.bg)
        self.team6Lbl = tk.Label(self, height=1, text="Team 6", font=self.lblFont, bg=self.bg)
        self.team7Lbl = tk.Label(self, height=1, text="Team 7", font=self.lblFont, bg=self.bg)
        self.team5 = TeamFrame(self, 5)
        self.team6 = TeamFrame(self, 6)
        self.team7 = TeamFrame(self, 7)
        self.csdFrame = CSDFrame(self)

        # Setup the grid
        # Row 0
        self.typeFrame.grid(row=0, column=0, sticky='nes')
        self.typeLbl.grid(row=0, column=0, padx=1, pady=2, sticky='nes')
        self.typeField.grid(row=0, column=1, padx=1, pady=2, sticky='nes')
        self.descLbl.grid(row=0, column=1, columnspan=3, sticky='news')
        # Row 1
        self.team1Lbl.grid(row=1, column=0, padx=2, pady=2, sticky='news')
        self.team2Lbl.grid(row=1, column=1, padx=2, pady=2, sticky='news')
        self.team3Lbl.grid(row=1, column=2, padx=2, pady=2, sticky='news')
        self.team4Lbl.grid(row=1, column=3, padx=2, pady=2, sticky='news')
        # Row 2
        self.team1.grid(row=2, column=0, sticky='news')
        self.team2.grid(row=2, column=1, sticky='news')
        self.team3.grid(row=2, column=2, sticky='news')
        self.team4.grid(row=2, column=3, sticky='news')
        # Row 3
        self.team5Lbl.grid(row=3, column=0, padx=2, pady=2, sticky='news')
        self.team6Lbl.grid(row=3, column=1, padx=2, pady=2, sticky='news')
        self.team7Lbl.grid(row=3, column=2, padx=2, pady=2, sticky='news')
        # Row 4
        self.team5.grid(row=4, column=0, sticky='news')
        self.team6.grid(row=4, column=1, sticky='news')
        self.team7.grid(row=4, column=2, sticky='news')
        self.csdFrame.grid(row=4, column=3, sticky='ws')

        # Setup the tab order
    # end def

    # Have the HeroDataFrame clear the fields to the defaults.
    def clear_data(self):
        pass
    # end def

    # Request the data from the HeroDataFrame. Do nothing if it returns False.
    def save_data(self):
        pass
    # end def
# end class