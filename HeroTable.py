# Class for storing and maintaining a table of Heroes
from pandas import DataFrame, read_csv
from Hero import Hero

class HeroTable(DataFrame):
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
        super().__init__(data, index, HeroTable.COLS, dtype, copy)
    # end def

    # Take a list of heroes that need to be added/updated and put them in the table
    def update(self, heroes):
        pass
    # end def

    # Take a list of heroes that are to be deleted from the table and delete them
    def remove_heroes(self, heroes):
        pass
    # end def
# end class

# Read an exported HeroTable .csv file in as a DataFrame, then transform to a HeroTable
def load_table(file):
    return HeroTable(read_csv(file).values)
# end def