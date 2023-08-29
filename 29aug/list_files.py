from os import listdir
from os.path import isfile, join
a = [f for f in listdir("C:/Users/Shivani/Pycharm/start/29aug") if isfile(join("C:/Users/Shivani/Pycharm/start/29aug", f))]
print(a)

##### same but file file in new line
for f in listdir("C:/Users/Shivani/Pycharm/start/29aug"):
    print(f)