#27. Write a Python program to separate and print the numbers of a given string.
import re

my_string = "Ten 10, Twenty 20, Thirty 30"

# result_1 = [x for x in re.split(r'\D+', my_string) if x != '']

# print result_1
# print "======================"

pattern = r'\D+'

result_2 = re.split(pattern,my_string)

for i in result_2:
    if i != "":
        print i

print "--------------------------------"

#28. Write a Python program to find all words starting with 'a' or 'e' in a given string.        

str_example = "evan and aqua produce good water eee aaaa."

my_pattern = r'(\b[a]\w+)|(\b[e]\w+)'

m = re.findall(my_pattern,str_example)

print m
