#6. Write a Python program to get the number of occurrences of a specified element in an array. 
from array import array

num_array = array('i', [1, 3, 5, 3, 7, 9, 3])

print "Number of occurances of number three is:", num_array.count(3)

#7. Write a Python program to append items from iterrable to the end of the array.
Original_array = array('i', [1, 3, 5, 7, 9])
my_extnd_array = array('i', [7 ,8 ,9 , 10])


Original_array.extend(my_extnd_array)
print Original_array

#8. Write a Python program to convert an array to an array of machine values and return the bytes representation.
my_array = array('i', [1, 3, 5, 7, 9])

my_array.byteswap()
print "-------------"
print my_array

print("Bytes to String: ")
x = array('b', [119, 51, 114, 101,  115, 111, 117, 114, 99, 101])
s = "".join(map(chr, x))
print(s)