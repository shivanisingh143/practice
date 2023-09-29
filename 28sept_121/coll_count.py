import collections

list = [1, 2, 2, 3, 3, 4, 5, 6, 6]
print(collections.Counter(list).values())
print(sum(collections.Counter(list).values()))