# Class for entering an entire TS comp into the database

import tkinter as tk
from tkinter import ttk
from tkinter.font import Font as tkFont
from frames.CSDFrame import CSDFrame
from frames.TeamFrame import TeamFrame
from Hero import Hero

class TSWindow(tk.Toplevel):
    def __init__(self, master):
        self.bg = master.cget('bg')
        super().__init__(master, bg=self.bg)
        self.lblFont = tkFont(size=20, weight='bold')
        self.descVar = tk.StringVar(value="Enter the heroes for each team in the specified TS debuff comp.\nSubs are optional.")

        # Modal setup
        self.transient(master)
        self.title("Enter TS Comp")
        self.grab_set()

        # Setup the children
        self.typeFrame = tk.Frame(self, bd=1, relief='solid', bg=self.bg)
        self.typeLbl = tk.Label(self.typeFrame, text="TS Debuff:", height=2, font=self.lblFont, bg=self.bg)
        self.typeField = ttk.Combobox(self.typeFrame, height=1, values=list(Hero.WEIGHT_MAP.keys()), font=tkFont(size=18))
        self.descLbl = tk.Label(self, height=1, textvariable=self.descVar, font=self.lblFont, bg=self.bg)
        self.team1Lbl = tk.Label(self, height=1, text="Team 1", font=self.lblFont, bg=self.bg)
        self.team2Lbl = tk.Label(self, height=1, text="Team 2", font=self.lblFont, bg=self.bg)
        self.team3Lbl = tk.Label(self, height=1, text="Team 3", font=self.lblFont, bg=self.bg)
        self.team4Lbl = tk.Label(self, height=1, text="Team 4", font=self.lblFont, bg=self.bg)
        self.team1 = TeamFrame(self, 1, has_extra=True)
        self.team2 = TeamFrame(self, 2, has_extra=True)
        self.team3 = TeamFrame(self, 3, has_extra=True)
        self.team4 = TeamFrame(self, 4, has_extra=True)
        self.team5Lbl = tk.Label(self, height=1, text="Team 5", font=self.lblFont, bg=self.bg)
        self.team6Lbl = tk.Label(self, height=1, text="Team 6", font=self.lblFont, bg=self.bg)
        self.team7Lbl = tk.Label(self, height=1, text="Team 7", font=self.lblFont, bg=self.bg)
        self.team5 = TeamFrame(self, 5)
        self.team6 = TeamFrame(self, 6)
        self.team7 = TeamFrame(self, 7)
        self.csdFrame = CSDFrame(self)

        self.teamFrames = [self.team1, self.team2, self.team3, self.team4, self.team5, self.team6, self.team7]

        # Setup the grid
        # Row 0
        self.typeFrame.grid(row=0, column=0, sticky='nes')
        self.typeLbl.grid(row=0, column=0, padx=1, pady=2, sticky='nes')
        self.typeField.grid(row=0, column=1, padx=1, pady=2, sticky='nes')
        self.descLbl.grid(row=0, column=1, columnspan=3, sticky='news')
        # Row 1
        self.team1Lbl.grid(row=1, column=0, padx=2, pady=2, sticky='news')
        self.team2Lbl.grid(row=1, column=1, padx=2, pady=2, sticky='news')
        self.team3Lbl.grid(row=1, column=2, padx=2, pady=2, sticky='news')
        self.team4Lbl.grid(row=1, column=3, padx=2, pady=2, sticky='news')
        # Row 2
        self.team1.grid(row=2, column=0, sticky='news')
        self.team2.grid(row=2, column=1, sticky='news')
        self.team3.grid(row=2, column=2, sticky='news')
        self.team4.grid(row=2, column=3, sticky='news')
        # Row 3
        self.team5Lbl.grid(row=3, column=0, padx=2, pady=2, sticky='news')
        self.team6Lbl.grid(row=3, column=1, padx=2, pady=2, sticky='news')
        self.team7Lbl.grid(row=3, column=2, padx=2, pady=2, sticky='news')
        # Row 4
        self.team5.grid(row=4, column=0, sticky='news')
        self.team6.grid(row=4, column=1, sticky='news')
        self.team7.grid(row=4, column=2, sticky='news')
        self.csdFrame.grid(row=4, column=3, padx=2, pady=2, sticky='ws')
    # end def

    # Have the frames clear their fields to the defaults.
    def clear_data(self):
        for frame in self.teamFrames: frame.clear_data()
    # end def

    # Request sets of hero names for each scoring bracket for the given frames through use
    # of a set. If one of them returns an error message instead of an empty string, highlight
    # the corresponding label red and abort, applying the error message to descVar. The final
    # tallies will be given to the table to perform an update.
    def save_data(self):
        # First, need to ensure a TS debuff was selected.
        debuff = self.typeField.get()
        if debuff == "":
            self.descVar.set("A TS Debuff must be selected before saving.")
            self.descLbl.configure(fg='red')
            self.typeLbl.configure(fg='red')
            return
        else: self.typeLbl.configure(fg='black') # No need to set desc back, it'll go away if it's all good
        # end if
        scores = self.__tally_scores(debuff)
        if not scores: return

        # Assuming the master of the window to be the HomeFrame, have the app save the scores
        self.master.master._tsw_app.save_ts(scores)
        self.destroy()
    # end def

    # Helper function for save_data, gets the scores for each hero in the comp
    def __tally_scores(self, debuff: str):
        scores = {"Debuff": debuff}

        # This could potentially be more modular, but ICBF
        # 7-point heroes
        currScore = 7 # TODO: Make this configurable?
        currHeroes = set()
        # Team 1
        if not self.__frame_fetch(currHeroes, self.team1, self.team1Lbl, "comp"): return False
        # Team 1 EX
        if not self.__frame_fetch(currHeroes, self.team1, self.team1Lbl, "extras"): return False
        # Team 2 EX
        if not self.__frame_fetch(currHeroes, self.team2, self.team2Lbl, "extras"): return False
        # Use of currScore here is only for if I make it configurable.
        for hero in currHeroes: scores[hero] = currScore

        # 6-point heroes
        # Extra teams are considered 1 tier above the final comps, max of 7
        currScore = 6
        currHeroes = set()
        # Team 2
        if not self.__frame_fetch(currHeroes, self.team2, self.team2Lbl, "comp"): return False
        # Team 3 EX
        if not self.__frame_fetch(currHeroes, self.team3, self.team3Lbl, "extras"): return False
        for hero in currHeroes: scores[hero] = max(currScore, scores.get(hero, 0))

        # 5-point heroes
        currScore = 5
        currHeroes = set()
        # Team 3
        if not self.__frame_fetch(currHeroes, self.team3, self.team3Lbl, "comp"): return False
        # Team 4 EX
        if not self.__frame_fetch(currHeroes, self.team4, self.team4Lbl, "extras"): return False
        # Team 1 Subs
        if not self.__frame_fetch(currHeroes, self.team1, self.team1Lbl, "subs"): return False
        # Team 1 EX Subs
        if not self.__frame_fetch(currHeroes, self.team1, self.team1Lbl, "exsubs"): return False
        # Team 2 EX Subs
        if not self.__frame_fetch(currHeroes, self.team2, self.team2Lbl, "exsubs"): return False
        for hero in currHeroes: scores[hero] = max(currScore, scores.get(hero, 0))

        # 4-point heroes
        currScore = 4
        currHeroes = set()
        # Team 4
        if not self.__frame_fetch(currHeroes, self.team4, self.team4Lbl, "comp"): return False
        # Team 2 Subs
        if not self.__frame_fetch(currHeroes, self.team2, self.team2Lbl, "subs"): return False
        # Team 3 EX Subs
        if not self.__frame_fetch(currHeroes, self.team3, self.team3Lbl, "exsubs"): return False
        for hero in currHeroes: scores[hero] = max(currScore, scores.get(hero, 0))

        # 3-point heroes
        currScore = 3
        currHeroes = set()
        # Team 5
        if not self.__frame_fetch(currHeroes, self.team5, self.team5Lbl, "comp"): return False
        # Team 3 Subs
        if not self.__frame_fetch(currHeroes, self.team3, self.team3Lbl, "subs"): return False
        # Team 4 EX Subs
        if not self.__frame_fetch(currHeroes, self.team4, self.team4Lbl, "exsubs"): return False
        for hero in currHeroes: scores[hero] = max(currScore, scores.get(hero, 0))

        # 2-point heroes
        currScore = 2
        currHeroes = set()
        # Team 6
        if not self.__frame_fetch(currHeroes, self.team6, self.team6Lbl, "comp"): return False
        # Team 4 Subs
        if not self.__frame_fetch(currHeroes, self.team4, self.team4Lbl, "subs"): return False
        for hero in currHeroes: scores[hero] = max(currScore, scores.get(hero, 0))

        # 1-point heroes
        currScore = 1
        currHeroes = set()
        # Team 7
        if not self.__frame_fetch(currHeroes, self.team7, self.team7Lbl, "comp"): return False
        # Team 4 Subs
        if not self.__frame_fetch(currHeroes, self.team4, self.team4Lbl, "subs"): return False
        # Team 5 Subs
        if not self.__frame_fetch(currHeroes, self.team5, self.team5Lbl, "subs"): return False
        # Team 6 Subs
        if not self.__frame_fetch(currHeroes, self.team6, self.team6Lbl, "comp"): return False
        # I was generous to Teams 5 & 6 (read: don't want to implement reduced sub slots)
        # But team 7 subs will not count or be checked.
        for hero in currHeroes: scores[hero] = max(currScore, scores.get(hero, 0))
        
        return scores
    # end def

    # Helper function for __tally_scores
    def __frame_fetch(self, heroSet: set, team: TeamFrame, teamLbl: tk.Label, fetchType: str):
        fetchMap = {
            "comp": team.fetch_heroes,
            "extras": team.fetch_extras,
            "subs": team.fetch_subs,
            "exsubs": team.fetch_extra_subs
        }
        err = fetchMap[fetchType](heroSet)
        if err:
            self.descVar.set(err)
            self.descLbl.configure(fg='red')
            teamLbl.configure(fg='red')
            return False
        else: teamLbl.configure(fg='black')
        # end if
        return True
# end class