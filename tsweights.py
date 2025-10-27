# Giovanni "Veirya" Oliver, 2025
# GUI For Generating a Spreadsheet for my TS weights

import os
import tkinter as tk
from Hero import Hero
from HeroTable import HeroTable, load_table
from frames.HomeFrame import HomeFrame
from windows.HeroWindow import HeroWindow

class TSWeights:
    def __init__(self, master, save_file):
        self.master = master
        self.master._tsw_app = self  # Useful reference to have without making this a frame
        self.save_file = save_file

        # Check if a saved table exists, and if so, import it and it's heroes
        if os.path.exists(save_file):
            # This will be the basic flow
            print("Saved Table detected. Importing ...", end=" ")
            self.table = load_table(save_file)
            self.heroes = self._import_heroes(self.table)
            print("Success")
        # Otherwise, initialize a new table and hero dictionary
        else:
            print(f"Table \"{save_file}\" not found. Starting from scratch.")
            self.table = HeroTable()
            self.heroes = dict() # Thinking this might be pointless, the table is the same thing basically
            # The Hero class, however, is useful as an intermediary class and for its constants

        # Initialize the home TK frame in the master
        # The App could probably inherit from tk.Frame itself
        self.homeFrame = HomeFrame(self.master)
        self.homeFrame.pack()
    # end def

    # Take a HeroTable and generate a dict of Heroes based on the input
    def _import_heroes(self, table: HeroTable):
        heroDict = dict()
        for name in table.index:
            newHero = Hero(name)
            data = table.loc[name]
            newHero.weights = [data["Ice"], data["Fire"], data["Forest"], data["Fog"], data["Pure"]]
            newHero.totalWeight = data["Total"]
            newHero.heroClass = data["Class"]
            newHero.role = data["Role"]
            newHero.prog = data["Prog"]
            newHero.coll.stars, newHero.coll.type = data["Coll"].split(" ")
            heroDict[name] = newHero
        return heroDict
    # end def

    def save_hero(self, hero: Hero):
        self.heroes[hero.name] = hero
        self.table.loc[hero.name] = hero.to_row()
        self.table.to_csv(self.save_file)
    # end def

    def save_ts(self, scores):
        print(scores)
        # Get useful sets
        scoreNames = scores.keys()
        tableIndices = set(self.table.index.values)
        newHeroes = scoreNames - tableIndices
        modHeroes = scoreNames & tableIndices
        zeroHeroes = tableIndices - scoreNames

        # First, fill in the data for any new heroes
        for name in newHeroes: 
            if name == "Debuff": continue # Not a hero
            newHero = Hero(name)
            nhWindow = HeroWindow(self.homeFrame, newHero)
            nhWindow.wait_window() # Wait for the data to be entered
            newHero.weights[Hero.WEIGHT_MAP[scores["Debuff"]]] = scores[name]
            newHero.totalWeight = sum(newHero.weights)
            self.heroes[newHero.name] = newHero
            self.table.loc[newHero.name] = newHero.to_row()
        
        # Next, apply the score to pre-existing hero entries
        for name in modHeroes:
            self.heroes[name].weights[Hero.WEIGHT_MAP[scores["Debuff"]]] = scores[name]
            self.heroes[name].update_total()
            self.table.at[name, scores["Debuff"]] = scores[name]
            self.table.at[name, "Total"] = self.heroes[name].totalWeight

        # Then, zero out the scores for heroes not in the score list but are in the tables.
        for name in zeroHeroes:
            self.heroes[name].weights[Hero.WEIGHT_MAP[scores["Debuff"]]] = 0
            self.heroes[name].update_total()
            self.table.at[name, scores["Debuff"]] = 0
            self.table.at[name, "Total"] = self.heroes[name].totalWeight

        # Finally, save the table to a csv after the writes are all done.
        self.table.to_csv(self.save_file)
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