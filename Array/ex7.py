#12. Write a Python program to remove the first occurrence of a specified element from an array.
from array import array
import numpy as np
num_array = array("i", [1, 2, 3, 4, 5, 6, 2])
deleted_items = [5, 6]

num_array.remove(5)
z = np.delete(num_array, deleted_items)

print num_array
print z