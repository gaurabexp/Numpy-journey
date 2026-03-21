import numpy as np
# 1d array
a= np.array([1,2,3])
print (a)


# 2d array
b= np.array([[9.0,3.0,4.0],[5.0,7.0,3.0]])
print(b)

# Get Dimensions
print(a.ndim)    #number of dimensions -> 1
print(b.ndim)     #number of dimensions -> 2


# Get shape
print(a.shape)    # gives 3 as it is one dimensions with 3 basis
print(b.shape)    #gives 2,3 as it has 2 rows and 3 columns

#get Type
print(a.dtype)   #d--> data   which is int 64
print(b.dtype)   #            which is float 64

#change datatype
a= np.array([1,2,3], dtype='int16')
print (a.dtype)                      # data type will be int16

# Get size
print(a.itemsize)     # gives 2 as int 16 is divided 2 bytes of length 8 bits each
print(b.itemsize)


#Get totalsize
print(a.size)     # gives total number of elements in array i.e 3
print(b.size)      # gives total number of elements in array i.e 6
print(a.size * a.itemsize )      # i.e 3 x 2 =6
print(b.size * b.itemsize )      # i.e 6 x (64/8) =48
print(a.nbytes)                 # same as size * itemsize
print(b.nbytes)






