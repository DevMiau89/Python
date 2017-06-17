#29. Write a Python program to separate and print the numbers and their position of a given string.
import re

my_string = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

p = re.search(r'\d+', my_string)

print p.span()
print "---------------------"

#30. Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.
str_1 = "Road, sixty six."

p = re.sub('Road', 'Rd.', str_1)

print p
print "--------------------"

#31. Write a Python program to replace all occurrences of space, comma, or dot with a colon. 

str_2 = "Road, sixty six."

pattern = r"\,|\ |\."

replace = re.sub(pattern, ":", str_2)

print replace 
print '--------------------'

#32. Write a Python program to replace maximum 2 occurrences of space, comma, or dot with a colon. 

text = 'Python Exercises, PHP exercises.'

pattern = r"[ ,.]"

rep = re.sub(pattern, ":", text, 2)

print rep