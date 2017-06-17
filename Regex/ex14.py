#18. Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string.
import re

my_string = "Exercises number 1, 12, 13, and 345 are important"

p = re.findall(r'\d{1,3}', my_string)

for i in p:
    print i


