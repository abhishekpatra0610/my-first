import numpy as np
# a[ : ,1] is used for 2d array slicing because of row and column indexing .
# 1d array has only one axis so this type of slicing gives indexError : too many indices


# 1d array slicing 
arr= np.array([1,2,3,4,5,6])
print (arr[0])
print(arr[1:5])