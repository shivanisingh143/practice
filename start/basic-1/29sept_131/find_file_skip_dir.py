import os

print([f for f in os.listdir("C:/Users/Shivani/Pycharm/start") if os.path.isfile(os.path.join("C:/Users/Shivani/Pycharm/start", f))])