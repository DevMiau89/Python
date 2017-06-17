#5. Write a Python program to get the current memory address and the length in elements of the buffer used to hold an array?s contents and also find the size of the memory buffer in bytes.
from array import *
from sys import getsizeof

num_array = array("i", [1, 2, 3])

Original_array = array('i', [1, 3, 5, 7, 9]) 

buffer = num_array.buffer_info()
buffer_view = num_array.buffer_info() * num_array.itemsize
size = getsizeof(Original_array)

print buffer
print buffer_view

print size