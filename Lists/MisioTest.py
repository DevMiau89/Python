
# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *

array_of_6 = ["*","*","*","*","*","*"]
array_of_4 = []
array_of_3 = []

for i in range(4):
    array_of_4.append(array_of_6)

print array_of_4

for i in range(3):
    array_of_3.append(array_of_4)

print array_of_3


#ex18 Write a Python program to generate all permutations of a list in Python.

def permutations_generator(lst1):
    if len(lst1) == 0:
        yield []
    elif len(lst1) == 1:
        yield lst1 
    else:
        for i in range(len(lst1)):
            x = lst1[i]
            xs = lst1[:i] + lst1[i+1:]
            for p in permutations_generator(xs):
                yield [x] + p

data = list('abc')

for p in permutations_generator(data):
    print p

from itertools import permutations

print (list(permutations([1,2,3])))

#ex19. Write a Python program to get the difference between the two lists.

list_1 = [1,2,3,7,8,9]
list_2 = [1,2,3,5,7,8]

set_1 = set(list_1)
set_2 = set(list_2)

temp3 = [x for x in set_1 if x not in set_2]

print temp3

from collections import Counter

list_1 = [1,2,7,8,9]
list_2 = [1,2,3,5,7,8]

c1 = Counter(list_1)
c2 = Counter(list_2)

diff2 = list(c2 - c1)
diff1= list(c1 - c2)

print diff1
print diff2