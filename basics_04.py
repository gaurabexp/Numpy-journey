#mathematics
import numpy as np
a= np.array([1,2,3,4])
print(a)
print(a+2)
print(a-2)
print(a*2)
print(a/2)


b= np.array([1,0,1,0])
print(a+b)
print(a**2)


#take the sin 
si=np.sin (a)
print(si)



#linear Algebra
aa= np.ones((2,3))
print(aa)

bb=np.full((3,2),2)
print(bb)

print(np.matmul(aa,bb))

#find the determinant
c=np.identity(3)
print(np.linalg.det(c))



### for more informations
# https://numpy.org/doc/stable/reference/routines.math.html



# Statistics
stats=np.array([[1,2,3],[4,5,6]])
print(stats)

print(np.min(stats))
print(np.min(stats, axis=1))
print(np.max(stats))
print(np.sum(stats))
print(np.sum(stats, axis=0))