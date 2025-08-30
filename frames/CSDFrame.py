# Frame class for the universal Clear, Save, and Discard buttons
import tkinter as tk
from tkinter.font import Font as tkFont

class CSDFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=master.cget('bg'))
        self.buttonFont = tkFont(size=16, weight="bold")

        # Initialize and organize buttons
        self.clearButton = tk.Button(
            self, bg='light gray', text="Clear",
            command=self.clear_data, height=2, width=10,
            font=self.buttonFont
        )
        self.saveButton = tk.Button(
            self, bg='lime green', text="Save",
            command=self.save_data, height=2, width=10,
            font=self.buttonFont
        )
        self.discardButton = tk.Button(
            self, bg='red', text="Discard",
            command=self.discard_data, height=2, width=10,
            font=self.buttonFont
        )
        self.clearButton.grid(row=0, column=0, padx=5, pady=0, sticky="se")
        self.saveButton.grid(row=0, column=1, padx=5, pady=0, sticky="se")
        self.discardButton.grid(row=0, column=2, padx=5, pady=0, sticky="se")  
    # end def

    # Clear all of the fields out
    def clear_data(self):
        pass
    # end def

    # Commit the data in the fields to the core dict and initiate a table update
    def save_data(self):
        pass
    # end def

    # Close the window, discarding anything entered
    def discard_data(self):
        pass
    # end def
#end class