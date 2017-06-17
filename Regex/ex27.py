#39. Write a Python program to remove multiple spaces in a string.
import re

my_string = "The   fox jumped   over    the log."

pattern = re.sub(" +", " ", my_string)

print pattern

#40. Write a Python program to remove all whitespaces from a string.

a_string = "The   fox jumped   over    the log."

p = re.sub("\s", "", my_string)

print "----------------------"
print p