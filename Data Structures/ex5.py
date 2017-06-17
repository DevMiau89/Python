#7. Write a Python program to count the number of students of individual class.
from collections import defaultdict

classes = (
    ('V', 1),
    ('VI', 1),
    ('V', 2),
    ('VI', 2),
    ('VI', 3),
    ('VII', 1),
)

a_list = defaultdict(dict)

for key,value in classes:
    a_list[key] = value


print a_list

l = {(key, value) for key,value in classes}

print l