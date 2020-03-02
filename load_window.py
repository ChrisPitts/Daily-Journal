import os
from datetime import date
from tkinter import *
import globals
from journal_window import WindowJournal

WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


class WindowLoad:

    def __init__(self):
        dates = self.get_dates()
        self.window = Tk()
        for i in range(0, len(dates)):
            button_text = "%s, %i/%i/%i" % (WEEKDAYS[dates[i].weekday()], dates[i].month, dates[i].day, dates[i].year)
            button = Button(self.window, text=button_text, command=lambda: self.open_journal(dates[i]))
            button.grid(row=i, column=0, sticky='W')

    def get_dates(self):
        dates = []
        for root, dirs, files in os.walk(globals.FILE_DIRECTORY):
            for filename in files:
                dates.append(date(2000 + int(filename[6:8]), int(filename[0:2]), int(filename[3:5])))
        return dates

    def open_journal(self, journal_date):
        self.window.destroy()
        WindowJournal(journal_date.strftime("%m-%d-%y"))

