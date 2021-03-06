from tkinter import *
from datetime import date
import os
import globals
import version_manager as vm

SAVE_BUTTON_TEXT = "Save"
SAVE_AND_EXIT_BUTTON_TEXT = "Save and Exit"


TEXTBOX_WIDTH=100
TEXTBOX_HEIGHT=25


class WindowJournal:
    def __init__(self, journal_date):
        # Read from existing file
        self.journal_date = journal_date
        self.file_name = "%s/%s.txt" % (globals.FILE_DIRECTORY, journal_date)
        # The file already exists
        if os.path.exists(self.file_name):
            file_array = vm.read_file(self.file_name)

        # No file exists
        else:
            file_array = [''] * (len(vm.SECTIONS) + 1)

        # Initialize the window
        self.window = Tk()
        self.window.title("Journal %s" % journal_date)
        self.canvas = Canvas(self.window)
        self.frame = Frame(self.canvas)
        self.scrollbar = Scrollbar(self.window, orient='vertical', command=self.canvas.yview)

        self.entries = []   # Holds all the text fields

        # Initialize the journal fields
        for i in range(0, len(vm.SECTIONS)):
            Label(self.frame, text=vm.SECTIONS[i]).grid(row=i, column=0, sticky='W')
            self.entries.append(Text(self.frame, width=TEXTBOX_WIDTH))
            self.entries[i].insert(END, file_array[i+1])
            self.entries[i].grid(row=i, column=1, sticky='W')

        # Save buttons
        Button(self.frame, text=SAVE_AND_EXIT_BUTTON_TEXT, command=self.save_and_exit).grid(row=len(vm.SECTIONS), column=1, sticky='W')
        Button(self.frame, text=SAVE_BUTTON_TEXT, command=self.save).grid(row=len(vm.SECTIONS), column=0, sticky='W')

        self.canvas.update_idletasks()
        self.canvas.create_window(0, 0, anchor='nw', window=self.frame)
        self.canvas.configure(scrollregion=self.canvas.bbox('all'), yscrollcommand=self.scrollbar.set)
        self.canvas.pack(fill='both', expand=True, side='left')
        self.scrollbar.pack(fill='y', side='right')
        self.window.mainloop()

    def save(self):
        write_array = [vm.CURRENT_VERSION]
        for entry in self.entries:
            write_array.append(entry.get(1.0, END))
        vm.save_file(self.file_name, write_array)

    def save_and_exit(self):
        self.save()
        self.window.destroy()
