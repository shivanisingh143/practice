import time


def sum_num(n):
    sum = 0
    start = time.time()
    for i in range(1, n + 1):
        sum = sum + i
    end = time.time()
    return sum, start, end


n = 5
print("\nTime to sum of 1 to ", n, " and required time to calculate is :", sum_num(n))
