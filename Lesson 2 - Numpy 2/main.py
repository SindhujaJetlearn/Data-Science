import numpy as np

a=np.array([1,2,3,4,5,6,7,8])
#index - always starts with 0
print(a[0])
print(a[0:4])

#from start
print(a[:4])

#till end
print(a[5:])

# Concept of array slicing array[start : end : step]
print(a[0:8:2])
print(a[::2]) # prints every second element

# reverse the array
print(a[::-1]) 

multi_array = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(multi_array[0:2, 0:2])

# Exercise 1 - Create a matrix of 7*7 and take out the middle 3*3 cross-seciton 
# out of the 7*7 matrix
mat=np.arange(1,50).reshape(7,7)
print(mat)
print(mat[2:5,2:5])

# Conditional selection of elements
# Select all the even elements from a numpy array

k=np.array([1,2,3,4,5,6,7,8])
even_array=k[k%2 == 0]
print("Even Array : ", even_array)

odd_array = k[k%2 != 0]
print("Odd Array : ", odd_array)

# compare with a value
b=k[k==5]
print(b) #prints 5 as it exists

b=k[k==500]
print(b) #returns empty

# selection by indexes
print(k[[2,4,6]]) # 2,4,6 are indexes

# Exercise 2 - Select the value less than 5 from an array of 1-10
s = np.array([1,2,3,4,5,6,7,8])
print("Number less than 5 :",s[s<5])

#Operations on List
sample_list=[1,2,3,4,5,6,7,8]
for i in range(0, len(sample_list)):
    sample_list[i] +=1
    
print("sample list : ",sample_list)	

#Operation on array
sample_array = np.array([1,2,3,4,5,6,7,8])
sample_array += 1  # No need to run a for loop
print("sample array : ",sample_array)

#Addition on array
sample_array1 = np.array([1,2,3,4,5,6,7,8])
sample_array2 = np.array([1,2,3,4,5,6,7,8])
result=sample_array1+sample_array2
print("sum of array : ", result)

# Exercise 3 - Do the matrix sub

# Matrix Addition through numpy 
matA = np.random.permutation(np.arange(16)).reshape(4,4)
print("MatA : \n", matA)

matB = np.random.permutation(np.arange(16)).reshape(4,4)
print("MatB : \n", matB)

print("Sum of MatA and MatB : \n",matA + matB) 

# Create a function for numpy operation
def linear_eqn(x):
    y=(2*x)+3
    print(y)

linear_eqn(10)
x=np.array([1,2,3,4,5])
linear_eqn(x)


