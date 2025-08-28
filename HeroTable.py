# Class for storing and maintaining a table of Heroes
import pandas
from Hero import Hero

class HeroTable(pandas.DataFrame):
    COLS = [
        "Name",
        "Ice",
        "Fire",
        "Forest",
        "Fog",
        "Pure",
        "Total",
        "Class",
        "Role",
        "Prog",
        "Coll",
        "Notes"
    ]

    # HeroTables are just DataFrames with extra functions and hard-coded column labels
    def __init__(self, data=None, index=None, dtype=None, copy=None):
        super.__init__(data, index, HeroTable.COLS, dtype, copy)

    # Take a list of heroes that need to be added/updated and put them in the table
    def update(self, heroes):
        pass

    # Take a list of heroes that are to be deleted from the table and delete them
    def remove_heroes(self, heroes):
        pass

# Read an exported HeroTable .csv file in as a DataFrame, then transform to a HeroTable
def load_table(file):
    return HeroTable(pandas.read_csv(file).values)