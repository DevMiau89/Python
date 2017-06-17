#13. Write a Python program to convert an array to an ordinary list with the same items. 
from array import array

num_array = array("i", [1, 2, 3, 4, 5, 6])

a_list = list(num_array)

print a_list