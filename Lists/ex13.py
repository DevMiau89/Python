#ex52. Write a Python program to compute the similarity between two lists.

sample_list1 = ["red", "orange", "green", "blue", "white"]
sample_list2 = ["black", "yellow", "green", "blue"]
set1 = set(sample_list1)
set2 = set(sample_list2)

print set1.difference(set2) 
print set2.difference(set1) 

#53. Write a Python program to create a list with infinite elements.
import itertools
c = itertools.count()

print(next(c))  
print(next(c))  
print(next(c))  
print(next(c))  

#54. Write a Python program to concatenate elements of a list. 
a_list = [1,2,3,4,5]

my_lst_str = ''.join(map(str, a_list))

print(my_lst_str)

color = ['red', 'green', 'orange']

print "".join(color)

#55. Write a Python program to remove key values pairs from a list of dictionaries.

new_list = [{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value3', 'key2': 'value4'}]

print("Original List: ")  
print(new_list)  
new_list = [{k: v for k, v in d.items() if k != 'key1'} for d in new_list]  
print("New List: ")  
print(new_list) 

#56. Write a Python program to convert a string to a list.
color = "black", "yellow", "green", "blue"

a_list = list(color)

print a_list