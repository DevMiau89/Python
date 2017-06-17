#ex7 Write a Python program to remove duplicates from a list.

sample_list = ['abc', 'xyz', 'aba', 'abc']
new_list = set(sample_list)

items = new_list.intersection()
        

print items   

#ex8 Write a Python program to check a list is empty or not.

sample_list1 = ['abc', 'xyz', 'aba', 'abc']

if len(sample_list) == 0:
    print "list is empty"
else:
    print "list is not empty"   


#ex9 Write a Python program to clone or copy a list     

old_list = ['abc', 'xyz', 'aba', 'abc']
new_list = list(old_list)

print old_list
print new_list

#ex11 Write a Python function that takes two lists and returns True if they have at least one common member.

def compare_elem(items1, items2):
    result = False
    for i in items1:
        for j in items2:
            if i == j:
                result = True
                return result
           
                


print compare_elem(['ab', 'xz', 'abad', 'abc'], ['abc', 'xyz', 'aba', 'abc'])                  

#ex12 Write a Python program to print a specified list after removing the 0th, 2nd, 4th and 5th elements.

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]  
print(color)  
