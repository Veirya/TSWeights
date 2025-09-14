# Class for a frame containing a single TS comp team

import tkinter as tk
from tkinter.font import Font as tkFont
from frames.TeamHeroFrame import TeamHeroFrame
from frames.ExtraTeamFrame import ExtraTeamFrame
from Hero import Hero

class TeamFrame(tk.Frame):
    def __init__(self, master, number, has_extra=False):
        super().__init__(master, bd=1, relief='solid', bg=master.cget('bg'))
        self.extraNumber = 2 if number == 1 else number
        self.has_extra = has_extra

        # Initialize Children
        self.hero1 = TeamHeroFrame(self, 1)
        self.hero2 = TeamHeroFrame(self, 2)
        self.hero3 = TeamHeroFrame(self, 3)
        self.hero4 = TeamHeroFrame(self, 4)
        self.hero5 = TeamHeroFrame(self, 5)
        if has_extra: self.extraFrame = ExtraTeamFrame(self, self.extraNumber)

        # Lay them out in the grid
        self.hero1.grid(row=0, column=0, sticky='news')
        self.hero2.grid(row=1, column=0, sticky='news')
        self.hero3.grid(row=2, column=0, sticky='news')
        self.hero4.grid(row=3, column=0, sticky='news')
        self.hero5.grid(row=4, column=0, sticky='news')
        if has_extra: self.extraFrame.grid(row=5, column=0, sticky='news')
    # end def

    # Have the children clear themselves
    def clear_data(self):
        self.hero1.clear_data()
        self.hero2.clear_data()
        self.hero3.clear_data()
        self.hero4.clear_data()
        self.hero5.clear_data()
        if self.has_extra: self.extraFrame.clear_data()
    # end def

    # Add heroes within the main section of the frame to the given set
    # Returns an empty string if no problems, but if a hero name isn't
    # in the list or has already been added, return an error describing it
    # and make the labels red.
    def fetch_heroes(self, heroSet: set):
        checkedHeroes = set()
        for hero in [self.hero1, self.hero2, self.hero3, self.hero4, self.hero5]:
            name = hero.nameField.get().title()
            if name.lower() not in Hero.HERO_NAMES:
                hero.idLbl.configure(fg='red')
                hero.nameLbl.configure(fg='red')
                return f"Hero '{name}' not recognized. Please check the spelling."
            elif name in checkedHeroes:
                hero.idLbl.configure(fg='red')
                hero.nameLbl.configure(fg='red')
                return f"Hero '{name}' is listed more than once in a comp.\nComps need unique heroes."
            else:
                hero.idLbl.configure(fg='black')
                hero.nameLbl.configure(fg='black')
                checkedHeroes.add(name)
                heroSet.add(name)
                # end if
        # end for
        return ""
    # end def

    # Similar to fetch_heroes, but for the ExtraTeamFrame, which handles things internally.
    def fetch_extras(self, heroSet: set):
        if not self.has_extra: raise ValueError("This team does not have an associated extra team.")
        return self.extraFrame.fetch_heroes(heroSet)
    # end def

    # Similar to fetch_heroes, but get the subs instead of the main comp, but now
    # blanks are acceptable and uniqueness only matters within each HeroFrame.
    def fetch_subs(self, heroSet: set):
        for hero in [self.hero1, self.hero2, self.hero3, self.hero4, self.hero5]:
            currCheck = set()
            for sub in [hero.sub1Field, hero.sub2Field, hero.sub3Field]:
                name = sub.get().title()
                if name == "": continue
                elif name.lower() not in Hero.HERO_NAMES:
                    hero.idLbl.configure(fg='red')
                    hero.subLbl.configure(fg='red')
                    return f"Hero '{name}' not recognized. Please check the spelling."
                elif name in currCheck:
                    hero.idLbl.configure(fg='red')
                    hero.subLbl.configure(fg='red')
                    return f"Hero '{name}' is listed more than once as a sub\nfor a single hero."
                else:
                    hero.idLbl.configure(fg='black')
                    hero.subLbl.configure(fg='black')
                    currCheck.add(name)
                    heroSet.add(name)
                # end if
            # end for
        # end for
        return ""
    # end def

    # Similar to fetch_extras, but looking for the subs instead. The ExtraTeamFrame handles it.
    def fetch_extra_subs(self, heroSet: set):
        if not self.has_extra: raise ValueError("This team does not have an associated extra team.")
        return self.extraFrame.fetch_subs(heroSet)
    # end def
# end class