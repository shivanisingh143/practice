my_list = [2, 10, 15]

result_dict = {}
for num in my_list:
    if num % 2 == 0:
        result_dict[num] = "even"
    else:
        result_dict[num] = "odd"

print(result_dict)