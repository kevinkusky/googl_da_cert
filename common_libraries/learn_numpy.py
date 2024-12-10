"""Numpy: Arrays and Vectors"""

import numpy as np
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# pylint: disable=pointless-string-statement
"""
    NumPy

    Array Attributes
        shape - returns tuple of array's dimensions
        dtype - returns data type of array contents
        size - returns number of elements in array
        T - Transpose array (rows swap columns)

"""

a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]
c = [
    [[1, 2], [3, 4]], [[5, 6], [7, 8]]
]


array_a = np.array(a)
array_b = np.array(b)
array_c = np.array(c)
array_d = np.array([[[1,2,3],
                     [4,5,6]],
                    [[9, 8, 7],
                     [6, 5, 4]]]
)

# Basic methods
print(np.floor(5.7)) # 5.0
print(np.ceiling(5.3)) # 6.0

print(type(array_a)) # <class 'numpy.ndarray'>
print(array_a.dtype) # dtype('int64')
print(np.mean(array_a)) # 3.0
print(np.log(array_a)) # [ln(x) for x in arr]
print(array_a.max())
print(array_a.max())

# 1 D Arrays
# array([1, 2, 3, 4])
print(array_a) # array([1, 2, 3, 4])
print(array_a.shape) # (3,)
print(array_a.ndim) # 1

# 2 D Arrays
# (4,2)                 (2,4)
# array([[1, 2],        array([[1, 2, 3, 4],
#       [3, 4],         [5, 6, 7, 8]])
#       [5, 6],
#       [7, 8]])
print(array_c)
print(array_c.shape) # (4, 2)
print(array_c.ndim) # 2
array_a = array_a.reshape(2, 4)
print(array_a)

# 2 D Arrays
# array([[[1, 2, 3],
#        [3, 4, 5]],
#
#       [[5, 6, 7],
#        [7, 8, 9]]])
print(array_d)
print(array_d.shape) # (2, 2, 3)
print(array_d.ndim) # 3
print(array_d.flatten())

# Special Arrays
# zeros(3, 2)            ones(2, 2)
# [[ 0.  0.]             [[ 1.  1.]
# [ 0.  0.]              [ 1.  1.]]
# [ 0.  0.]]
print(np.zeros(3,2))
print(np.ones(2,2))
# full((array, shape), fill_value)
np.full((5, 3), 8)

array_a[-1] = 7 # [1, 2, 3, 4, 7]

# Opperations
a = np.array([(1, 2, 3), (4, 5, 6)])
b = np.array([[1, 2, 3], [1, 2, 3]])
print('a:')
print(a)
print()
print('b:')
print(b)
print()
print('a + b:')
print(a + b)
print()
print('a * b:')
print(a * b)
