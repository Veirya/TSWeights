# Frame class for entering  Hero data
import tkinter as tk
from tkinter.font import Font as tkFont

class HeroDataFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=master.cget('bg'))
        
        # This is a test display
        self.test = tk.Label(self, text="This is the Hero Data Frame")
        self.test.pack()
        # TODO: Implement
    # end def

    # TODO: implement way to write values into the fields
# end class