import numpy as np

list1 = [10, 11, 12]
list2 = [1, 2, 3]

array1 = np.array(list1)
array2 = np.array(list2)

subtracted_array = np.subtract(array1, array2)
subtracted = list(subtracted_array)

print(subtracted)
