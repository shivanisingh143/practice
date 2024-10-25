import glob
import os

# os.chdir("C:/Users/Shivani/Pycharm/start/31aug/")
files = glob.glob(".py")
files.sort(key=os.path.getmtime)
print("\n".join(files))

# files.sort(key=os.path.getmtime)
# print("\n".join(files))
