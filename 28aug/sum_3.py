def sum(x, y, z):
    if x == y or y == z or z == x:
        sum = 0
    else:
        sum = x+y+z
    return sum

print(sum(1, 2, 3))
print(sum(1, 2, 2))