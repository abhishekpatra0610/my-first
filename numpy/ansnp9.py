import numpy as np
# .dtype() shows the datatype of an array
arr = np.array([2.0,3.0,5.0])
print(arr.dtype)

#.astype() coverts array elements to an other datatype 
arr1 =np.array([1.0,2.0,3.0])
print(arr1.astype(int))