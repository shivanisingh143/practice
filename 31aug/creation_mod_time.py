import os
import time

print("file modification time: %s" % time.ctime(os.path.getmtime("C:/Users/Shivani/Pycharm/start/31aug/abs_filepath.py")))
print("file creation time: %s" % time.ctime(os.path.getctime("C:/Users/Shivani/Pycharm/start/31aug/abs_filepath.py")))