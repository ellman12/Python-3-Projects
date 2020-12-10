#######################################################################
# Purpose: Used to sort files.
#######################################################################
# Comments: Created on Tuesday, December 8, 2020 11:15 AM.
# My first real/actually practical Python script.
#######################################################################
# Ideas: have a way to rename the current file in the loop if the
# user wants???
# Different modes for sorting. Option to put them by day too.
# Move files with errors to unsorted folder.
# "also, i would reccomment zero padding the month folder, so it's 01 for january, that way it sorts well"
#######################################################################

import os.path
import shutil
from tkinter import *
from tkinter import filedialog
import PIL.Image
import datetime

# Constants
EXIF_DATETIME_TAG = 36867

folderDialog = Tk()
folderDialog.withdraw()  # Hide useless extra window.

# Get the directories to use.
dirToSort = filedialog.askdirectory(title="Select directory to sort")
destinationDir = filedialog.askdirectory(title="Where should the sorted files go?")

for dirPath, _, files in os.walk(dirToSort):
    for file in files:
        # if (".jpg" in file) or (".mp4" in file):
        if (".jpg" in file):
            img = PIL.Image.open(os.path.join(dirPath, file))
            exif_data = img._getexif()

            if (exif_data == None):
                print(f"Error. {file} doesn't have date :(")
                continue

            if (EXIF_DATETIME_TAG in exif_data):
                fileTakenDate = datetime.datetime.strptime(exif_data[EXIF_DATETIME_TAG], "%Y:%m:%d %H:%M:%S")

                filePath = os.path.join(dirPath, file)
                # filePath = dirPath + r"/" + file

                destinationPath = os.path.join(destinationDir, str(fileTakenDate.year), str(fileTakenDate.month))
                # destinationPath = destinationDir + r"/" + str(fileTakenDate.year) + r"/" + str(fileTakenDate.month)

                if not os.path.exists(destinationPath):
                    os.makedirs(destinationPath)
                shutil.copyfile(filePath, os.path.join(destinationPath, file))

                print(f"{file} at {filePath} moved to {destinationPath}")

        else:
            print("Unsupported file type.")
