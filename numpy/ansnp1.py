import numpy as  np
arr = np.array([
    [11,22,33],
    [44,55,66],
    [66,77,88],
])
print("first column:",arr[ : ,0])
print("last row:",arr[-1])
print(arr[ :2, 1:])