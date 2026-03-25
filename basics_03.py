# Initializing Different Types of Arrays
import numpy as np

#print all zeros
a= np.zeros(5)
print(a)

#print  2x 3 matrix
b= np.zeros((2,3))
print(b)

#priint 3d matrix
c= np.zeros((2,3,3))
print(c)

#all 1s matrix
d=np.ones((2,3,3))
print(d)


#Any other number
e= np.full((2,2),99, dtype='float32')
print(e)               #---->[[99. 99.]
                        #     [99. 99.]]
print(e.dtype)


#Any other number(full_like)
f=np.full_like(a,4)
print(f)            #--->[4. 4. 4. 4. 4.]



#random decimal numbers
g=np.random.rand(4,2)
h=np.random.random_sample(a.shape)
print(g)
print(h)




#random Integer values
i=np.random.randint(7)
j=np.random.randint(7, size=(3,3))
print(i)    #this gives one value , so we need to give size to from a proper matrix
print(j)

#In that line of code, -4 and 8 define the range of the random integers being generated.
k=np.random.randint(-4,8, size=(3,3))
print(k)


#identity matrix
l= np.identity(3)
print(l)


#Repeat an array
arr= np.array([[1,2,3]])
r1=np.repeat(arr,3, axis=0)
print(r1)        

# [[1 2 3]
#  [1 2 3]
#  [1 2 3]]

new=np.ones((5,5))
oz=np.zeros((3,3))
oz[1,1]=9
print(oz)

new[1:4,1:4]= oz

print(new)


