import numpy as np 
a =np.array([[1,2,3],
             [4,5,6]])

print("shape = ",a.shape)
print("size=",a.size)
print("Ndim =",a.ndim)
print("Dtype=",a.dtype)

b = a.astype(float)
print("new data type=",b.dtype)