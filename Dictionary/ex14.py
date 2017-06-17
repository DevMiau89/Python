#35. Write a Python program to sort Counter by value.
sample_data = {'Math':81, 'Physics':83, 'Chemistry':87}

new_d = {}
for k,v in (sample_data.items()):
    new_d[k] = v

print new_d    

from collections import Counter

x = Counter(sample_data)
print x.most_common()

#36. Write a Python program to create a dictionary from two lists without losing duplicate values.
keys = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'] 
values = [1, 2, 2, 3]


dic = dict(zip(keys,values))

print dic

#37. Write a Python program to replace dictionary values with their sum.

student_details={'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},{'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},{'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}  
 
def sum_math_v_vi_average(list_of_dicts):  
    for d in list_of_dicts:  
        n1 = d.pop('V')  
        n2 = d.pop('VI') 
        d['V+VI'] = (n1 + n2)/2      
    return list_of_dicts  

print "------------------------------"
print sum_math_v_vi_average(student_details)
