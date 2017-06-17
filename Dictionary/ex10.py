#26. Write a Python program to count the values associated with key in a dictionary. 

sample_data = [
           {'id': 1, 'success': True, 'name': 'Lary'},
           {'id': 2, 'success': False, 'name': 'Rabi'}, 
           {'id': 3, 'success': True, 'name': 'Alex'}
]


count_success = len(filter(lambda x:x.get('success'), sample_data))

print count_success
print "------------------"

result = 0
for i in sample_data:
     x = i.get('success')
     if x == True:
         result +=1

print result         
     
print "------------------"

#27. Write a Python program to convert a list into a nested dictionary of keys.

num_list = [1, 2, 3, 4] 

d = {}

for i in reversed(num_list):
    print i
    d = {i: d}
    

print d

num_list = [1, 2, 3, 4]  
new_dict = current = {}  
for name in num_list:  
    current[name] = {}  
    current = current[name]  
print(current)   