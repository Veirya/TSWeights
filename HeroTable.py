# Class for storing and maintaining a table of Heroes
# It's possible that even by the end this class is superficial.
# I will convert it to a regular DataFrame if that's the case,
# because (unsurprisingly) DF's are very good natively and do everything
# that I was going to do manually
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
        self.set_index("Name", inplace=True)
    # end def

    # Take a list of heroes that need to be added/updated and put them in the table
    def update(self, heroes):
        pass # TODO: This may be pointless
    # end def

    # Take a list of heroes that are to be deleted from the table and delete them
    def remove_heroes(self, heroes):
        pass # TODO: This may also be pointless
    # end def
# end class

# Read an exported HeroTable .csv file in as a DataFrame, then transform to a HeroTable
def load_table(file):
    return HeroTable(data=read_csv(file).values)
# end def