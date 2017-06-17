#1. Write a Python script to sort (ascending and descending) a dictionary by value.
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}  

z = sorted(d.values())
x = sorted(d.values(), reverse = True)

print z
print x

import operator
sorted_lst = sorted(d.items(), key=operator.itemgetter(0))

print sorted_lst

#2. Write a Python script to add a key to a dictionary. 
sample_dictionary = {0: 10, 1: 20}
key = {2: 30}

sample_dictionary.update(key)

print sample_dictionary

#ex3. Write a Python script to concatenate following dictionaries to create a new one.

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic1.update(dic2)
dic1.update(dic3)

print dic1

new_d = {}
for i in dic1,dic2,dic3:
    new_d.update(i)
print new_d

