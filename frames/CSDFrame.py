# Frame class for the universal Clear, Save, and Discard buttons
# Frames containing these buttons are assumed to be children in a tree
# of Tk classes leading to a Toplevel-based class that implements
# clear_data and save_data functions.
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

    # Clear all of the data fields
    def clear_data(self):
        tl = self.__find_tl()
        tl.clear_data()
    # end def

    # Commit the data in the fields to the core dict and initiate a table update
    def save_data(self):
        tl = self.__find_tl()
        tl.save_data()
    # end def

    # Close the window, discarding anything entered
    def discard_data(self):
        tl = self.__find_tl()
        tl.destroy()
    # end def

    # Work up the master tree until it finds a TopLevel-based class and return the reference.
    # If the root tk.Tk is found, raise TypeError.
    # This is used to allow the buttons to call window-specific Clear/Save functions or destroy it.
    def __find_tl(self):
        tl = self.master
        while not (issubclass(type(tl), tk.Toplevel) or type(tl) is tk.Toplevel):
            if type(tl) == tk.Tk:
                raise TypeError("Unexpectedly found the root while climbing the tree.")
            # end if
            tl = tl.master
        # end while
        return tl
    # end def
#end class