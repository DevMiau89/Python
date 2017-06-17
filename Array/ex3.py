#4. Write a Python program to get the length in bytes of one array item in the internal representation. 

from array import *
from sys import getsizeof

num_array = array("i", [1, 2, 3])

z = num_array.itemsize

print z 

size = getsizeof(num_array)

a = 2
item_size = getsizeof(a)
print size
print item_size