#37. Write a Python program to find common items from two lists.

def find_common_elem(lst1, lst2):
    common_elem = []
    for i in lst1:
        for j in lst2:
            if i == j:
                common_elem.append(i)
    return common_elem


print find_common_elem([1,2,4], [1,6,5,2,4])   

my_list1 = [2,3,5,6,"red", "blue"]
my_list2 = [2,4,7,9,"blue"]             

set1 = set(my_list1)
set2 = set(my_list2)

print set1 & set2


#38. Write a Python program to change the position of every n-th value with the (n+1)th in a list. 

def change_position(lst1):    
    for i in range(len(lst1)-1):
        lst1[i] = lst1[i+1]

    return lst1
 
print change_position([7,1,7,1,7,1])        

