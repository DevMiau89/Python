#2. Write a Python program to append a new item to the end of the array.
#3. Write a Python program to reverse the order of the items in the array.

from array import *

num_array = array("i", [1, 2, 3])

new_nums = 4

num_array.append(new_nums)

print "New array :", num_array

num_array.reverse()

print num_array

z = list(reversed(num_array))
print z

my_array = array("i", [1, 2, 3])

my_array.reverse()

print my_array