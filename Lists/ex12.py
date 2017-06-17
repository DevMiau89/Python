#48. Write a Python program to print a nested lists (each list on a new line) using the print() function.

a_list = [['Red'], ['Green'], ['Black']]  

for x in a_list:
    print x


#ex49. Write a Python program to convert list to list of dictionaries.

lst1 = ["Black", "Red", "Maroon", "Yellow"]
lst2 = ["#000000", "#FF0000", "#800000", "#FFFF00"]

seq = ("color_name","color_code")
new_dict = dict.fromkeys(seq)

for i in range(4):
    color_name = lst1[i]
    color_code = lst2[i]
    new_dict = dict.fromkeys(seq)
    new_dict["color_name"] = color_name
    new_dict["color_code"] = color_code
    print new_dict
    
#50. Write a Python program to sort a list of nested dictionaries.

my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}] 

my_list.sort(reverse = True)

print my_list   

#51. Write a Python program to split a list every Nth element. 
sample_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
new_list = []
new_list.append(sample_list[0:5])
new_list.append(sample_list[5:10])
new_list.append(sample_list[10:])

print new_list

def split_nth(lst, n):
    new_list = []
    for i in range(0, len(lst), n):
        new_list.append(lst[i:i+n])  
    return new_list    

print split_nth(sample_list,3)  

def list_slice(lst1, step):  
    return [lst1[i::step] for i in range(step)]  
print list_slice(sample_list,3)  