#37. Write a python program to convert snake case string to camel case string.
import re

my_string = 'python_exercises'

p = ''.join(x.capitalize() for x in my_string.split('_'))

print p

#38. Write a Python program to extract values between quotation marks of a string.

a_string = 'I found a note and it says "Hello World" - "Hello Python" -  "Hello PHP"'

print re.findall(r'".*?"', a_string)

