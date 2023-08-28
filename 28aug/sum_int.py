def add_numbers(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a+b
    else:
        return "input must be integer"

print(add_numbers(10, 20))
print(add_numbers(10, 20.23))
print(add_numbers('5', 6))
print(add_numbers('5', '6'))