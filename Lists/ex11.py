#46. Write a Python program to select the odd items of a list.

def odd_numbers(lst1):
    new_list = []
    for i in lst1:
        if i % 2 != 0:
            new_list.append(i)
    return new_list

print odd_numbers([1,2,3,4,5]) 

#47. Write a Python program to insert an element before each element of a list. 

a_list = [1,2,3,4,5]

def add_element(lst1):
    new_list = []
    for i in lst1:
        new_list.append("e")
        new_list.append(i)
    return new_list


print add_element([1,2,3,4,5])

color = ['Red', 'Green', 'Black']  
new_list = []

for elt in color:   
    for v in ("c", elt):
        new_list.append(v)
print new_list


    
