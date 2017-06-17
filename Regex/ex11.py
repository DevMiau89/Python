#13. Write a Python program that matches a word containing 'z', not start or end of the word. 
import re

my_string = "Thez zquick brownza fox jumpzsz over the lazy dogz"    
pattern = re.findall(r'\w+z\w+?', my_string)

for i in pattern:    
    if pattern:
        print i
    else:
        print False



#14. Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
str1 = "Python Exercises"

p = re.match(r'^[a-zA-z0-9_]*$', str1)

if p:
    print "found a match"
else:
    print "no match found"