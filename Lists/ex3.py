
array = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]  
print(array) 

#ex14. Write a Python program to print the numbers of a specified list after removing even numbers from it.  

even_list = [1, 2, 3, 4, 2, 3, 4, 2, 7, 2]

new_list = [x for x in even_list if x % 2]

print new_list

import random

def my_shuffle(ls):
    random.shuffle(ls)
    return ls


print my_shuffle([1, 2, 3, 4, 2, 3, 4, 2, 7, 2])   

#ex15. Write a Python program to shuffle and print a specified list.
from random import shuffle

even_list2 = [4, 2, 7, 2]
shuffle(even_list2)
new = even_list2
print new

#ex16 Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included)

from math import *
square_list = []
counter = 0
while len(square_list) != 30:
    counter += 1
    power1 = pow(counter, 2)
    square_list.append(power1)
    

print square_list[0:5] + square_list[-5:]
print square_list[5:] 
    





