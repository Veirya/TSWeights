# Class for a frame containing the extra team fields

import tkinter as tk
from tkinter.font import Font as tkFont

class ExtraTeamFrame(tk.Frame):
    def __init__(self, master, number: int):
        self.bg = master.cget('bg')
        super().__init__(master, bd=1, relief='solid', bg=self.bg)
        self.fieldFont = tkFont(size=14)

        # Initialize the children
        self.idLbl = tk.Label(self, text=f"{number} Teams Heroes", height=1, font=tkFont(size=18, weight='bold'), bg=self.bg)
        self.hero1Field = tk.Entry(self, width=10, font=self.fieldFont)
        self.hero2Field = tk.Entry(self, width=10, font=self.fieldFont)
        self.hero3Field = tk.Entry(self, width=10, font=self.fieldFont)
        self.hero4Field = tk.Entry(self, width=10, font=self.fieldFont)
        self.hero5Field = tk.Entry(self, width=10, font=self.fieldFont)
        self.subFrame = tk.Frame(self, bd=1, relief='solid', bg=self.bg)
        self.subLbl = tk.Label(self.subFrame, text="Top Subs", height=1, font=tkFont(size=14, weight='bold'), bg=self.bg)
        self.sub1Field = tk.Entry(self.subFrame, width=10, font=self.fieldFont)
        self.sub2Field = tk.Entry(self.subFrame, width=10, font=self.fieldFont)
        self.sub3Field = tk.Entry(self.subFrame, width=10, font=self.fieldFont)

        # Lay them out in the grid
        self.idLbl.grid(row=0, column=0, columnspan=3, padx=2, pady=2, sticky='nw')
        self.hero1Field.grid(row=1, column=0, padx=2, pady=2, sticky='news')
        self.hero2Field.grid(row=1, column=1, padx=2, pady=2, sticky='news')
        self.hero3Field.grid(row=1, column=2, padx=2, pady=2, sticky='news')
        self.hero4Field.grid(row=2, column=0, padx=2, pady=2, sticky='news')
        self.hero5Field.grid(row=2, column=1, padx=2, pady=2, sticky='news')
        self.subFrame.grid(row=0, column=3, rowspan=3)
        self.subLbl.grid(row=0, column=0, padx=2, pady=2, sticky='news')
        self.sub1Field.grid(row=1, column=0, padx=2, pady=2, sticky='news')
        self.sub2Field.grid(row=2, column=0, padx=2, pady=2, sticky='news')
        self.sub3Field.grid(row=3, column=0, padx=2, pady=2, sticky='news')
    # end def
# end class