# Frame class for the universal Clear, Save, and Discard buttons
import tkinter as tk
from tkinter.font import Font as tkFont

class CSDFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Debug items
        self.test = tk.Label(self, text="This is the CSD Frame")
        self.test.pack()
    # end def
    # TODO: Implement
#end class