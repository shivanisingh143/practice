numlist = [15, 30, 45, 50, 60]

x = list(filter(lambda a: (a % 15 == 0), numlist))
print(x)