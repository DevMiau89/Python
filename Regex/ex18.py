#22. Write a Python program to find the occurrence and position of the substrings within a string.
import re

my_string = 'Python exercises, PHP exercises, C# exercises'
occurrence = 0
for m in re.finditer('exercises', my_string):
    if m:
        occurrence += 1
    print m.start(),":", m.end()

print "Exercises occur:", occurrence

