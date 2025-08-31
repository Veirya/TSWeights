# Class for a frame containing the entry fields for a single hero in a team

import tkinter as tk
from tkinter.font import Font as tkFont

class TeamHeroFrame(tk.Frame):

    def __init__(self, master, number: int):
        self.bg = master.cget('bg')
        super().__init__(master, bd=1, relief='solid', bg=self.bg)
        self.lblFont = tkFont(size=14, weight='bold')
        self.slashFont = tkFont(size=22, weight='bold')
        self.fieldFont = tkFont(size=14)

        # Initialize the children
        self.idLbl = tk.Label(self, text=f"Hero {number}", font=tkFont(size=18, weight='bold'), height=1, bg=self.bg)
        self.nameLbl = tk.Label(self, text="Name", font=self.lblFont, height=1, bg=self.bg)
        self.nameField = tk.Entry(self, width=10, font=self.fieldFont)
        self.subLbl = tk.Label(self, text="Subs", font=self.lblFont, height=1, bg=self.bg)
        self.sub1Field = tk.Entry(self, width=10, font=self.fieldFont)
        self.slash1Lbl = tk.Label(self, text="/", font=self.slashFont, height=1, bg=self.bg)
        self.sub2Field = tk.Entry(self, width=10, font=self.fieldFont)
        self.slash2Lbl = tk.Label(self, text="/", font=self.slashFont, height=1, bg=self.bg)
        self.sub3Field = tk.Entry(self, width=10, font=self.fieldFont)

        # Lay them out in the grid
        self.idLbl.grid(row=0, column=0, padx=2, pady=2, sticky='nw')
        self.nameLbl.grid(row=0, column=1, columnspan=2, padx=2, pady=2, sticky='nes')
        self.nameField.grid(row=0, column=3, columnspan=3, padx=1, pady=2, sticky='news')
        self.subLbl.grid(row=1, column=0, padx=2, pady=2, sticky='nes')
        self.sub1Field.grid(row=1, column=1, padx=2, pady=2, sticky='news')
        self.slash1Lbl.grid(row=1, column=2, padx=2, pady=2, sticky='news')
        self.sub2Field.grid(row=1, column=3, padx=2, pady=2, sticky='news')
        self.slash2Lbl.grid(row=1, column=4, padx=2, pady=2, sticky='news')
        self.sub3Field.grid(row=1, column=5, padx=2, pady=2, sticky='news')
    # end def
# end class