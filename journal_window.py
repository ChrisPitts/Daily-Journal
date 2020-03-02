from tkinter import *
from datetime import date
import os
import globals

SAVE_BUTTON_TEXT = "Save"
SAVE_AND_EXIT_BUTTON_TEXT = "Save and Exit"
JOURNAL_SECTIONS = ["Day summary", "Emotions", "Ethics"]

TEXTBOX_WIDTH=100
TEXTBOX_HEIGHT=25


class WindowJournal:
    def __init__(self, journal_date):
        # Read from existing file
        self.journal_date = journal_date

        # The file already exists
        if os.path.exists("%s/%s.txt" % (globals.FILE_DIRECTORY, journal_date)):
            journal_file = open("%s/%s.txt" % (globals.FILE_DIRECTORY, journal_date), 'r')
            file_array = journal_file.read().split(globals.DELIMITER)
            journal_file.close()

        # No file exists
        else:
            file_array = [''] * len(JOURNAL_SECTIONS)

        # Initialize the window
        self.window = Tk()
        self.window.title("Journal %s" % journal_date)
        self.canvas = Canvas(self.window)
        self.frame = Frame(self.canvas)
        self.scrollbar = Scrollbar(self.window, orient='vertical', command=self.canvas.yview)

        self.entries = []   # Holds all the text fields

        # Initialize the journal fields
        for i in range(0, len(JOURNAL_SECTIONS)):
            Label(self.frame, text=JOURNAL_SECTIONS[i]).grid(row=i, column=0, sticky='W')
            self.entries.append(Text(self.frame, width=TEXTBOX_WIDTH))
            self.entries[i].insert(END, file_array[i])
            self.entries[i].grid(row=i, column=1, sticky='W')

        # Save buttons
        Button(self.frame, text=SAVE_AND_EXIT_BUTTON_TEXT, command=self.save_and_exit).grid(row=len(JOURNAL_SECTIONS), column=1, sticky='W')
        Button(self.frame, text=SAVE_BUTTON_TEXT, command=self.save).grid(row=len(JOURNAL_SECTIONS), column=0, sticky='W')

        self.canvas.update_idletasks()
        self.canvas.create_window(0, 0, anchor='nw', window=self.frame)
        self.canvas.configure(scrollregion=self.canvas.bbox('all'), yscrollcommand=self.scrollbar.set)
        self.canvas.pack(fill='both', expand=True, side='left')
        self.scrollbar.pack(fill='y', side='right')
        self.window.mainloop()

    def save(self):
        file_string = ''
        journal_file = open("%s/%s.txt" % (globals.FILE_DIRECTORY, self.journal_date), 'w')
        for entry in self.entries:
            file_string = file_string + entry.get(1.0, END) + globals.DELIMITER
        journal_file.write(file_string)
        journal_file.close()

    def save_and_exit(self):
        self.save()
        self.window.destroy()
