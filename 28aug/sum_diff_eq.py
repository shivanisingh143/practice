def sum_diff(x, y):
    if x==y or abs(x-y) == 5 or (x+y)==5:
       return True
    else:
        return False

print(sum_diff(2, 3))
print(sum_diff(10, 5))
print(sum_diff(5, 3))