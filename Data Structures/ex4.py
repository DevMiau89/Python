#5. Write a Python program to count the most common words in a dictionary.
words = [  
   'red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes',  
   'white', 'black', 'orange', 'pink', 'pink', 'red', 'red', 'white', 'orange',  
   'white', "black", 'pink', 'green', 'green', 'pink', 'green', 'pink',  
   'white', 'orange', "orange", 'red'  
]

from collections import *

print Counter(words).most_common(4)
print "---------------------------"

#6. Write a Python program to find the class wise roll number from a tuple-of-tuples.
from collections import defaultdict  
classes = (  
    ('V', 1),  
    ('VI', 1),  
    ('V', 2),  
    ('VI', 2),  
    ('VI', 3),  
    ('VII', 1),  
) 

z = defaultdict(list)

for key,value in classes:
    z[key].append(value)

print z    
