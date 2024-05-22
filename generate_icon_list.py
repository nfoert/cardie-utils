# This is a script for the Cardie project that turns a folder of Phosphor icons into a list of those icons
# https://github.com/nfoert/cardie

# Imports
import os
import sys
from pathlib import Path

DEFAULT_FOLDER_LOCATION = "./icons"

if len(sys.argv) >= 2:
    print(f"Using folder location '{sys.argv[1]}'")
    directory = sys.argv[1]
else:
    print(f"No folder location specified, using default folder, '{DEFAULT_FOLDER_LOCATION}', instead.")
    directory = DEFAULT_FOLDER_LOCATION

files = os.listdir(DEFAULT_FOLDER_LOCATION)
print(f"Found {len(files)} files.")

# Open the file to clear it
icons_list = open("icons_list.txt", "w")
icons_list.close()

# Iterate through all the file names and write them to the file
with open("icons_list.txt", "a") as icons_list:
    for file in range(len(files)):
        file_name = Path(files[file]).stem
        icons_list.write(file_name + "\n")

print("Done writing to icons_list.txt")
