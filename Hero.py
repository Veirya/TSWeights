# Structs for storing hero data
import json

class Hero:
    with open("heroNames.json", 'r') as f:
        HERO_NAMES = set([name.lower() for name in json.load(f)["Names"]])
    # end with

    PROG_VALUES = [
        "",
        "Done",
        "Good Enough",
        "In Progress",
        "Queued",
        "Nowhere Near",
    ]
    CLASSES = [
        "",
        "Support",
        "Mage",
        "Warrior",
        "Tank",
        "Ranger"
    ]
    WEIGHT_MAP = {
        "Ice": 0,
        "Fire": 1,
        "Forest": 2,
        "Fog": 3,
        "Pure": 4,
    }

    # Only take name to start so rest can be filled in after creation
    def __init__(self, name):
        self.name = name
        self.weights = [0]*5
        self.totalWeight = 0
        self.heroClass = ""
        self.role = ""
        self.prog = ""
        self.coll = Collection()
        self.notes = ""
    # end def

    def to_row(self):
        return self.weights + [self.totalWeight, self.heroClass, self.role, self.prog, str(self.coll), self.notes]
    # end def
# end class

class Collection:
    TYPES = sorted([
        "",
        "Zolrath",
        "Saurus",
        "Orthos",
        "Damian",
        "Athalia",
        "Tidus",
        "Mehira",
        "Oden",
        "Rowan",
        "Tasi",
        "Izold",
        "Anoki",
        "Thane",
        "Zaphrael",
        "Raine",
    ])
    STAR_VALUES = ["", "1*", "2*", "3*"]

    def __init(self):
        self.stars = ""
        self.type = ""
    # end def

    def __str__(self):
        return f"{self.stars} {self.type}"
    # end def
# end class