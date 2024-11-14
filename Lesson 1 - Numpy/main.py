import numpy as np
sample = [1,2,3,4]
print(type(sample))

sample_numpy = np.array(sample)
print(type(sample_numpy))

#homogenous - only one type of data
#error_array = np.array([1,2,4],"name")

#can perform arithmetic operation
a=np.array([1,2,3])
a+=1
print(a)

arrayzero = np.zeros(5)
print(arrayzero)

onesarray = np.ones(5)
print(onesarray)

floatarray = np.array([1,2,3,4,5],dtype = "f")
print(floatarray)

#array_2d_error = np.array([[1,2],[3]])
#print(array_2d)

array_2d = np.array([[1,2],[3,4]])
print(array_2d)

print("Array Dimension ",array_2d.ndim) #1D, 2D , 3D
print("Number of rows_col ",array_2d.shape) #number of rows and  colum
print("Number of elements ",array_2d.size) #number of elements
print("Array size",array_2d.nbytes) #Size in bytes - 4 bytes

num_array = np.arange(1,100)
print(num_array)

even_array = np.arange(2,100,2)
print(even_array)

odd_array = np.arange(1,100,2)
print(odd_array)

#Prints number from 1 to 10 in random order
random_arr = np.random.permutation(np.arange(1,11))
print("Permutation : ",random_arr)

random_num = np.random.randint(1,10)
print(random_num)

#prints 20 random float from 0 to 1
random_array = np.random.rand(1,20)
print(random_array)
print(random_array.shape)

reshaped_array = np.arange(1, 10).reshape(3,3)
print(reshaped_array)
print(reshaped_array.shape)

#Exc 1
linear_array = np.arange(1,37)

print(linear_array.reshape(6,6))
print(linear_array.reshape(12, 3))
print(linear_array.reshape(18,2))


random_array = np.random.permutation(np.arange(1,10))
print(random_array)
sorted_array = np.sort(random_array)
print(sorted_array)