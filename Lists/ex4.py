#ex20. Write a Python program access the index of a list. 

my_list = [1,2,3]

for i,j in enumerate(my_list):
    print i,j

#21. Write a Python program to convert a list of characters into a string.   


my_list = ['a','b','c']
new_list = ''.join(my_list)

print new_list

#22. Write a Python program to find the index of an item in a specified list
#my_list = ['a','b','c']

def find_item(item, list1):
    for i in list1:
        if item in list1:
            return list1.index(item)


print find_item('a', ['a','b','c'])            


#ex23. Write a Python program to flatten a shallow list.

from itertools import chain

my_list = [['a','b','c'],['d'], ['i']]
chain = chain(*my_list)

print list(chain)

#ex24. Write a Python program to append a list to the second list. 

color_list = ['red', 'blue', 'green']
color_list1 = ['grey']

new_list = color_list1 + color_list

print new_list

#25. Write a Python program to select an item randomly from a list.

import random

color_list = ['red', 'blue', 'green']

x = random.choice(color_list)
print x

