import numpy as np
#             Accessing/Changing specific elements, rows, columns, etc
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)
print(a.shape)


#get specific element[r, c]
print(a[1, 5])      #the 2 x 3 matrix has row index as 0, 1 i.e 1st row is 0 and 2nd row is 1
print(a[1,-2])  # gives same value as a[2,5] i.e 2nd row 2nd last element 


# to get specific row
print (a[0, :])      #  : is the basic slice syntax


# get specific column;
print (a[:, 2])

# getting little more fancy [startindex:endindex:stepsize]
print(a[0, 1:6:2])    #i.e from row 1 start from 2nd index to the 6 value leaving one space


# change the value of row 1 element 5 value i.e 13 to 20
a[1, 5] = 20
print(a)

# change columns
a[:, 2] =5
print(a)

a[:, 2] =[1,2]
print(a)


#3d example
b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)

#get specific element (works outside in)
print(b[0,1,1])    # 0-> first index of the 3d array [[1,2],[3,4]] , 1--> second row , 1--> second element (i.e 4)

print(b[0,1,:])         # [3,4]  print index 1 row from 1st array index
print(b[0,:,0])         #[1,3]   Print intex 0 column from 1st array index

#replace
b[:,1,:] =[[9,9],[8,8]]  # this changes the value of both row index of 0 and 1 of arrays
# b[:,1,:] =[[9,9,9],[8,8]]  #this doesnot work
print(b)

#get class type
print(type(a))       #---><class 'numpy.ndarray'>