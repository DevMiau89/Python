#10. Write a Python program to group a sequence of key-value pairs into a dictionary of lists.
from collections import defaultdict

class_roll = [('v', 1), ('vi', 2), ('v', 3), ('vi', 4), ('vii', 1)]

new_dict = defaultdict(list)

for k,v in sorted(class_roll):
    new_dict[k].append(v)

sorted_dict = sorted(new_dict.items(), key=lambda x: x[0])

print sorted_dict