#11. Write a Python program to compare two unordered lists (not sets).
from collections import Counter

list_1 = [6, 1, 3, 2]
list_2 = [10, 8 , 5]

print Counter(list_1) == Counter(list_2)

if ((len(list_1) == len(list_2)) and
   (all(i in list_1 for i in list_2))):
    print 'True'
else:
    print 'False'

print "--------------------"

#12. Write a Python program to create an array contains six integers. Also print all the members of the array.
from array import array

my_array = array("i", [10, 20, 30, 40, 50, 60])

for i in my_array:
    print i

