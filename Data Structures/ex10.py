#15. Write a Python program to get the length of an array.
from array import array

my_array = array("c", "kot")
num_array = array("i", [1, 2, 3, 4, 5])

print "Lenght of the array is:"
print len(my_array)
print len(num_array)

#16. Write a Python program to convert an array to an ordinary list with the same items.

number_array = array("i", [1, 2, 3, 4, 5]).tolist()

print "Array to list:"
print number_array

#17. Write a Python program to convert an array to an array of machine values and return the bytes representation.
import binascii

an_array = array("i", [11, 12, 13, 14, 15])


print binascii.hexlify(an_array)
