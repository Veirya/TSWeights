# Giovanni "Veirya" Oliver, 2025
# GUI For Generating a Spreadsheet for my TS weights

import os
import tkinter as tk
from Hero import Hero, Collection
from HeroTable import HeroTable, load_table
from HomeFrame import HomeFrame

class TSWeights:
    def __init__(self, master, save_file):
        self.master = master
        self.save_file = save_file

        # Check if a saved table exists, and if so, import it and it's heroes
        if os.path.exists(save_file):
            raise NotImplementedError
            # This will be the basic flow
            print("Saved Table detected. Importing ...", end=" ")
            self.table = load_table(save_file)
            self.heroes = self._import_heroes(table)
            print("Success")
        # Otherwise, initialize a new table and hero dictionary
        else:
            print(f"Table \"{save_file}\" not found. Starting from scratch.")
            self.table = HeroTable()
            self.heroes = dict()

        # Initialize the home TK frame in the master
        # The App could probably be a tk Frame itself
        self.homeFrame = HomeFrame(self.master)
        self.homeFrame.pack()
    # end def

    # Take a HeroTable and generate a dict of Heroes based on the input
    def _import_heroes(table):
        # TODO: Implement
        return dict()
    # end def
# end class

if __name__ == "__main__":
    SAVE_FILE = "TS_Weights.csv"
    root = tk.Tk()
    root.title("TSWeights")
    root.configure(background='gray66')
    app = TSWeights(root, SAVE_FILE)
    root.mainloop()
# end if