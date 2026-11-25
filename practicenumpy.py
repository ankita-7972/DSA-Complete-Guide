from numpy import *

val = array([1,2,3,4])
# In Python NumPy, there are different array
#  creation functions used to create arrays with specific values or sequences.
# It generates evenly spaced numbers between a starting value and an ending value. (linspace(start, stop, num))
val= linspace(10,20,3)
print (val)
# Logarithmic Space.
# It generates numbers that are evenly spaced on a logarithmic scale.(logspace(start, stop, num))
val= logspace(1,4,4)
print (val.dtype)

# Array range (It generates values within a given range using a specified step size.) (arange(start, stop, step))
val= arange(1,20,3)
print(val)

# It creates an array filled with zeros.(zeros(shape))
val= zeros(5)
print(val)

# It creates an array filled with ones.(ones(shape))
val= ones(6)
print(val)

# It creates an array filled with a specific value.(full(shape, fill_value))

val = full(5,8)
print(val)
# for x in val:
#     print(x, end=" ")


# 2D array
two = array([[1,2,3],[4,5,6],[7,8,9]])
print(two)

# 3D array
three = array([  [ [1,2,],[3,4] ],[ [5,6],[7,8] ]  ])
print(three,"3D array")