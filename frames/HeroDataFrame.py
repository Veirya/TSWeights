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
        self.columnconfigure(0, weight=0) # Base grid is 5x3, don't want col 0 to expand past the bare necessities
        self.descVar = tk.StringVar(value="Enter the full data for a single hero.")
        self.vcmd = (self.register(self.__val_int), "%P")
        
        # Organizational helper frames
        self.weightFrame = tk.Frame(self, bg=self.bg)
        self.suppFrame = tk.Frame(self, bg=self.bg)
        self.collFrame = tk.Frame(self.suppFrame, bg=self.bg)

        # Initialize children widgets into their organizational frames
        self.descLbl = tk.Label(self, textvariable=self.descVar, height=1,font=self.sectionFont, bg=self.bg)
        self.nameLbl = tk.Label(self, text="Hero Name", width=9, height=1, font=self.sectionFont, bg=self.bg)
        self.nameField = tk.Entry(self, width=20, font=self.fieldFont)
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
        self.nameLbl.grid(row=1, column=0, padx=2, pady=2, sticky='nes')
        self.nameField.grid(row=1, column=1, padx=2, pady=2, sticky='news')
        self.weightSecLbl.grid(row=2, column=0, padx=2, pady=2, sticky='nes')
        self.weightFrame.grid(row=2, column=1, columnspan=2, padx=2, pady=2, sticky='news')
        self.org_weightframe()
        self.suppSecLbl.grid(row=3, column=0, padx=2, pady=2, sticky='nes')
        self.suppFrame.grid(row=3, column=1, columnspan=2, padx=2, pady=2, sticky='news')
        self.org_suppframe()
        self.notesFieldLbl.grid(row=4, column=0, padx=2, pady=2, sticky='nes')
        self.notesField.grid(row=4, column=1, columnspan=2, padx=2, pady=2, sticky='news')
        
        # Setup the tab order. I hate how this works, but at least now I understand it
        order = (
            self.nameField, self.weightFrame, self.suppFrame, self.notesField,
            self.collFrame, self.collStarField, self.collTypeField
        )
        for wid in order: wid.tkraise()
    # end def

    # Initialize all of the labels for the weight fields
    def init_weightfls(self):
        self.iceLbl = tk.Label(self.weightFrame, text="Ice", width=9, height=1, font=self.fieldFont, bg=self.bg)
        self.fireLbl = tk.Label(self.weightFrame, text="Fire", width=9, height=1, font=self.fieldFont, bg=self.bg)
        self.forestLbl = tk.Label(self.weightFrame, text="Forest", width=9, height=1, font=self.fieldFont, bg=self.bg)
        self.fogLbl = tk.Label(self.weightFrame, text="Fog", width=9, height=1, font=self.fieldFont, bg=self.bg)
        self.pureLbl = tk.Label(self.weightFrame, text="Pure", width=9, height=1, font=self.fieldFont, bg=self.bg)
        return [self.iceLbl, self.fireLbl, self.forestLbl, self.fogLbl, self.pureLbl]
    # end def

    # Initialize the Entry widgets for TS comp weights
    def init_weightfields(self):
        self.iceField = tk.Entry(self.weightFrame, width=2, font=self.fieldFont, validate='key', validatecommand=self.vcmd)
        self.fireField = tk.Entry(self.weightFrame, width=2, font=self.fieldFont, validate='key', validatecommand=self.vcmd)
        self.forestField = tk.Entry(self.weightFrame, width=2, font=self.fieldFont, validate='key', validatecommand=self.vcmd)
        self.fogField = tk.Entry(self.weightFrame, width=2, font=self.fieldFont, validate='key', validatecommand=self.vcmd)
        self.pureField = tk.Entry(self.weightFrame, width=2, font=self.fieldFont, validate='key', validatecommand=self.vcmd)
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
        self.collStarField = ttk.Combobox(self.collFrame, state="readonly", values=Collection.STAR_VALUES, width=2, font=self.fieldFont)
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

    # Clear all of the fields
    def clear_data(self):
        self.nameField.delete(0, 'end')
        for field in self.weightFields:
            field.delete(0, 'end')
        # end for
        for field in self.suppFields[:-1]:
            # Method differs between Entry and Combobox types
            if type(field) == ttk.Combobox: field.set("")
            else: field.delete(0, 'end')
        # end for
        self.collStarField.set("")
        self.collTypeField.set("")
        self.notesField.delete(0, 'end')
    # end def

    # Validate the input, highlighting the first thing that was found to be incorrect.
    # Returns a Hero object containing the data if it's all good, otherwise returns False.
    # TODO: Might have this check every field for errors before returning if one is found
    def fetch_data(self):
        # First check that the name is valid
        name = self.nameField.get()
        if name.lower() not in Hero.HERO_NAMES:
            self.descVar.set(f"Hero '{name}' not recognized. Check the spelling.")
            self.descLbl.configure(fg='dark red')
            self.nameLbl.configure(fg='dark red')
            return False
        else: self.nameLbl.configure(fg='black') # In case it was turned red before
        # end if

        hero = Hero(name.title())

        # Check that at least one TS Weight was filled in with a non-zero. Blanks treated as 0.
        weights = []
        for field in self.weightFields:
            val = field.get()
            val = 0 if val=="" else int(val)
            weights.append(val)
        # end for
        hero.weights = weights
        hero.totalWeight = sum(hero.weights)
        if hero.totalWeight == 0:
            self.descVar.set("At least one weight must be greater than zero.")
            self.descLbl.configure(fg='dark red')
            self.weightSecLbl.configure(fg='dark red')
            for label in self.weightFieldLbls: label.configure(fg='dark red')
        else:
            self.weightSecLbl.configure(fg='black')
            [label.configure(fg='black') for label in self.weightFieldLbls]
        # end if

        # Everything else is optional and either free-input or enforced by Comboboxes
        hero.heroClass = self.classField.get()
        hero.role = self.roleField.get()
        hero.prog = self.progField.get()
        hero.coll.stars = self.collStarField.get()
        hero.coll.type = self.collTypeField.get()
        hero.notes = self.notesField.get()

        return hero
    # end def

    # Used to force positive integer input for Entry fields
    def __val_int(self, P):
        return P.isdigit() or P == ""
    # end def
# end class