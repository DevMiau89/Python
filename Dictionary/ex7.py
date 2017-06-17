#18. Write a Python program to check a dictionary is empty or not. 

d = {}
d1 = {'food': 'spam', 'age': 42, 'name': 'Monty'}

print all(x==0 for x in d.keys())
print all(x==0 for x in d1.keys())

print all(x==0 for x in d.values())
print all(x==0 for x in d1.values())

if not d:
    print "Dictionary is empty"
else:
     print "Dictionary is not empty"   

if not bool(d1):
    print "Dictionary is empty"
else:
     print "Dictionary is not empty"       


#19. Write a Python program to combine two dictionary adding values for common keys.

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
   
new_dic = d2

for i in d1.keys():
    if i not in new_dic:
        new_dic[i] = d1[i]
    else:            
        new_dic[i] += d1[i]    

print new_dic  

from collections import Counter

d1 = {'a': 100, 'b': 200, 'c':300}  
d2 = {'a': 300, 'b': 200, 'd':400}  
d = Counter(d1) + Counter(d2)  
print(d)  


