#22. Write a Python program to replace last value of tuples in a list.
sample_t =  [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

sample_t[:5]

print sample_t

#23. Write a Python program to sort a tuple by its float element.
sample_data = [('item1', '19.20'), ('item2', '15.10'), ('item3', '24.5')]

from operator import itemgetter

t = sorted(sample_data, key= itemgetter(1))

print t

#24. Write a Python program to count the elements in a list until an element is a tuple.

num = [10,20,30,{10:20},40] 

counter = 0
for i in num:
    counter += 1 
    if isinstance(i, dict):
        counter -= 1

print "--------------------"
print counter        
