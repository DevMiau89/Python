#26. Write a python program to check whether two lists are circularly identical.

list1 = [10, 10, 0, 0, 10]  
list2 = [10, 10, 10, 0, 0]  
list3 = [1, 10, 10, 0, 0]  

print ' '.join(map(str, list1 * 2))

print('Compare list1 and list2')  
print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))  
print('Compare list1 and list3')  
print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2))) 

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))

print squared

#27. Write a Python program to find the second smallest number in a list.


def second_smallest(numbers):
    numbers.sort()  
    sorted_list = numbers
    return sorted_list[1]
        

print(second_smallest([1, 2, -8, -2, 0]))  

#28. Write a Python program to find the second largest number in a list.

def second_smallest(numbers):
    numbers.sort()  
    sorted_list = numbers
    return sorted_list[-2]
        

print(second_smallest([1, 2, -8, -2, 0]))  

#ex29. Write a Python program to get unique values from a list. 

mylist = [1,1,2,2,-2, -8, -2, 0]

set_list = set(mylist)

print set_list

