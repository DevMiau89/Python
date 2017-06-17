#28. Write a Python program to sort a list alphabetically in a dictionary.
num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}  

 
sorted_num = {k: sorted(v) for k,v in num.items()}

print sorted_num

for k,v in num.items():
    num[k] = sorted(v)

print num    
    
#29. Write a Python program to remove spaces from dictionary keys. 
my_dict = {'C  14': ['15263808', '13210478'], 'W   1': ['13122205']}

updated_dict = {k.replace(' ', ''):v for k,v in my_dict.items()}

print updated_dict
#29. Write a Python program to remove spaces from dictionary keys. 

for key in my_dict.keys():
    if " " in key:
        my_dict[key.translate(None," ")] = my_dict[key]
        del my_dict[key]

print "--------------------"
print my_dict

#30. Write a Python program to get the top three items in a shop. 
from collections import Counter

d = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}

three_numbers = dict(Counter(d).most_common(3))

print three_numbers

from heapq import nlargest
from operator import itemgetter  

for name,value in nlargest(3, d.items(),  key=itemgetter(1)):
    print name,value



 