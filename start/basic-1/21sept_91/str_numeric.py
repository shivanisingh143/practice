x = 'abc23'

try:
    a = int(x)
    print('numeric')
except Exception as e:
    print("not numeric")