import numpy as np

#miscellaneous

#load data from files
filedata=np.genfromtxt('data.txt' , delimiter=',')
filedata=filedata.astype('int32')
print(filedata)



###  Boolean masking and Advanced indexing
print(filedata > 50)
print(filedata[filedata > 50])    #gives onlythe value greater than 50

### You can index with a list in numpy


a= np.array([1,2,3,4,5,6,7,8,9])
print(a[[1,2,8]])

print(np.any(filedata > 50, axis=0))    #np.any: Returns True if at least one number in the row is > 50.
print(np.all(filedata > 50, axis=0))    #np.all: Returns True only if every single number in the row is > 50.
print(np.any(filedata > 50, axis=1))

print((filedata > 50) & (filedata < 100))
print(~((filedata > 50) & (filedata < 100)))    # not