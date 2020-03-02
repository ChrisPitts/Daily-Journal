from tkinter import *
import os
import globals
from datetime import date
from journal_window import WindowJournal
from load_window import WindowLoad

# TITLE
WINDOW_TITLE = "Main Menu"

# BUTTON TEXT
TODAYS_JOURNAL_BUTTON_TEXT = "Today's Journal"
LOAD_JOURNAL_BUTTON_TEXT = "Load Journal"

class WindowMainMenu:

    def __init__(self):

        # initialize the window
        self.window = Tk()
        self.window.title(WINDOW_TITLE)

        # initialize the buttons
        Button(self.window, text=TODAYS_JOURNAL_BUTTON_TEXT, command=self.onclick_new_journal).grid(row=0, column=0, sticky='W')
        Button(self.window, text=LOAD_JOURNAL_BUTTON_TEXT, command=self.load_journal).grid(row=1, column=0, sticky='W')

        self.window.mainloop()

    def onclick_new_journal(self):
        if not os.path.exists(globals.FILE_DIRECTORY):
            os.mkdir(globals.FILE_DIRECTORY)
        WindowJournal(date.today().strftime('%m-%d-%y'))

    def load_journal(self):
        WindowLoad()


WindowMainMenu()
