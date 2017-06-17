list1 = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]] 

list1.sort()

new_lst = []

for i in list1:
    if i not in new_lst:
        new_lst.append(i)
print new_lst

#70. Write a Python program to check if all dictionaries in a list are empty or not.

Sample_list = [{},{},{}]

Sample_list1 = [{"kot": 1},{},{}]

print all(not d for d in Sample_list)
print all(not d for d in Sample_list1)
print()
for i in Sample_list1:
    if i == {"kot": 1}:
        print True
    else:
        print False  

print ()
for i in Sample_list:
    if i == {}:
        print True
    else:
        print False          


