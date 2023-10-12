def max_min(data):
    max = data[0]
    min = data[0]

    for i in data:
        if i > max:
            max = i
        elif i < min:
            min = i
    return max, min


print(max_min([0, 10, 20, -5, 3, 5, 2]))