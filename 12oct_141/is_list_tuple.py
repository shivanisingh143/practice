x = ('tuple', 2, 3, 3.5)

print(isinstance(x, list))
print(isinstance(x, tuple))

if x is list:
    print('list')
else:
    print('tuple')