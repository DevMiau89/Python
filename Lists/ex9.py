#40. Write a Python program to split a list based on first character of word.

from itertools import groupby
from operator import itemgetter

somelist = ["red", "blue","green"]

for letter, words in groupby(sorted(somelist), key= lambda elem: elem[1]):
    print letter
    for word in words:
        print word
    
   
list_of_tuples = [(1,2), (3,4), (5,0)]
new = min(list_of_tuples, key=itemgetter(1))

print new


#41. Write a Python program to create multiple lists.

from itertools import repeat

new_list = list(repeat(['x', 'y'], 5))

print new_list

obj = {}  
for i in range(1, 21):  
    obj[i] = []  
print obj

#42. Write a Python program to find missing and additional values in two lists.
a_list1 = ['a','b','c','d','e','f'] 
a_list2 = ['d','e','f','g','h']  

set1 = set(a_list1)
set2 = set(a_list2)

print "Missing values in second list: ", ",".join(set1.difference(set2)) 
print "Additional values in second list: ", ",".join(set2.difference(set1))

