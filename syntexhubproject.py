import numpy as np
#Array Creation
#1D array
arr1 =np.array([10,20,30,40,50,60,70])

#2D array
arr2 =np.array([[1,2,3,4],[4,5,6,8]])
print(arr1)
print(arr2)

#Indexing
print(arr1[2])
#2D indexing
print([arr2[1,3]])

#Slicing
print(arr1[1:3])
#2D slicing
print(arr2[:,1])
print(arr2[1,:])

#Operations
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a+b)
print(a*b)
print(a**2)