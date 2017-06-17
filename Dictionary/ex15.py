#38. Write a Python program to convert a dictionary to OrderedDict.
import collections

Bob = {"W": 25, "Race": "White", "Job": "Mechanic", "Random": "stuff"} 

print Bob
print "----------------------"
Bob = collections.OrderedDict(Bob)

print Bob

print "------------------------------"

#39. Write a Python program to match key values in two dictionaries.
x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}

for key in x.keys():
    if key in y.keys():
        print "{} is present in both x and y".format(key)
    else:
        print "{} is NOT present in both x and y".format(key)    
    