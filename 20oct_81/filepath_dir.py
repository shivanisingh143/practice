import os

# path = "abc.txt"
# path="C:/Users/Shivani/Pycharm/start/20oct_81/concatenate_n_str.py"
path="C:/Users/Shivani/Pycharm/start/20oct_81/"


if os.path.isdir(path):
    print('dir')
elif os.path.isfile(path):
    print('file')
else:
    print('nothing')
