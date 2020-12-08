#######################################################################
# Purpose: Used to sort files.
#######################################################################
# Comments: Created on Tuesday, December 8, 2020 11:15 AM.
# My first real/actually practical Python script.
#######################################################################

import os
from tkinter import *
from tkinter import filedialog

folderDialog = Tk()
folderDialog.withdraw()  # Hide useless extra window.

# Get the directories to use.
folderDialog = filedialog.askdirectory(title="Select directory to sort")
dirToSort = folderDialog  # Unsorted directory.

folderDialog = filedialog.askdirectory(title="Select directory to sort")
destinationDir = folderDialog  # Where sorted files go.

for _, _, files in os.walk(dirToSort):
    for file in files:
        if (".png" in file) or (".jpg" in file):
            print(file)
