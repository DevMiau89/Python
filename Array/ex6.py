#9. Write a Python program to append items from a specified list.
from array import array
a_list = [7, 8, 9]

my_array = array("i", [1, 2, 3, 4, 5, 6])

my_array.fromlist(a_list)

print my_array

#10. Write a Python program to insert a new item before the second element in an existing array.
#11. Write a Python program to remove a specified item using the index from an array
num_array = array("i", [1, 2, 3, 4, 5, 6])

num_array.insert(1,5)

num_array.pop(5)
num_array.remove(1)
print num_array