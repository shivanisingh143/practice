from timeit import default_timer

# print(default_timer())
def timer(n):
    str = default_timer()
    print(str)

    for i in range(0, n):
        print(i)

    print(default_timer())
    print(default_timer() - str)

timer(5)