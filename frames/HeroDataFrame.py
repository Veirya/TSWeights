# Frame class for entering  Hero data
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font as tkFont
from Hero import Hero, Collection

class HeroDataFrame(tk.Frame):
    def __init__(self, master):
        self.bg = master.cget('bg')
        super().__init__(master, bg=self.bg)
        self.sectionFont = tkFont(size=16, weight="bold")
        self.fieldFont = tkFont(size=14)
        self.columnconfigure(0, weight=0) # Base grid is 4x3, don't want col 0 to expand past the bare necessities
        
        # Organizational helper frames
        self.weightFrame = tk.Frame(self, bg=self.bg)
        self.suppFrame = tk.Frame(self, bg=self.bg)
        self.collFrame = tk.Frame(self.suppFrame, bg=self.bg)

        # Initialize children widgets into their organizational frames
        self.descLbl = tk.Label(self, text="Enter the full data for a single hero.", font=self.sectionFont, bg=self.bg)
        self.weightSecLbl = tk.Label(self, text="TS Comp Weights", height=1, font=self.sectionFont, bg=self.bg)
        self.weightFieldLbls = self.init_weightfls()
        self.weightFields = self.init_weightfields()
        self.suppSecLbl = tk.Label(self, text="Supplemental Info", height=1, font=self.sectionFont, bg=self.bg)
        self.suppFieldLbls = self.init_suppfls()
        self.suppFields = self.init_suppfields()
        self.notesFieldLbl = tk.Label(self, text="Notes", height=1, font=self.fieldFont, bg=self.bg)
        self.notesField = tk.Entry(self, font=self.fieldFont)

        # Organize everything into the grid
        self.descLbl.grid(row=0, column=0, columnspan=3, padx=2, pady=2, sticky='news')
        self.weightSecLbl.grid(row=1, column=0, padx=2, pady=2, sticky='nes')
        self.weightFrame.grid(row=1, column=1, columnspan=2, padx=2, pady=2, sticky='news')
        self.org_weightframe()
        self.suppSecLbl.grid(row=2, column=0, padx=2, pady=2, sticky='nes')
        self.suppFrame.grid(row=2, column=1, columnspan=2, padx=2, pady=2, sticky='news')
        self.org_suppframe()
        self.notesFieldLbl.grid(row=3, column=0, padx=2, pady=2, sticky='nes')
        self.notesField.grid(row=3, column=1, columnspan=2, padx=2, pady=2, sticky='news')
    # end def

    # Initialize all of the labels for the weight fields
    def init_weightfls(self):
        self.iceLbl = tk.Label(self.weightFrame, text="Ice", width=6, height=1, font=self.fieldFont, bg=self.bg)
        self.fireLbl = tk.Label(self.weightFrame, text="Fire", width=6, height=1, font=self.fieldFont, bg=self.bg)
        self.forestLbl = tk.Label(self.weightFrame, text="Forest", width=6, height=1, font=self.fieldFont, bg=self.bg)
        self.fogLbl = tk.Label(self.weightFrame, text="Fog", width=6, height=1, font=self.fieldFont, bg=self.bg)
        self.pureLbl = tk.Label(self.weightFrame, text="Pure", width=6, height=1, font=self.fieldFont, bg=self.bg)
        return [self.iceLbl, self.fireLbl, self.forestLbl, self.fogLbl, self.pureLbl]
    # end def

    # Initialize the Entry widgets for TS comp weights
    def init_weightfields(self):
        self.iceField = tk.Entry(self.weightFrame, width=2, font=self.fieldFont)
        self.fireField = tk.Entry(self.weightFrame, width=2, font=self.fieldFont)
        self.forestField = tk.Entry(self.weightFrame, width=2, font=self.fieldFont)
        self.fogField = tk.Entry(self.weightFrame, width=2, font=self.fieldFont)
        self.pureField = tk.Entry(self.weightFrame, width=2, font=self.fieldFont)
        return [self.iceField, self.fireField, self.forestField, self.fogField, self.pureField]
    # end def

    # Initialize the labels for the supplemental data
    def init_suppfls(self):
        # TODO: Set widths to match the size of the fields they control
        self.classLbl = tk.Label(self.suppFrame, text="Class", height=1, font=self.fieldFont, bg=self.bg)
        self.roleLbl = tk.Label(self.suppFrame, text="Role", height=1, font=self.fieldFont, bg=self.bg)
        self.progLbl = tk.Label(self.suppFrame, text="Investment Prog", height=1, font=self.fieldFont, bg=self.bg)
        self.collLbl = tk.Label(self.suppFrame, text="Desired Collection", height=1, font=self.fieldFont, bg=self.bg)
        return [self.classLbl, self.roleLbl, self.progLbl, self.collLbl]
    # end def

    # Initialize the various input widgets for the supplemental data
    def init_suppfields(self):
        self.classField = ttk.Combobox(self.suppFrame, state="readonly", values=Hero.CLASSES, width=7, font=self.fieldFont)
        self.roleField = tk.Entry(self.suppFrame, width=12, font=self.fieldFont)
        self.progField = ttk.Combobox(self.suppFrame, state="readonly", values=Hero.PROG_VALUES, width=11, font=self.fieldFont)
        self.collStarField = ttk.Combobox(self.collFrame, state="readonly", values=Collection.STARS, width=2, font=self.fieldFont)
        self.collTypeField = ttk.Combobox(self.collFrame, state="readonly", values=Collection.TYPES, width=7, font=self.fieldFont)
        # Return the colFrame instead of the collXXXFields for convenience when gridding
        return [self.classField, self.roleField, self.progField, self.collFrame]
    # end def

    # Organize the weights Frame
    def org_weightframe(self):
        for i,lbl in enumerate(self.weightFieldLbls):
            lbl.grid(row=0, column=i, padx=4, pady=4, sticky='news')
        # end for
        for i,field in enumerate(self.weightFields):
            field.grid(row=1, column=i, padx=4, pady=4, sticky='news')
        # end for
    # end def

    # Organize the supplemental data Frame
    def org_suppframe(self):
        for i, lbl in enumerate(self.suppFieldLbls):
            lbl.grid(row=0, column=i, padx=4, pady=4, sticky='news')
        # end for
        for i,field in enumerate(self.suppFields):
            field.grid(row=1, column=i, padx=4, pady=4, sticky='news')
        # end for
        self.collStarField.grid(row=0, column=0, padx=7, sticky='news')
        self.collTypeField.grid(row=0, column=1, padx=0, sticky='news')
    # end def
# end class