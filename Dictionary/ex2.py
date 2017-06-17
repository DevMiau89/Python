dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}


new_d = {}
for i in dic1,dic2,dic3:
    new_d.update(i)
print new_d

#4. Write a Python script to check if a given key already exists in a dictionary.
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

key_check = d.has_key(1)

print key_check

for i in d:
    key_check = d.has_key(i)
    print key_check


def key_check(d, key):
    if key in d:
        print "Key exists"
    else: 
        print "Key does not exists"


key_check({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}, 1)   

#5. Write a Python program to iterate over dictionaries using for loops.   

d = {'x': 10, 'y': 20, 'z': 30}   

for i_key, i_value in d.items():
    print i_key, "=", i_value