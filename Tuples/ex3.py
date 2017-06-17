#7. Write a Python program to get the 4th element and 4th element from last of a tuple. 

tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")  

print tuplex[3]
print tuplex[-4]

#8. Write a Python program to create the colon of a tuple.
from copy import deepcopy

tuplex = ("HELLO", 5, [], True)

z  = deepcopy(tuplex)
z[2].append(20)

print tuplex
print z
print "---------------------"

#9. Write a Python program to find the repeated items of a tuple.

my_tup = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")  

my_dict = dict.fromkeys(my_tup,0)


for key in my_tup:
    my_dict[key] += 1

print my_dict

for key in my_dict:
    my_dict[key] += 1
    
    
print my_dict      

letter_count = my_tup.count("e")
print "---------------------"
print letter_count
