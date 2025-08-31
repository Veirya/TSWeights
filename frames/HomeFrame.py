# Frame for the home window of the tsweights app
import tkinter as tk
from tkinter.font import Font as tkFont
from windows.HeroWindow import HeroWindow
from windows.TSWindow import TSWindow

class HomeFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=master.cget('bg'))
        self.buttonFont = tkFont(size=20, weight='bold')

        # Initialize the buttons
        self.addHeroBtn = tk.Button(
            self, bg='light gray', text="Enter Hero",
            command=self._open_enterhero, height=2,
            font= self.buttonFont
        )
        self.editHeroBtn = tk.Button(
            self, bg='light gray', text="Edit Hero",
            command=self._open_edithero, height=2,
            font= self.buttonFont
        )
        self.addTSBtn = tk.Button(
            self, bg='light gray', text="Enter TS Comps",
            command=self._open_enterts, height=2,
            font= self.buttonFont
        )

        # Then pack them
        self.addHeroBtn.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.editHeroBtn.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.addTSBtn.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
    # end def

    # Button Functions. Simple enough to not be one, but are in case of expansion.
    # Open the modal Hero window
    def _open_enterhero(self):
        HeroWindow(self)
    # end def

    # Open the modal Enter TS Comp window
    def _open_enterts(self):
        TSWindow(self)
    # end def

    # Open the modal Edit Hero window
    def _open_edithero(self):
        pass
    # end def

# end class