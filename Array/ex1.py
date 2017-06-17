#1. Write a Python program to create an array of 5 integers and display the array items. Access individual element through indexes. 

from array import array

num_array = array("i", [1,2,4])

for i in num_array:
    print i

print "---------"    
print num_array[0]
print num_array[1]
print num_array[2]

str_array = array("c", "kot")

print "----------------"

for word in str_array:
    print word