#13. Write a Python program to map two lists into a dictionary.
keys = ('name', 'age', 'food')
values = ('Monty', 42, 'spam')

l = dict(zip(keys,values))

print l
print "----------------"

new_dic = {k:v for k,v in zip(keys, values)}

print new_dic

#14. Write a Python program to sort a dictionary by key.
d1 = {'food': 'spam', 'age': 42, 'name': 'Monty'}

for k,v in sorted(d1.items(),key = lambda x: x[0]):
    print k,v

print "----------------"

color_dict = {'red':'#FF0000',  
          'green':'#008000',  
          'black':'#000000',  
          'white':'#FFFFFF'}    

for key in sorted(color_dict):
    print "{0} = {1}".format(key, color_dict[key])


#15. Write a Python program to get the maximum and minimum value in a dictionary.
d2 = {'food': 1, 'age': 42, 'name': 30}
print "----------------"
print max(d2, key= lambda x: d2[x])
print min(d2, key= lambda x: d2[x])

import operator

result = max(d2.iteritems(), key=operator.itemgetter(1))
result1 = min(d2.iteritems(), key=operator.itemgetter(1))
print "----------------"
print result
print result1