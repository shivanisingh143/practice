from functools import reduce

li = [10, 20, 30]

num = reduce((lambda x, y: x * y), li)
print(num)
