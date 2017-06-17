#9. Write a Python program to iterate over dictionaries using for loops. 
d = {'Red': 1, 'Green': 2, 'Blue': 3}   
for color_key, value in d.items():
    print(color_key, 'corresponds to ', d[color_key])   


#10. Write a Python program to sum all the items in a dictionary.
d = {'key1':1,'key2':14,'key3':47}

print sum(d.values())

#11. Write a Python program to multiply all the items in a dictionary.
d = {'key1':1,'key2':14,'key3':47}

print d["key1"]

result = 1
for key in d:
    d[key] = d[key] * d[key]
    result = result * d[key]
print d
print result


#12. Write a Python program to remove a key from a dictionary. 
d = {'key1':1,'key2':14,'key3':47}

d.pop("key1", None)

print d