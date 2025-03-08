import numpy as np

arr = np.array([1, 2, 3, 4, 5])

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = arr1 + arr2
print(result)

# Matrix multiplication
result = np.dot(arr1, arr2)
print(result)


arr_slice = np.array([1, 2, 3, 4, 5])

# indexing
print(arr_slice[0])

# slicing
print(arr_slice[1:3])

arr_reshape = np.array([1, 2, 3, 4, 5])

# reshaping
arr_reshape1 =arr_reshape.reshape(2, 3)
print(arr_reshape1)

arr_reshape2 = arr_reshape.T
print(arr_reshape2)