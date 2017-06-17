#ex43 Write a Python program to print the square and cube symbol in the area of a rectangle and volume of a cylinder.
import math

print "The area of rectangle is %d" % (math.sqrt(5))
print "The volume of cylinder is %d" % (math.sqrt(math.pi * 4.0))

area = 1256.66  
volume = 1254.725  
decimals = 2  
print("The area of the rectangle is {0:.{1}f}cmu\u00b2".format(area, decimals))  
decimals = 3  
print("The volume of the cylinder is {0:.{1}f}cm\u00b3".format(volume, decimals)) 


 #ex44 Write a Python program to print the index of the character in a string.
sample_string = 'w3resource'

for letter in sample_string:
    print "Current character {0} position at : {1}".format(letter, sample_string.index(letter))


#ex46 Write a Python program to convert a string in a list.

str1 = 'kot'
new_list = list(str1)

print new_list

