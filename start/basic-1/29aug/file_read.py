######  file read
import os

file = open("C:/Users/Shivani/Pycharm/start/29aug/demo", "rt")
a = file.read()
print(a)

print(file.readline())
print(file.readline())
print(file.readline())
file.close()


c = file.readlines()
print(c)

##########  file append

f1 = open("C:/Users/Shivani/Pycharm/start/29aug/demo_write", "a")
f1.write("checking file written")
f1.close()

###### file overwrite

f2 = open("C:/Users/Shivani/Pycharm/start/29aug/demo_write", "w")
f2.write("Woops! I have deleted the content!")
f2.close()

########### create file

file = open("C:/Users/Shivani/Pycharm/start/29aug/demo_write", "x")
file.read()

############ delete file

os.remove("C:/Users/Shivani/Pycharm/start/29aug/demo_write")
# os.rmdir("")

###### chk file exist

if os.path.exists("C:/Users/Shivani/Pycharm/start/29aug/demo_write"):
    print("file removed")
else:
    print("file not exist")