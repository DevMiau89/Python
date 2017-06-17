#20. Write a Python program to print all unique values in a dictionary.
Sample_Data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

s = set(val for x in Sample_Data for val in x.values())

print s

#21. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. 
import itertools

d = {'1':['a','b'], '2':['c','d']}

for x in itertools.product(*[d[k] for k in d.keys()]):
    print ''.join(x)

#22. Write a Python program to find the highest 3 values in a dictionary.
from heapq import nlargest

my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}

three_largest = nlargest(3, my_dict, key=my_dict.get)

print(three_largest)

#23. Write a Python program to combine values in python list of dictionaries.
d1 = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

from collections import Counter

result = Counter()  
for d in d1:  
    result[d['item']] += d['amount']  
print(result)  

