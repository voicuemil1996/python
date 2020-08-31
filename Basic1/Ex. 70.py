import glob
import os

files = glob.glob("*")
print(files, '\n')

files.sort(key=os.path.getmtime)
print("\n".join(files))