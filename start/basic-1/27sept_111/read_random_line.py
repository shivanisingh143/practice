import random


def random_line(file):
    line = open(file).read().splitlines()
    return random.choice(line)


print(random_line("C:/Users/Shivani/Pycharm/start/27sept_111/file"))
