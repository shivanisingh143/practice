import os

# for file in [__file__, os.path.dirname(__file__), '/', './broken_link']:
for file in [__file__, os.path.dirname('C:/Users/Shivani/Pycharm/start/26sept_101/'), '/', './broken_link']:
# file = __file__
    print("file :", file)
    print(os.path.isdir(file))
    print(os.path.isfile(file))
    print(os.path.isabs(file))
    print(os.path.islink(file))
    print(os.path.exists(file))
    print(os.path.lexists(file))