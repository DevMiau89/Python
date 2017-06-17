#67. Write a Python program to find all the values in a list are greater than a specified number.

list1 = [220, 330, 500]  
list2 = [12, 17, 21]  

print all(i >= 220 for i in list1)

print all(i >= 5 for i in list2)

#68. Write a Python program to extend a list without append.

list1 = [220, 330, 500]  
list2 = [12, 17, 21]  

list1.extend(list2)

extended_list = list1

print extended_list

#69. Write a Python program to remove duplicates from a list of lists.
import itertools  
num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]  
print("Original List", num)  
num.sort()  
new_num = list(num for num,_ in itertools.groupby(num))  
print("New List", new_num)  

list1 = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]] 

list1.sort()

new_lst = []

for i in list1:
    if i not in new_lst:
        new_lst.append(i)
print new_lst
