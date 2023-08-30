import cProfile

def sum():
    return 3+5

cProfile.run('sum()')