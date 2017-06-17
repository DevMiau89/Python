#6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

d = {}
for i in range(1,5): 
    d[i] = i*i
print d 

#7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.

d = {}
for i in range(1,16): 
    d[i] = i*i
print d 

#8. Write a Python script to merge two Python dictionaries.
d1 = {1:10, 2:20}
d2 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

d = d1.copy()
d.update(d2)

print d

