def fact(n):
    return (n == 1) or (n * fact(n - 1))
    # return (n == 1) or (n * fact(n - 1))


x = fact(4)
print(x)
