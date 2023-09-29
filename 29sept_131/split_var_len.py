var_list = ['a', 'b', 'c', 'd']
x, y, z = var_list[0:3]
print(x, y, z)
var_list = [100, 20.25, 20]
x, y = (var_list + [None] * 2)[1:3]
print(x, y)