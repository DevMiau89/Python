#24. Write a Python program to create a dictionary from a string.

sample_string = 'w3resource'

d = {}
for i in sample_string:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

print d        

#25. Write a Python program to print a dictionary in table format. 
my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}  

for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    print row  



#26. Write a Python program to count the values associated with key in a dictionary.     
sample_data = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]

print(sum(d['success'] for d in sample_data))   
