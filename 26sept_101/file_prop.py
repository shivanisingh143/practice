import os.path
import time

print("file : ", __file__)
print(time.ctime(os.path.getctime(__file__)))
print(time.ctime(os.path.getmtime(__file__)))
print(time.ctime(os.path.getatime(__file__)))
print(os.path.getsize(__file__))