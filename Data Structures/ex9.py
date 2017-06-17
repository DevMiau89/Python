#13. Write a Python program to get the array size of types unsigned integer and float
from array import array
import numpy as np

x = np.array([1,2,3], dtype=np.float64)
print x.itemsize

my_float = array("f", [1.2, 1.3, 4.3])
print my_float.itemsize

print "------------------"

#14. Write a Python program to get an array buffer information.

my_array = array("i", [1, 2, 3])
print("Array buffer start address in memory and number of elements.")
print my_array.buffer_info()
