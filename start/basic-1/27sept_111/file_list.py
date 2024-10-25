import glob

file = glob.glob('*.*')
print(file)
print(glob.glob('*.py'))
print(glob.glob('./[0to9].*'))
